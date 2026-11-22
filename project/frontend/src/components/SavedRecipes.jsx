import { useState } from "react";
import { deleteRecipe } from "../api";

const DIFFICULTY_COLOR = {
  Easy: "#22c55e",
  Medium: "#f59e0b",
  Hard: "#ef4444",
};

export default function SavedRecipes({ recipes, onDelete }) {
  const [expanded, setExpanded] = useState(null);
  const [deleting, setDeleting] = useState(null);

  const handleDelete = async (id) => {
    if (!window.confirm("Remove this recipe from your saved list?")) return;
    setDeleting(id);
    try {
      await deleteRecipe(id);
      onDelete(id);
    } catch (err) {
      alert("Failed to delete: " + err.message);
    } finally {
      setDeleting(null);
    }
  };

  if (recipes.length === 0) {
    return (
      <div className="card empty-state">
        <div className="empty-icon">📭</div>
        <p className="empty-text">No saved recipes yet.</p>
        <p className="empty-sub">Generate recipes and hit <strong>Save</strong> to store them here!</p>
      </div>
    );
  }

  return (
    <div className="saved-list">
      {recipes.map((recipe) => {
        const diffColor = DIFFICULTY_COLOR[recipe.difficulty] || "#6b7280";
        const isOpen = expanded === recipe.id;
        const date = new Date(recipe.created_at).toLocaleDateString("en-IN", {
          day: "numeric", month: "short", year: "numeric",
        });

        return (
          <div key={recipe.id} className="recipe-card saved-card">
            <div className="recipe-header">
              <div>
                <h3 className="recipe-title">{recipe.title}</h3>
                <div className="recipe-meta">
                  <span className="meta-badge">🍽 {recipe.cuisine_type}</span>
                  <span className="meta-badge">⏱ {recipe.prep_time}</span>
                  <span className="meta-badge difficulty-badge" style={{ color: diffColor }}>
                    ● {recipe.difficulty}
                  </span>
                  <span className="meta-badge date-badge">📅 {date}</span>
                </div>
              </div>
              <button
                className="btn btn-delete"
                onClick={() => handleDelete(recipe.id)}
                disabled={deleting === recipe.id}
              >
                {deleting === recipe.id ? "..." : "🗑 Delete"}
              </button>
            </div>

            <button
              className="toggle-btn"
              onClick={() => setExpanded(isOpen ? null : recipe.id)}
            >
              {isOpen ? "▲ Hide Details" : "▼ View Recipe"}
            </button>

            {isOpen && (
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
      })}
    </div>
  );
}
