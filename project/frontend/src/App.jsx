import { useState, useEffect, useCallback } from "react";
import IngredientInput from "./components/IngredientInput";
import RecipeCard from "./components/RecipeCard";
import SavedRecipes from "./components/SavedRecipes";
import { generateRecipes, getSavedRecipes } from "./api";
import "./App.css";

export default function App() {
  const [activeTab, setActiveTab] = useState("generate");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [generatedRecipes, setGeneratedRecipes] = useState([]);
  const [savedRecipes, setSavedRecipes] = useState([]);
  const [lastIngredients, setLastIngredients] = useState([]);

  const fetchSaved = useCallback(async () => {
    try {
      const data = await getSavedRecipes();
      setSavedRecipes(data);
    } catch {
      /* silently fail */
    }
  }, []);

  useEffect(() => {
    fetchSaved();
  }, [fetchSaved]);

  const handleGenerate = async (ingredients, dietary, numRecipes) => {
    setLoading(true);
    setError("");
    setGeneratedRecipes([]);
    setLastIngredients(ingredients);
    try {
      const data = await generateRecipes(ingredients, dietary, numRecipes);
      setGeneratedRecipes(data.recipes);
    } catch (err) {
      setError(err.message || "Something went wrong. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  const handleSaved = () => {
    fetchSaved();
  };

  const handleDelete = (deletedId) => {
    setSavedRecipes((prev) => prev.filter((r) => r.id !== deletedId));
  };

  return (
    <div className="app">
      {/* Header */}
      <header className="app-header">
        <div className="header-content">
          <div className="logo">🍳</div>
          <div>
            <h1 className="app-title">AI Recipe Finder</h1>
            <p className="app-tagline">Find delicious recipes from your ingredients</p>
          </div>
        </div>
      </header>

      {/* Tabs */}
      <nav className="tab-bar">
        <button
          className={`tab-btn ${activeTab === "generate" ? "active" : ""}`}
          onClick={() => setActiveTab("generate")}
        >
          ✨ Generate Recipes
        </button>
        <button
          className={`tab-btn ${activeTab === "saved" ? "active" : ""}`}
          onClick={() => { setActiveTab("saved"); fetchSaved(); }}
        >
          🔖 Saved Recipes
          {savedRecipes.length > 0 && (
            <span className="badge">{savedRecipes.length}</span>
          )}
        </button>
      </nav>

      {/* Content */}
      <main className="main-content">
        {activeTab === "generate" && (
          <div>
            <IngredientInput onGenerate={handleGenerate} loading={loading} />

            {error && (
              <div className="error-box">
                ⚠️ {error}
              </div>
            )}

            {loading && (
              <div className="loading-box">
                <div className="spinner" />
                <p>Gemini AI is cooking up recipes for you...</p>
              </div>
            )}

            {generatedRecipes.length > 0 && (
              <div className="results-section">
                <h2 className="results-title">
                  🎉 {generatedRecipes.length} Recipes found for:{" "}
                  <em>{lastIngredients.join(", ")}</em>
                </h2>
                {generatedRecipes.map((recipe, idx) => (
                  <RecipeCard key={idx} recipe={recipe} onSaved={handleSaved} />
                ))}
              </div>
            )}
          </div>
        )}

        {activeTab === "saved" && (
          <div>
            <div className="saved-header">
              <h2 className="section-title">🔖 Your Saved Recipes</h2>
              <span className="saved-count">{savedRecipes.length} recipe{savedRecipes.length !== 1 ? "s" : ""}</span>
            </div>
            <SavedRecipes recipes={savedRecipes} onDelete={handleDelete} />
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="app-footer">
        Built with ❤️ using React · FastAPI · SQLite
      </footer>
    </div>
  );
}
