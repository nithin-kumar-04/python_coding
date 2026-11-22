import { useState } from "react";
import { saveRecipe } from "../api";

const DIFFICULTY_COLOR = {
  Easy: "#22c55e",
  Medium: "#f59e0b",
  Hard: "#ef4444",
};

export default function RecipeCard({ recipe, onSaved }) {
  const [saving, setSaving] = useState(false);
  const [saved, setSaved] = useState(false);
  const [expanded, setExpanded] = useState(false);

  const handleSave = async () => {
    setSaving(true);
    try {
      await saveRecipe(recipe);
      setSaved(true);
      onSaved && onSaved();
    } catch (err) {
      alert("Failed to save recipe: " + err.message);
    } finally {
      setSaving(false);
    }
  };

  const diffColor = DIFFICULTY_COLOR[recipe.difficulty] || "#6b7280";

  return (
    <div className="recipe-card">
      {/* Header */}
      <div className="recipe-header">
        <div>
          <h3 className="recipe-title">{recipe.title}</h3>
          <div className="recipe-meta">
            <span className="meta-badge">🍽 {recipe.cuisine_type}</span>
            <span className="meta-badge">⏱ {recipe.prep_time}</span>
            <span className="meta-badge difficulty-badge" style={{ color: diffColor }}>
              ● {recipe.difficulty}
            </span>
          </div>
        </div>
        <button
          className="btn btn-save"
          onClick={handleSave}
          disabled={saving || saved}
          title={saved ? "Already saved!" : "Save recipe"}
        >
          {saved ? "✅ Saved" : saving ? "Saving..." : "🔖 Save"}
        </button>
      </div>

      {/* Toggle Details */}
      <button className="toggle-btn" onClick={() => setExpanded(!expanded)}>
        {expanded ? "▲ Hide Details" : "▼ View Full Recipe"}
      </button>

      {expanded && (
        <div className="recipe-details">
          <div className="detail-section">
            <h4 className="detail-heading">📋 Ingredients</h4>
            <pre className="detail-text">{recipe.ingredients}</pre>
          </div>
          <div className="detail-section">
            <h4 className="detail-heading">👨‍🍳 Instructions</h4>
            <pre className="detail-text">{recipe.instructions}</pre>
          </div>
        </div>
      )}
    </div>
  );
}
