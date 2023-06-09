from api.settings import settings
from fastapi import APIRouter, status, Header, HTTPException
from fastapi.responses import JSONResponse
import jwt
from jwt import InvalidAudienceError
from typing import Dict, Callable
from api.middleware import API_UNAUTHORIZED, API_RESPONSES


router = APIRouter()


@router.get(
    f"{settings.API_DEFAULT_PATH}/login-aud",
    status_code=status.HTTP_200_OK,
    description="check if the user is authorized",
    response_model=Dict
)
# assign that function return's another function,
# and the function return's a JSONResponse or HTTPException
async def login_aud(Authorization: str = Header(default=None)) -> Callable[[str], JSONResponse | HTTPException]:
    """
    curl -H "Authorization: <YOUR_JWT_TOKEN>" -X GET http://localhost:8080/v1/jwt/login-aud
    """
    def __decode_jwt_token_aud(token: str) -> (JSONResponse | HTTPException):
        try:
            jwt.decode(
                token,
                key=settings.API_JWT_KEY,
                audience=[settings.API_JWT_DEFAULT_ISSUER, "lcs-42"],
                algorithms=[settings.API_JWT_DEFAULT_ALGORITHM]
            )
        except InvalidAudienceError:
            raise API_UNAUTHORIZED
        return API_RESPONSES[2]
    return __decode_jwt_token_aud(token=Authorization)
