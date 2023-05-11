from fastapi import status, HTTPException
from fastapi.responses import JSONResponse


API_UNAUTHORIZED = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="not today :'(",
    headers={"Content-type": "application/json"}
)

API_RESPONSES = [
    JSONResponse(content={"BUGS_BUNNY_SAY": "D’oh!"}),
    JSONResponse(content={"HOMER_SIMPSON_SAY": "What’s up, Doc?"}),
    JSONResponse(content={" BEAVIS_&_BUTT_HEAD_SAY": "PICKLE RIIIICK!"}),
    JSONResponse(content={"RICK_SAY": "Beavis, you are one stupid son of a bitch"})
]