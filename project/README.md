# 🍳 AI Recipe Finder

A full-stack web application that uses **Google Gemini AI** to generate recipes based on ingredients you have at home.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 18 + Vite |
| Backend | Python + FastAPI |
| AI | Google Gemini 1.5 Flash |
| Database | SQLite + SQLAlchemy |
| Config | python-dotenv |

## Project Structure

```
project/
├── backend/
│   ├── main.py             # FastAPI app & REST API routes
│   ├── database.py         # SQLAlchemy + SQLite setup
│   ├── models.py           # DB table definitions
│   ├── schemas.py          # Pydantic request/response schemas
│   ├── gemini_service.py   # Gemini AI integration
│   ├── requirements.txt    # Python dependencies
│   └── .env                # API keys (DO NOT commit)
└── frontend/
    ├── src/
    │   ├── App.jsx          # Main app component
    │   ├── App.css          # All styles
    │   ├── api.js           # API call functions
    │   └── components/
    │       ├── IngredientInput.jsx
    │       ├── RecipeCard.jsx
    │       └── SavedRecipes.jsx
    ├── index.html
    ├── package.json
    └── vite.config.js
```

## REST API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/api/recipes/generate` | Generate recipes via Gemini AI |
| POST | `/api/recipes/save` | Save a recipe to database |
| GET | `/api/recipes/saved` | Get all saved recipes |
| DELETE | `/api/recipes/saved/{id}` | Delete a saved recipe |
| GET | `/api/ingredients/history` | Get recent search history |

## Setup & Run

### 1. Backend Setup

```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn main:app --reload --port 8000
```

The API will be available at: http://localhost:8000
Interactive API docs: http://localhost:8000/docs

### 2. Frontend Setup

```bash
cd frontend

# Install Node dependencies
npm install

# Start the dev server
npm run dev
```

The app will be available at: http://localhost:5173

## Features

- 🥘 **Add Ingredients** — Type ingredients you have and add them as tags
- 🎯 **Dietary Preferences** — Filter by Vegetarian, Vegan, Keto, etc.
- 🤖 **AI Recipe Generation** — Gemini AI creates detailed recipes
- 🔖 **Save Favorites** — Save recipes to SQLite database
- 🗑 **Delete Recipes** — Remove saved recipes you no longer need
- 📋 **Full Recipe View** — Ingredients list + step-by-step instructions
- 📅 **Search History** — Tracks your past ingredient searches
