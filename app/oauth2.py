from jose import JWTError, jwt
from datetime import datetime, timedelta

# openssl rand -hex 32
SECRET_KEY = "38b96b95d4830f3013542e0245c6aa37873794027022b0e3e878b5a6fd296dff"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt




