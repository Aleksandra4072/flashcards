from pydantic import (
    BaseModel,
    Field
)


class GeneralResponse(BaseModel):
    message: str = Field(
        default="Signup successful"
    )
