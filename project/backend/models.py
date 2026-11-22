from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from database import Base


class SavedRecipe(Base):
    __tablename__ = "saved_recipes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    ingredients = Column(Text, nullable=False)
    instructions = Column(Text, nullable=False)
    cuisine_type = Column(String(100))
    prep_time = Column(String(50))
    difficulty = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)


class IngredientSearch(Base):
    __tablename__ = "ingredient_searches"

    id = Column(Integer, primary_key=True, index=True)
    ingredients = Column(Text, nullable=False)
    searched_at = Column(DateTime, default=datetime.utcnow)
