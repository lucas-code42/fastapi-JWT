from datetime import datetime
import pytz
from fastapi import FastAPI, Response
from fastapi import status
from api.settings import settings
from typing import Dict
from api.security import auth_exp, auth_nbf, auth_iss, token_generators, auth_aud, auth_iat


app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION,
)
app.include_router(token_generators.router, tags=["jwt"])
app.include_router(auth_exp.router, tags=["auth_exp"])
app.include_router(auth_nbf.router, tags=["auth_nbf"])
app.include_router(auth_iss.router, tags=["auth_iss"])
app.include_router(auth_aud.router, tags=["auth_aud"])
app.include_router(auth_iat.router, tags=["auth_iat"])


@app.get(
    path=f"{settings.API_DEFAULT_PATH}/health",
    response_model=Dict,
    response_description="responds with a JSON to informe that service is alive",
    status_code=status.HTTP_200_OK,
    description="check if API is live",
    tags=["health"]
)
async def api_health(response: Response) -> Dict:
    tz = pytz.timezone("America/Sao_Paulo")
    response.headers["Content-type"] = "application/json"
    return {
        "serviceAlive": True,
        "serviceTZ": datetime.now(tz=tz)
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        workers=settings.API_DEFAULT_WORKERS,
        app="main:app",
        port=settings.API_DEFAULT_PORT,
        host=settings.API_DEFAULT_HOST,
        use_colors=True
    )
