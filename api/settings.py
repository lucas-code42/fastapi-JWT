from datetime import datetime, timedelta
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse


class Settings:
    API_TITLE: str = "FAST-API && JWT (SIMPLE EXAMPLE)"
    API_DESCRIPTION: str = "Simple project just for play around with fastapi and jwt"
    API_VERSION: str = "v0.0.1"
    
    API_DEFAULT_HOST: str = "localhost"
    API_DEFAULT_PATH: str = "/v1/jwt"
    API_DEFAULT_PORT: int = 8080
    API_DEFAULT_WORKERS: int = 2

    API_DEFAULT_AUTHORIZATION: str = "knock knock"
    
    API_JWT_KEY = "2ae6dee2-be05-4a1e-9d1c-1e12579b5bdf"
    API_JWT_DEFAULT_ALGORITHM = "HS256"
    API_JWT_DEFAULT_EXP = datetime.utcnow() + timedelta(minutes=40)
    API_JWT_DEFAULT_NBF = datetime.utcnow() + timedelta(seconds=5)
    API_JWT_DEFAULT_ISSUER = "52d7d8604bf71e968bf07d468c7d394bff7cb0bb142fd4da7a85dd6f8056a940"


settings = Settings()
    