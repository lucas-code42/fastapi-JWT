from api.settings import settings
from fastapi import APIRouter, status, Header, HTTPException
from fastapi.responses import JSONResponse
import jwt
from jwt import ExpiredSignatureError
from typing import Dict, Callable, Any, Tuple


router = APIRouter()

UNAUTHORIZED = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="not today :'(",
    headers={"Content-type": "application/json"}
)

RESPONSE_1 = JSONResponse(
    content={"CATCHPHRASES_SAY": "D’oh!"}
)

RESPONSE_2 = JSONResponse(
    content={"HOMER_SIMPSON_SAY": "What’s up, Doc?"}
)


@router.get(
    f"{settings.API_DEFAULT_PATH}/login-exp",
    response_model=Dict,
    status_code=status.HTTP_200_OK,
    description="check if the user is authorized"
)
# assign that function return's another function,
# and the function return's a JSONResponse or HTTPException
async def login(TokenAcess_exp: str = Header(default=None)) -> Callable[[str], JSONResponse | HTTPException]:
    """
    curl -H "TokenAcess_exp: <YOUR_JWT_TOKEN>" -X GET http://localhost:8080/v1/jwt/login-exp
    """
    return decode_jwt_token_exp(token=TokenAcess_exp)


def decode_jwt_token_exp(token: str) -> RESPONSE_1:
    try:
        jwt.decode(
            token,
            key=settings.API_JWT_KEY,
            algorithms=[settings.API_JWT_DEFAULT_ALGORITHM]
        )
    except ExpiredSignatureError:
        raise UNAUTHORIZED
    return RESPONSE_1
