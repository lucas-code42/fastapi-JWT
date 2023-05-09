from settings import settings
from fastapi import APIRouter, status
import jwt



router = APIRouter()


@router.get(
    f"{settings.API_DEFAULT_PATH}/auth",
    response_model=str,
    status_code=status.HTTP_200_OK,
    description="returns a jwt token"
)
async def auth() -> str:
    return _generate_jwt_token()


def _generate_jwt_token() -> str:
    payload = {"exp": settings.API_JWT_DEFAULT_EXP}
    return jwt.encode(
        payload=payload,
        key=settings.API_JWT_KEY,
        algorithm=settings.API_JWT_DEFAULT_ALGORITHM
    )
