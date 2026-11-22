from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import engine, get_db
from gemini_service import generate_recipes

# Create all DB tables on startup
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Recipe Finder API", version="1.0.0")

# Allow requests from React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ──────────────────────────────────────────────
# Health check
# ──────────────────────────────────────────────
@app.get("/")
def root():
    return {"message": "🍳 AI Recipe Finder API is running!"}


# ──────────────────────────────────────────────
# Generate recipes via Gemini AI
# ──────────────────────────────────────────────
@app.post("/api/recipes/generate", response_model=schemas.GenerateRecipesResponse)
def generate_recipe_suggestions(
    request: schemas.RecipeGenerateRequest,
    db: Session = Depends(get_db),
):
    if not request.ingredients:
        raise HTTPException(
            status_code=400, detail="Please provide at least one ingredient."
        )

    # Persist search to history
    search = models.IngredientSearch(ingredients=", ".join(request.ingredients))
    db.add(search)
    db.commit()

    try:
        recipes = generate_recipes(
            request.ingredients,
            request.dietary_preference,
            request.num_recipes,
        )
    except Exception as exc:
        raise HTTPException(
            status_code=500, detail=f"Gemini AI error: {str(exc)}"
        )

    return schemas.GenerateRecipesResponse(
        recipes=[schemas.GeneratedRecipe(**r) for r in recipes],
        searched_ingredients=request.ingredients,
    )


# ──────────────────────────────────────────────
# Save a recipe
# ──────────────────────────────────────────────
@app.post("/api/recipes/save", response_model=schemas.RecipeResponse)
def save_recipe(recipe: schemas.RecipeSaveRequest, db: Session = Depends(get_db)):
    db_recipe = models.SavedRecipe(**recipe.model_dump())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


# ──────────────────────────────────────────────
# Get all saved recipes
# ──────────────────────────────────────────────
@app.get("/api/recipes/saved", response_model=List[schemas.RecipeResponse])
def get_saved_recipes(db: Session = Depends(get_db)):
    return (
        db.query(models.SavedRecipe)
        .order_by(models.SavedRecipe.created_at.desc())
        .all()
    )


# ──────────────────────────────────────────────
# Delete a saved recipe
# ──────────────────────────────────────────────
@app.delete("/api/recipes/saved/{recipe_id}")
def delete_saved_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = (
        db.query(models.SavedRecipe)
        .filter(models.SavedRecipe.id == recipe_id)
        .first()
    )
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found.")
    db.delete(recipe)
    db.commit()
    return {"message": "Recipe deleted successfully."}


# ──────────────────────────────────────────────
# Get recent ingredient search history
# ──────────────────────────────────────────────
@app.get("/api/ingredients/history")
def get_search_history(db: Session = Depends(get_db)):
    searches = (
        db.query(models.IngredientSearch)
        .order_by(models.IngredientSearch.searched_at.desc())
        .limit(10)
        .all()
    )
    return [
        {"id": s.id, "ingredients": s.ingredients, "searched_at": s.searched_at}
        for s in searches
    ]
