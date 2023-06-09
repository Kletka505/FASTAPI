from datetime import datetime

from sqlalchemy import MetaData, TIMESTAMP, String, ForeignKey, Table, Column, Integer, JSON, Boolean

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=True),
    Column('permissions', JSON)
)

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String, nullable=False),
    Column('email', String, nullable=False),
    Column('hashed_password', String, nullable=False),
    Column('registered_at', TIMESTAMP, default=datetime.utcnow),
    Column('role_id', Integer, ForeignKey(role.c.id)),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False),
)

