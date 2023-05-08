from datetime import datetime, timedelta


class Settings:
    API_DEFAULT_PATH: str = "/v1/jwt"
    API_DEFAULT_PORT: int = 8080
    API_DEFAULT_WORKERS: int = 3

    API_TITLE: str = "FAST-API && JWT (SIMPLE EXAMPLE)"
    API_DESCRIPTION: str = "Simple project just for play around with fastapi and jwt"
    API_VERSION: str = "v0.0.1"

    API_JWT_KEY = "2ae6dee2-be05-4a1e-9d1c-1e12579b5bdf"
    API_JWT_DEFAULT_ALGORITHM = "HS256"
    API_JWT_DEFAULT_EXP = datetime.utcnow() + timedelta(minutes=40)


settings = Settings()
    