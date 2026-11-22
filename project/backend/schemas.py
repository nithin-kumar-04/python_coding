from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


class RecipeGenerateRequest(BaseModel):
    ingredients: List[str]
    dietary_preference: Optional[str] = None
    num_recipes: Optional[int] = 3


class RecipeSaveRequest(BaseModel):
    title: str
    ingredients: str
    instructions: str
    cuisine_type: Optional[str] = None
    prep_time: Optional[str] = None
    difficulty: Optional[str] = None


class RecipeResponse(BaseModel):
    id: int
    title: str
    ingredients: str
    instructions: str
    cuisine_type: Optional[str]
    prep_time: Optional[str]
    difficulty: Optional[str]
    created_at: datetime

    model_config = {"from_attributes": True}


class GeneratedRecipe(BaseModel):
    title: str
    ingredients: str
    instructions: str
    cuisine_type: str
    prep_time: str
    difficulty: str


class GenerateRecipesResponse(BaseModel):
    recipes: List[GeneratedRecipe]
    searched_ingredients: List[str]
