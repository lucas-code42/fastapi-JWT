from typing import Annotated
from settings import settings
from fastapi import APIRouter, status, Header
import jwt


router = APIRouter()


@router.post(
    f"{settings.API_DEFAULT_PATH}/login",
    response_model=bool,
    status_code=status.HTTP_200_OK,
    description="check if the user is authorized"
)
async def login(authorization_token: str = Header(default=None)) -> bool:
    print(authorization_token)
    return _decode_jwt_token(token=authorization_token)


def _decode_jwt_token(token: str) -> bool:
    token_is_valid = jwt.decode(
        token,
        key=settings.API_JWT_KEY,
        algorithms=[settings.API_JWT_DEFAULT_ALGORITHM]
    )
