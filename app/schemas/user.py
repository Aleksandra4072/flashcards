import uuid
from typing import Optional
from pydantic import (
    BaseModel,
    EmailStr,
    Field,
)
from datetime import datetime

from app.schemas import role


class AddRequest(BaseModel):
    email: EmailStr = Field(
        description='Email address',
        examples=['example@mial.com']
    )
    password: str = Field(
        description='Password',
        examples=['StrongPassword!123']
    )
    age: Optional[int] = Field(
        description='User age',
        examples=[2]
    )
    role_id: Optional[uuid.UUID] = Field(
        description='Role id',
        examples=["123e4567-e89b-12d3-a456-426614174000"]
    )


class AlterRequest(BaseModel):
    email: Optional[EmailStr] = Field(
        description='Email address',
        examples=['example@mial.com']
    )
    password: Optional[str] = Field(
        description='Password',
        examples=['StrongPassword!123']
    )
    age: Optional[int] = Field(
        description='User age',
        examples=[2]
    )
    role_id: Optional[uuid.UUID] = Field(
        description='Role id',
        examples=["123e4567-e89b-12d3-a456-426614174000"]
    )


class GetAllUserResponseItem(BaseModel):
    id: uuid.UUID
    email: str
    age: int
    created_at: datetime
    is_activated: bool
    path: str
    roles: list[role.GetRoleResponseItem]

    class Config:
        from_attributes = True


class GetAllUserResponse(BaseModel):
    users: list[GetAllUserResponseItem] = Field(
        description="List of all the users"
    )

    model_config = {
        "json_schema_extra": {
            "examples": [{
                'id': "123e4567-e89b-12d3-a456-426614174000",
                'email': 'example@mail.com',
                'age': '28',
                'created_at': '2024-07-18',
                'is_activated': True,
                'path': 'flkfslfjajlgnvu4309b4',
                'roles': [
                    {
                        'id': "123e4567-e89b-12d3-a456-426614174000",
                        'name': 'USER'
                    }
                ]
            }]
        }
    }
