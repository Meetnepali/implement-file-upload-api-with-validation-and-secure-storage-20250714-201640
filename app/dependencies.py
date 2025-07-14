from fastapi import Header, HTTPException, Depends, status
from app.logger import get_audit_logger

def get_current_user(authorization: str = Header(...)):
    # Simulated authentication; accept 'Bearer testtoken' as valid
    if authorization != "Bearer testtoken":
        raise HTTPException(status_code=401, detail="Unauthorized. Invalid token.")
    return {"id": "user123", "username": "demo_user"}

def get_logger():
    return get_audit_logger()
