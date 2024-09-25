from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base


# Tabela Pipocas e Sabores (já criadas anteriormente)
class Pipocas(Base):
    __tablename__ = "popcorns"

    id = Column(Integer, primary_key=True, index=True)
    created_on = Column(DateTime, index=True)
    taste_id = Column(Integer, ForeignKey('taste.id'))
    weight = Column(Float)
    quantity = Column(Float)

    taste = relationship("Sabores", back_populates="popcorns")
    orders = relationship("Orders", back_populates="popcorn")
    production = relationship("Production", back_populates="popcorn")


class Sabores(Base):
    __tablename__ = "taste"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    cost_by_gr = Column(Float)

    popcorns = relationship("Pipocas", back_populates="taste")


# Nova tabela Pontos de Venda
class PointOfSale(Base):
    __tablename__ = "points_of_sale"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, index=True)
    name = Column(String, index=True)

    orders = relationship("Orders", back_populates="point_of_sale")


# Nova tabela Pedidos
class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    order_date = Column(DateTime, index=True)
    popcorn_id = Column(Integer, ForeignKey('popcorns.id'))
    point_of_sale_id = Column(Integer, ForeignKey('points_of_sale.id'))
    total_price = Column(Float)

    popcorn = relationship("Pipocas", back_populates="orders")
    point_of_sale = relationship("PointOfSale", back_populates="orders")


# Nova tabela Produção
class Production(Base):
    __tablename__ = "production"

    id = Column(Integer, primary_key=True, index=True)
    production_date = Column(DateTime, index=True)
    quantity = Column(Float)
    popcorn_id = Column(Integer, ForeignKey('popcorns.id'))

    popcorn = relationship("Pipocas", back_populates="production")
