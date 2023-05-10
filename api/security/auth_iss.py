from api.settings import settings
from fastapi import APIRouter, status, Header, HTTPException
from fastapi.responses import JSONResponse
import jwt
from jwt import InvalidIssuerError
from typing import Dict, Callable


router = APIRouter()

UNAUTHORIZED = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="not today :'(",
    headers={"Content-type": "application/json"}
)

RESPONSE = [
    JSONResponse(content={"CATCHPHRASES_SAY": "D’oh!"}),
    JSONResponse(content={"HOMER_SIMPSON_SAY": "What’s up, Doc?"})
]


@router.get(
    f"{settings.API_DEFAULT_PATH}/login-iss",
    status_code=status.HTTP_200_OK,
    description="check if the user is authorized",
    response_model=Dict
)
# assign that function return's another function,
# and the function return's a JSONResponse or HTTPException
async def login_exp(Authorization: str = Header(default=None)) -> Callable[[str], JSONResponse | HTTPException]:
    """
    curl -H "Authorization: <YOUR_JWT_TOKEN>" -X GET http://localhost:8080/v1/jwt/login-iss
    """
    print(Authorization)
    def __decode_jwt_token_exp(token: str) -> (JSONResponse | HTTPException):
        try:
            jwt.decode(
                token,
                key=settings.API_JWT_KEY,
                issuer=settings.API_JWT_DEFAULT_ISSUER,
                algorithms=settings.API_JWT_DEFAULT_ALGORITHM
            )
        except InvalidIssuerError:
            raise UNAUTHORIZED
        return RESPONSE[1]
    return __decode_jwt_token_exp(token=Authorization)






