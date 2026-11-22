import { useState } from "react";

const DIETARY_OPTIONS = ["", "Vegetarian", "Vegan", "Gluten-Free", "Keto", "Low-Carb", "Dairy-Free"];

export default function IngredientInput({ onGenerate, loading }) {
  const [inputValue, setInputValue] = useState("");
  const [ingredients, setIngredients] = useState([]);
  const [dietary, setDietary] = useState("");
  const [numRecipes, setNumRecipes] = useState(3);

  const addIngredient = () => {
    const trimmed = inputValue.trim();
    if (trimmed && !ingredients.includes(trimmed)) {
      setIngredients([...ingredients, trimmed]);
      setInputValue("");
    }
  };

  const removeIngredient = (item) => {
    setIngredients(ingredients.filter((i) => i !== item));
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" || e.key === ",") {
      e.preventDefault();
      addIngredient();
    }
  };

  const handleGenerate = () => {
    if (ingredients.length === 0) return;
    onGenerate(ingredients, dietary, numRecipes);
  };

  return (
    <div className="card input-card">
      <h2 className="section-title">🥘 What's in your kitchen?</h2>
      <p className="subtitle">Add ingredients you have and let AI create recipes for you!</p>

      {/* Ingredient Input */}
      <div className="input-row">
        <input
          type="text"
          className="text-input"
          placeholder="e.g. chicken, tomato, garlic..."
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyDown={handleKeyDown}
        />
        <button className="btn btn-secondary" onClick={addIngredient}>
          + Add
        </button>
      </div>

      {/* Ingredient Tags */}
      {ingredients.length > 0 && (
        <div className="tags">
          {ingredients.map((ing) => (
            <span key={ing} className="tag">
              {ing}
              <button className="tag-remove" onClick={() => removeIngredient(ing)}>×</button>
            </span>
          ))}
        </div>
      )}

      {/* Options Row */}
      <div className="options-row">
        <div className="option-group">
          <label className="option-label">Dietary Preference</label>
          <select
            className="select-input"
            value={dietary}
            onChange={(e) => setDietary(e.target.value)}
          >
            {DIETARY_OPTIONS.map((opt) => (
              <option key={opt} value={opt}>{opt || "None"}</option>
            ))}
          </select>
        </div>

        <div className="option-group">
          <label className="option-label">Number of Recipes</label>
          <select
            className="select-input"
            value={numRecipes}
            onChange={(e) => setNumRecipes(Number(e.target.value))}
          >
            {[1, 2, 3, 4, 5].map((n) => (
              <option key={n} value={n}>{n} recipe{n > 1 ? "s" : ""}</option>
            ))}
          </select>
        </div>
      </div>

      <button
        className="btn btn-primary full-width"
        onClick={handleGenerate}
        disabled={ingredients.length === 0 || loading}
      >
        {loading ? "🤖 Generating..." : "✨ Find My Recipes"}
      </button>
    </div>
  );
}
