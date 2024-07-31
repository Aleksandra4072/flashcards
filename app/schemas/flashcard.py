import uuid
from typing import Optional
from pydantic import (
    BaseModel,
    Field,
)


class BundleId(BaseModel):
    id: str = Field(
        description='Bundle ID',
        examples=['123e4567-e89b-12d3-a456-426614174000']
    )


class AddRequest(BaseModel):
    term: str = Field(
        description='Term',
        examples=['Example terminology']
    )
    description: str = Field(
        description='Description',
        examples=['Example term description']
    )
    bundle_id: str = Field(
        description='Bundle ID',
        examples=['123e4567-e89b-12d3-a456-426614174000']
    )


class AlterRequest(BaseModel):
    term: Optional[str] = Field(
        None,
        description='Flashcard term',
        examples=['Example terminology']
    )
    description: Optional[str] = Field(
        None,
        description='Term description',
        examples=['Example description']
    )


class GetFlashcardResponseItem(BaseModel):
    id: uuid.UUID
    term: str
    description: str

    class Config:
        from_attributes = True


class GetAllFlashcardsResponse(BaseModel):
    flashcards: list[GetFlashcardResponseItem] = Field(
        description='List of flashcards of the current user'
    )

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "flashcards": [
                    {
                        'id': "123e4567-e89b-12d3-a456-426614174000",
                        'term': 'Flashcard term',
                        'description': 'Term description',
                    },
                    {
                        'id': "123e4567-e89b-12d3-a456-43847248432",
                        'term': 'Flashcard term #2',
                        'description': 'Term description #2',
                    },
                ]
            }]
        }
    }


class GetFlashcardResponse(BaseModel):
    flashcard: Optional[GetFlashcardResponseItem] = Field(
        description='Flashcard information'
    )

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "flashcard":
                    {
                        'id': "123e4567-e89b-12d3-a456-426614174000",
                        'term': 'Flashcard term',
                        'description': 'Term description',
                    }
            }]
        }
    }
