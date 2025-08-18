import jwt
from config import settings
from datetime import datetime, timezone, timedelta


def jwt_access_token_generator(user_id: int, count: int = 30):
    
    now = datetime.now(timezone.utc).timestamp()
    
    payload = {
        "type": "access",
        "user_id": user_id,
        "iat": now,
        "exp": now + timedelta(minutes=count)
    }
    
    access_token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=["HS256"])
    return access_token


def jwt_refresh_token_generator(user_id: int, count: int = 1):
    
    now = datetime.now(timezone.utc).timestamp()
    
    payload = {
        "type": "refresh",
        "user_id": user_id,
        "iat": now,
        "exp": now + timedelta(days=count)
    }
    
    refresh_token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=["HS256"])
    return refresh_token