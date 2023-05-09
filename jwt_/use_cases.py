from datetime import datetime, timedelta
import jwt
from time import sleep
from jwt import ExpiredSignatureError, PyJWTError, ImmatureSignatureError, InvalidIssuerError, InvalidAudienceError, InvalidIssuedAtError

API_JWT_KEY = "2ae6dee2-be05-4a1e-9d1c-1e12579b5bdf"
API_JWT_DEFAULT_ALGORITHM = "HS256"
API_JWT_DEFAULT_EXP = datetime.utcnow() + timedelta(seconds=1)
API_JWT_DEFAULT_NBF = datetime.utcnow() + timedelta(seconds=1)


# all use cases are based on offical documentation
# https://pyjwt.readthedocs.io/en/stable/usage.html#issuer-claim-iss


# exp claim
class ExpClaim:
    """
    Expiration Time Claim (exp)
    The “exp” (expiration time) claim identifies the expiration time on or after which the JWT MUST NOT be accepted for processing. 
    The processing of the “exp” claim requires that the current date/time MUST be before the expiration date/time listed in the “exp” claim. 
    Implementers MAY provide for some small leeway, usually no more than a few minutes, to account for clock skew. 
    Its value MUST be a number containing a NumericDate value. Use of this claim is OPTIONAL.
    """
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
            raise ExpiredSignatureError("Signature has expired (exp)")
        return True


# nbf claim
class NbfClaim():
    """
    Not Before Time Claim (nbf)
    The “nbf” (not before) claim identifies the time before which the JWT MUST NOT be accepted for processing.
    The processing of the “nbf” claim requires that the current date/time MUST be after or equal to the not-before date/time listed in the “nbf” claim. 
    Implementers MAY provide for some small leeway, usually no more than a few minutes, to account for clock skew. 
    Its value MUST be a number containing a NumericDate value. 
    Use of this claim is OPTIONAL.
    """
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


# iss claim
class IssClaim():
    """
    Audience Claim (aud)
    The “aud” (audience) claim identifies the recipients that the JWT is intended for. 
    Each principal intended to process the JWT MUST identify itself with a value in the audience claim. 
    If the principal processing the claim does not identify itself with a value in the “aud” claim when this claim is present, then the JWT MUST be rejected.
    """
    def generate_jwt_token_iss(self) -> str:
        payload = {"iss": "urn:lcs42"}
        return jwt.encode(
            payload=payload,
            key=API_JWT_KEY,
            algorithm=API_JWT_DEFAULT_ALGORITHM
        )

    def decode_jwt_token_iss(self, token: str) -> bool:
        try:
            decode = jwt.decode(
                token,
                key=API_JWT_KEY,
                issuer="urn:lcs42",
                algorithms=API_JWT_DEFAULT_ALGORITHM
            )
            print("ISS result:", decode)
        except InvalidIssuerError:
            raise InvalidIssuerError("Invalid issuer")


# aud claim
class AudClaim():
    """
    Audience Claim (aud)
    The “aud” (audience) claim identifies the recipients that the JWT is intended for. 
    Each principal intended to process the JWT MUST identify itself with a value in the audience claim. 
    If the principal processing the claim does not identify itself with a value in the “aud” claim when this claim is present, then the JWT MUST be rejected.

    If the audience claim is incorrect, jwt.InvalidAudienceError will be raised.
    """
    def generate_jwt_token_aud(self) -> str:
        payload = {"aud": ["urn:lcs42", "pythonjwt"]}
        return jwt.encode(
            payload=payload,
            key=API_JWT_KEY,
            algorithm=API_JWT_DEFAULT_ALGORITHM
        )

    def decode_jwt_token_aud(self, token: str) -> bool:
        try:
            decode = jwt.decode(
                token,
                key=API_JWT_KEY,
                # we can pass a list and if one of those are true the decode is successfully
                audience=["urn:qw", "332"],
                algorithms=API_JWT_DEFAULT_ALGORITHM
            )
            print("AUD result:", decode)
        except InvalidAudienceError:
            raise InvalidAudienceError("Invalid audience")


# iat claim
class IatClaim():
    """
    Issued At Claim (iat)
    The iat (issued at) claim identifies the time at which the JWT was issued. 
    This claim can be used to determine the age of the JWT. 
    Its value MUST be a number containing a NumericDate value. 
    Use of this claim is OPTIONAL.

    If the iat claim is not a number, an jwt.InvalidIssuedAtError exception will be raised.
    """
    def generate_jwt_token_iat(self) -> str:
        payload = {"iat": (60 * 7 * 24), "iss": "lcs42"}  # (60 * 7 * 24) = 1week
        return jwt.encode(
            payload=payload,
            key=API_JWT_KEY,
            algorithm=API_JWT_DEFAULT_ALGORITHM
        )

    def decode_jwt_token_iat(self, token: str) -> bool:
        try:
            decode = jwt.decode(
                token,
                key=API_JWT_KEY,
                algorithms=API_JWT_DEFAULT_ALGORITHM,
                # Requiring Presence of Claims
                # If you wish to require one or more claims to be present in the claimset,
                # you can set the require parameter to include these claims.
                options={"require": ["iat", "iss"]}
            )
            print("IAT result:", decode)
        except InvalidIssuedAtError:
            raise InvalidIssuedAtError("Invalid audience")


if __name__ == "__main__":
    ############
    # EXP TEST #
    ############
    token = ExpClaim().generate_jwt_token_exp()
    print(f"token EXP:\n{token}")
    x = None
    sleep(1.1)
    try:
        x = ExpClaim().decode_jwt_token_exp(token=token)
        print("EXP token is valid!")
    except PyJWTError as e:
        print(e)

    ############
    # NBF TEST #
    ############
    token = NbfClaim().generate_jwt_token_nbf()
    print(f"\ntoken NFB:\n{token}")
    x = None
    sleep(.1)
    try:
        x = NbfClaim().decode_jwt_token_nbf(token=token)
        print("NBF token is valid!")
    except PyJWTError as e:
        print(e)

    ############
    # ISS TEST #
    ############
    token = IssClaim().generate_jwt_token_iss()
    print(f"\ntoken ISS:\n{token}")
    x = None
    try:
        x = IssClaim().decode_jwt_token_iss(token=token)
        print("ISS token is valid!")
    except PyJWTError as e:
        print(e)

    ############
    # AUD TEST #
    ############
    token = AudClaim().generate_jwt_token_aud()
    print(f"\ntoken AUD:\n{token}")
    x = None
    try:
        x = AudClaim().decode_jwt_token_aud(token=token)
        print("AUD token is valid!")
    except PyJWTError as e:
        print(e)

    ############
    # IAT TEST #
    ############
    token = IatClaim().generate_jwt_token_iat()
    print(f"\ntoken IAT:\n{token}")
    x = None
    try:
        x = IatClaim().decode_jwt_token_iat(token=token)
        print("IAT token is valid!")
    except PyJWTError as e:
        print(e)
