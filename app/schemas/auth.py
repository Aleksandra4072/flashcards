import re
from typing import Optional
from pydantic import (
    BaseModel,
    Field,
    EmailStr,
    field_validator
)


# Signup Schemas
class SignupRequest(BaseModel):
    email: EmailStr = Field(
        description='Email address',
        examples=['example@mial.com']
    )
    password: str = Field(
        description='Password',
        examples=['StrongPassword!123']
    )

    @field_validator("password")
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")

        if not re.search(r'[a-z]', v):
            raise ValueError("Password must contain at least one lowercase letter")

        if not re.search(r'[A-Z]', v):
            raise ValueError("Password must contain at least one uppercase letter")

        if not re.search(r'[0-9]', v):
            raise ValueError("Password must contain at least one number")

        if not re.search(r'[\W_]', v):
            raise ValueError("Password must contain at least one capital letter")

        return v


# Signin Schemas
class LoginRequest(BaseModel):
    email: EmailStr = Field(
        description='Email address',
        examples=['example@mial.com']
    )
    password: str = Field(
        description='Password',
        examples=['StrongPassword!123']
    )


class LoginResponse(BaseModel):
    access_token: str = Field(
        examples=['eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c']
    )


class TokenData(BaseModel):
    email: Optional[str] = None
    roles: Optional[list[str]] = []


class ReadTokenResponse(BaseModel):
    token_payload: str = Field(
        description='Token payload',
    )
