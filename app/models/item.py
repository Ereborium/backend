from sqlalchemy import Column, Integer, Float, String

from app.db.base_class import Base


class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    description = Column(String)
