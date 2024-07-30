import datetime
import uuid
from typing import List
from sqlalchemy import (
    Column,
    String,
    Uuid,
    Integer,
    DateTime,
    Boolean,
    Table,
    ForeignKey
)
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.core.db_config import Base
from app.core.utils import utils

user_role_table = Table(
    "user_role",
    Base.metadata,
    Column("user_id", ForeignKey('users.id')),
    Column("role_id", ForeignKey('roles.id'))
)

user_task_table = Table(
    "user_task",
    Base.metadata,
    Column("user_id", ForeignKey('users.id')),
    Column("task_id", ForeignKey('tasks.id'))
)


class User(Base):
    __tablename__ = 'users'
    id: Mapped[Uuid] = mapped_column(Uuid(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    age = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime(timezone=True), nullable=True)
    is_activated = Column(Boolean, nullable=False, default=False)
    path = Column(String(255), nullable=False, default=utils.random_string())
    roles = relationship(
        'Role',
        back_populates='users',
        secondary=user_role_table,
        lazy="selectin"
    )
    bundles: Mapped[List["Bundle"]] = relationship(cascade="all, delete-orphan")


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Uuid(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    name = Column(String(255), unique=True, nullable=False)
    users = relationship(
        'User',
        back_populates='roles',
        secondary=user_role_table
    )


class Bundle(Base):
    __tablename__ = 'bundles'
    id: Mapped[Uuid] = mapped_column(Uuid(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    title = Column(String(255), unique=True, nullable=False)
    description = Column(String(1000), unique=False, nullable=True)
    last_reviewed = Column(DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow())
    public_url = Column(String(255), nullable=False, default=utils.random_string(), unique=True)
    user_id: Mapped[Uuid] = mapped_column(ForeignKey("users.id"), nullable=False)
    flashcards = relationship("Flashcard", cascade="all, delete-orphan")


class Flashcard(Base):
    __tablename__ = 'flashcards'
    id: Mapped[Uuid] = mapped_column(Uuid(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    term = Column(String(255), unique=False, nullable=False)
    description = Column(String(1000), unique=False, nullable=False)
    bundle_id: Mapped[Uuid] = mapped_column(ForeignKey("bundles.id"))
