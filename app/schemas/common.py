from pydantic import (
    BaseModel,
    Field
)


class GeneralResponse(BaseModel):
    message: str = Field(
        default="Message response from backend"
    )


class CropImgRequest(BaseModel):
    filename: str = Field(
        description='Name of the image cropped',
        examples=['filename', 'image']
    )
    left: int = Field(
        description='Left coordinate of the image cropped',
        examples=[1, 14]
    )
    top: int = Field(
        description='Top coordinate of the image cropped',
        examples=[1, 14]
    )
    right: int = Field(
        description='Right coordinate of the image cropped',
        examples=[1, 14]
    )
    bottom: int = Field(
        description='Bottom coordinate of the image cropped',
        examples=[1, 14]
    )

