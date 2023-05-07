from datetime import datetime, timedelta
import jwt
from time import sleep
from jwt import ExpiredSignatureError

API_JWT_KEY = "2ae6dee2-be05-4a1e-9d1c-1e12579b5bdf"
API_JWT_DEFAULT_ALGORITHM = "HS256"
API_JWT_DEFAULT_EXP = datetime.utcnow() + timedelta(seconds=1)


def generate_jwt_token() -> str:
    payload = {"exp": API_JWT_DEFAULT_EXP}
    return jwt.encode(
        payload=payload,
        key=API_JWT_KEY,
        algorithm=API_JWT_DEFAULT_ALGORITHM
    )


def decode_jwt_token(token: str) -> bool:
    try:
        jwt.decode(
            token,
            key=API_JWT_KEY,
            algorithms=[API_JWT_DEFAULT_ALGORITHM]
        )
    except ExpiredSignatureError:
        raise Exception("erro de token expirado!!!")
    return True


if __name__ == "__main__":
    token = generate_jwt_token()
    sleep(2)

    x = None
    try:
        x = decode_jwt_token(token=token)
        print("***", x)
    except:
        print("x error")
