const BASE_URL = "http://localhost:8000";

export const generateRecipes = async (ingredients, dietaryPreference = null, numRecipes = 3) => {
  const res = await fetch(`${BASE_URL}/api/recipes/generate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      ingredients,
      dietary_preference: dietaryPreference || null,
      num_recipes: numRecipes,
    }),
  });
  if (!res.ok) {
    const err = await res.json();
    throw new Error(err.detail || "Failed to generate recipes");
  }
  return res.json();
};

export const saveRecipe = async (recipe) => {
  const res = await fetch(`${BASE_URL}/api/recipes/save`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(recipe),
  });
  if (!res.ok) throw new Error("Failed to save recipe");
  return res.json();
};

export const getSavedRecipes = async () => {
  const res = await fetch(`${BASE_URL}/api/recipes/saved`);
  if (!res.ok) throw new Error("Failed to fetch saved recipes");
  return res.json();
};

export const deleteRecipe = async (id) => {
  const res = await fetch(`${BASE_URL}/api/recipes/saved/${id}`, {
    method: "DELETE",
  });
  if (!res.ok) throw new Error("Failed to delete recipe");
  return res.json();
};

export const getSearchHistory = async () => {
  const res = await fetch(`${BASE_URL}/api/ingredients/history`);
  if (!res.ok) throw new Error("Failed to fetch history");
  return res.json();
};
