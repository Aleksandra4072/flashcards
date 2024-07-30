import uuid
from typing import Optional
from pydantic import (
    BaseModel,
    Field,
)
from datetime import datetime


class AddRequest(BaseModel):
    title: str = Field(
        description='Title',
        examples=['Example title']
    )
    description: str = Field(
        description='Description',
        examples=['Example description']
    )


class AlterRequest(BaseModel):
    title: Optional[str] = Field(
        None,
        description='Bundle title',
        examples=['Example title']
    )
    description: Optional[str] = Field(
        None,
        description='Bundle description',
        examples=['Example description']
    )


class GetBundleResponseItem(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    last_reviewed: datetime
    public_url: str

    class Config:
        from_attributes = True


class GetAllBundleResponse(BaseModel):
    bundles: list[GetBundleResponseItem] = Field(
        description='List of bundles of the current user'
    )

    model_config = {
        "json_schema_extra": {
            "examples": [{
                'id': "123e4567-e89b-12d3-a456-426614174000",
                'title': 'Task title',
                'description': 'Task description',
                'last_reviewed': '2024-07-18',
                'public_url': "dgfjkh32ihkh4h95hjn",
            }]
        }
    }


class GetBundleResponse(BaseModel):
    bundle: Optional[GetBundleResponseItem] = Field(
        description='Bundle information'
    )

    model_config = {
        "json_schema_extra": {
            "examples": [{
                'id': "123e4567-e89b-12d3-a456-426614174000",
                'title': 'Task title',
                'description': 'Task description',
                'last_reviewed': '2024-07-18',
                'public_url': "dgfjkh32ihkh4h95hjn",
            }]
        }
    }