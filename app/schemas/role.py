import uuid
from pydantic import BaseModel, Field


class GetRoleResponseItem(BaseModel):
    id: uuid.UUID
    name: str

    class Config:
        from_attributes = True


class GetAllRolesResponse(BaseModel):
    roles: list[GetRoleResponseItem] = Field(
        description='List of flashcards of the current user'
    )

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "roles": [
                    {
                        'id': "123e4567-e89b-12d3-a456-426614174000",
                        'name': 'USER'
                    },
                    {
                        'id': "123e4567-e89b-12d3-a456-43847248432",
                        'term': 'ADMIN'
                    },
                ]
            }]
        }
    }