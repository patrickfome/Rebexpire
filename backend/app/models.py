from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    nom = Column(String)
    email = Column(String, unique=True)
    telephone = Column(String)
    adresse = Column(String)
    password_hash = Column(String)

class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True)
    nom = Column(String)
    lien = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    documents = relationship("Document", back_populates="person")

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True)
    type = Column(String)
    expiry_date = Column(Date)
    renewal_started = Column(Boolean, default=False)
    renewal_date = Column(Date, nullable=True)
    person_id = Column(Integer, ForeignKey("persons.id"))
    person = relationship("Person", back_populates="documents")
