from datetime import datetime, timedelta
import jwt
from time import sleep
from jwt import ExpiredSignatureError, PyJWTError, ImmatureSignatureError

API_JWT_KEY = "2ae6dee2-be05-4a1e-9d1c-1e12579b5bdf"
API_JWT_DEFAULT_ALGORITHM = "HS256"
API_JWT_DEFAULT_EXP = datetime.utcnow() + timedelta(seconds=1)
API_JWT_DEFAULT_NBF = datetime.utcnow() + timedelta(seconds=1)


# exp claim
class ExpClaim:
    def generate_jwt_token_exp(self) -> str:
        payload = {"exp": API_JWT_DEFAULT_EXP}
        return jwt.encode(
            payload=payload,
            key=API_JWT_KEY,
            algorithm=API_JWT_DEFAULT_ALGORITHM
        )

    def decode_jwt_token_exp(self, token: str) -> bool:
        try:
            decode = jwt.decode(
                token,
                key=API_JWT_KEY,
                algorithms=[API_JWT_DEFAULT_ALGORITHM]
            )
            print("EXP result:", decode)
        except ExpiredSignatureError as e:
            print(e)
            raise ExpiredSignatureError("Signature has expired (exp)")
        return True


# nbf claim
class NbfClaim():
    def generate_jwt_token_nbf(self) -> str:
        payload = {"nbf": API_JWT_DEFAULT_NBF}
        return jwt.encode(
            payload=payload,
            key=API_JWT_KEY,
            algorithm=API_JWT_DEFAULT_ALGORITHM
        )

    def decode_jwt_token_nbf(self, token: str) -> bool:
        try:
            decode = jwt.decode(
                token,
                key=API_JWT_KEY,
                algorithms=[API_JWT_DEFAULT_ALGORITHM]
            )
            print("NBF result:", decode)
        except ImmatureSignatureError:
            raise ImmatureSignatureError("The token is not yet valid (nbf)")
        return True


if __name__ == "__main__":
    token = ExpClaim().generate_jwt_token_exp()
    print(f"token EXP:\n{token}")
    x = None
    sleep(1.1)
    try:
        x = ExpClaim().decode_jwt_token_exp(token=token)
        print("EXP token is valid!")
    except PyJWTError as e:
        print(e)

    token = NbfClaim().generate_jwt_token_nbf()
    print(f"\ntoken NFB:\n{token}")
    x = None
    sleep(.1)
    try:
        x = NbfClaim().decode_jwt_token_nbf(token=token)
        print("NBF token is valid!")
    except PyJWTError as e:
        print(e)
