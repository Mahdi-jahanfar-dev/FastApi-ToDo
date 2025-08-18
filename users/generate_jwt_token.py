import jwt
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError, DecodeError
from config import settings
from datetime import datetime, timezone, timedelta
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.exceptions import HTTPException
from fastapi import Depends, status

security = HTTPBearer()


def jwt_access_token_generator(user_id: int, count: int = 30):
    
    now = datetime.now(timezone.utc)
    
    payload = {
        "type": "access",
        "user_id": user_id,
        "iat": now,
        "exp": now + timedelta(minutes=count)
    }
    
    access_token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm="HS256")
    return access_token


def jwt_refresh_token_generator(user_id: int, count: int = 1):
    
    now = datetime.now(timezone.utc)
    
    payload = {
        "type": "refresh",
        "user_id": user_id,
        "iat": now,
        "exp": now + timedelta(days=count)
    }
    
    refresh_token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm="HS256")
    return refresh_token

def get_authenticated_user(credential: HTTPAuthorizationCredentials = Depends(security)):
    
    token = credential.credentials
    
    try:
        decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
        return decoded_token
    except InvalidTokenError:
        raise HTTPException(detail="invalid token", status_code=status.HTTP_401_UNAUTHORIZED)
    except ExpiredSignatureError:
        raise HTTPException(detail="token is expired", status_code=status.HTTP_401_UNAUTHORIZED)
    except DecodeError:
        raise HTTPException(detail="authentication faild", status_code=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        raise HTTPException(detail=f"error: {e}", status_code=status.HTTP_401_UNAUTHORIZED)
