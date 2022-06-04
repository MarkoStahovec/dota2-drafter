from sqlalchemy import Column, Integer, ForeignKey, text
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.sql.sqltypes import TIMESTAMP, VARCHAR

from .db.base import Base


class Heroes(Base):
    __tablename__ = "Heroes"

    hero_id = Column(Integer, primary_key=True, nullable=False)
    hero_name = Column(VARCHAR(40), unique=True, nullable=False)
    image_name = Column(VARCHAR(45), unique=True, nullable=False)
    primary_attr = Column(VARCHAR(8), nullable=False)


class Counters(Base):
    __tablename__ = "Counters"

    hero_id_1 = Column(Integer, ForeignKey("Heroes.hero_id", ondelete="CASCADE"), primary_key=True, nullable=False)
    hero_id_2 = Column(Integer, ForeignKey("Heroes.hero_id", ondelete="CASCADE"), primary_key=True, nullable=False)
    c_value = Column(Integer, nullable=False)


class Synergies(Base):
    __tablename__ = "Synergies"

    hero_id_1 = Column(Integer, ForeignKey("Heroes.hero_id", ondelete="CASCADE"), primary_key=True, nullable=False)
    hero_id_2 = Column(Integer, ForeignKey("Heroes.hero_id", ondelete="CASCADE"), primary_key=True, nullable=False)
    s_value = Column(Integer, nullable=False)

