from api.settings import settings
from fastapi import APIRouter, status, Header, HTTPException
import jwt

router = APIRouter()


UNAUTHORIZED = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="knock on the door before entering",
    headers={"Content-type": "application/json"}
)


def __validate_authorization(auth: str) -> bool:
    return auth == settings.API_DEFAULT_AUTHORIZATION


@router.get(
    f"{settings.API_DEFAULT_PATH}/exp",
    response_model=str,
    status_code=status.HTTP_200_OK,
    description="returns a jwt token exp"
)
async def generate_jwt_token_exp(Authorization: str = Header(default=None)) -> str:
    """
    curl -H "Authorization: toc toc" -X GET http://localhost:8080/v1/jwt/exp
    """
    if __validate_authorization(Authorization):
        payload = {"exp": settings.API_JWT_DEFAULT_EXP}
        return jwt.encode(
            payload=payload,
            key=settings.API_JWT_KEY,
            algorithm=settings.API_JWT_DEFAULT_ALGORITHM
        )
    raise UNAUTHORIZED


@router.get(
    f"{settings.API_DEFAULT_PATH}/nbf",
    response_model=str,
    status_code=status.HTTP_200_OK,
    description="returns a jwt token nbf"
)
def generate_jwt_token_nbf(Authorization: str = Header(default=None)) -> str:
    """
    curl -H "Authorization: toc toc" -X GET http://localhost:8080/v1/jwt/nbf
    """
    if __validate_authorization(auth=Authorization):
        payload = {"nbf": settings.API_JWT_DEFAULT_NBF}
        return jwt.encode(
            payload=payload,
            key=settings.API_JWT_KEY,
            algorithm=settings.API_JWT_DEFAULT_ALGORITHM
        )
    raise UNAUTHORIZED


@router.get(
    f"{settings.API_DEFAULT_PATH}/iss",
    response_model=str,
    status_code=status.HTTP_200_OK,
    description="returns a jwt token iss"
)
def generate_jwt_token_iss(self) -> str:
    payload = {"iss": settings.API_JWT_DEFAULT_ISSUER}
    return jwt.encode(
        payload=payload,
        key=settings.API_JWT_KEY,
        algorithm=settings.API_JWT_DEFAULT_ALGORITHM
    )


@router.get(
    f"{settings.API_DEFAULT_PATH}/aud",
    response_model=str,
    status_code=status.HTTP_200_OK,
    description="returns a jwt token aud"
)
def generate_jwt_token_iss(self) -> str:
    payload = {"aud": [settings.API_JWT_DEFAULT_ISSUER, "lcs-42"]}
    return jwt.encode(
        payload=payload,
        key=settings.API_JWT_KEY,
        algorithm=settings.API_JWT_DEFAULT_ALGORITHM
    )


@router.get(
    f"{settings.API_DEFAULT_PATH}/iat",
    response_model=str,
    status_code=status.HTTP_200_OK,
    description="returns a jwt token iat"
)
def generate_jwt_token_iat(self) -> str:
    week = (60 * 7 * 24)
    # (60 * 7 * 24) = 1week
    payload = {"iat": week, "iss": settings.API_JWT_DEFAULT_ISSUER}
    return jwt.encode(
        payload=payload,
        key=settings.API_JWT_KEY,
        algorithm=settings.API_JWT_DEFAULT_ALGORITHM
    )
