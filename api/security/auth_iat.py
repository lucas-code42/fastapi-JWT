from api.settings import settings
from fastapi import APIRouter, status, Header, HTTPException
from fastapi.responses import JSONResponse
import jwt
from jwt import InvalidIssuedAtError
from typing import Dict, Callable
from api.middleware import API_UNAUTHORIZED, API_RESPONSES


router = APIRouter()


@router.get(
    f"{settings.API_DEFAULT_PATH}/login-iat",
    status_code=status.HTTP_200_OK,
    description="check if the user is authorized",
    response_model=Dict
)
# assign that function return's another function,
# and the function return's a JSONResponse or HTTPException
async def login_iat(Authorization: str = Header(default=None)) -> Callable[[str], JSONResponse | HTTPException]:
    """
    curl -H "Authorization: <YOUR_JWT_TOKEN>" -X GET http://localhost:8080/v1/jwt/login-iat
    """
    def __decode_jwt_token_aud(token: str) -> (JSONResponse | HTTPException):
        try:
            jwt.decode(
                token,
                key=settings.API_JWT_KEY,
                options={"require": ["iat", "iss"]},
                issuer=settings.API_JWT_DEFAULT_ISSUER,
                algorithms=[settings.API_JWT_DEFAULT_ALGORITHM]
            )
        except InvalidIssuedAtError:
            raise API_UNAUTHORIZED
        return API_RESPONSES[0]
    return __decode_jwt_token_aud(token=Authorization)
