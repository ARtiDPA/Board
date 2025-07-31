"""Token's operations."""
import jwt
from datetime import datetime, timedelta
from typing import Optional
import os

SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'fallback-secret-key')
ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS256')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRE_MINUTES', '30'))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv('JWT_REFRESH_TOKEN_EXPIRE_DAYS', '7'))

def create_access_token(user_id: int, role: str) -> str:
    """_summary_
    Creating access token
    Args:
        user_id (int): user id from table
        role (str): user role from table

    Returns:
        str: access token
    """    
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        'user_id':user_id,
        'role':role,
        'type':'access',
        'exp':expire
    }
    return jwt.encode(payload, SECRET_KEY, algorithm = ALGORITHM)

def create_refresh_token(user_id: int, role: str)->str:
    """_summary_
    Creating refresh token
    Args:
        user_id (int): user id from table
        role (str): user role from table

    Returns:
        str: refresh token
    """    
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    payload = {
        'user_id':user_id,
        'role':role,
        'type':'refresh',
        'exp':expire
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token:str)->Optional[dict]:
    """_summary_
    Validate and verify token
    Args:
        token (str): some token

    Returns:
        Optional[dict]: token or None
    """    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

