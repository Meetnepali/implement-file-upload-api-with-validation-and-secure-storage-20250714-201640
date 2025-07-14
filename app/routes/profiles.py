from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status, BackgroundTasks, Request
from fastapi.responses import JSONResponse
from typing import Optional
from app.schemas import UserProfileUpdate, UserProfileResponse, ErrorResponse
from app.dependencies import get_current_user, get_logger
from app.utils import save_image, generate_thumbnail
from app.logger import get_audit_logger
from pathlib import Path
import shutil

router = APIRouter()

@router.post("/me/profile", response_model=UserProfileResponse, responses={
    400: {"model": ErrorResponse},
    401: {"model": ErrorResponse},
    422: {"model": ErrorResponse}
})
async def update_profile(
    request: Request,
    profile: UserProfileUpdate = Depends(),
    avatar: Optional[UploadFile] = File(None),
    background_tasks: BackgroundTasks = Depends(),
    current_user: dict = Depends(get_current_user),
    logger=Depends(get_logger)
):
    user_id = str(current_user["id"])
    response_data = {"username": profile.username, "bio": profile.bio, "avatar_url": None}
    
    if avatar:
        try:
            image_path = save_image(avatar, user_id)
            background_tasks.add_task(generate_thumbnail, image_path)
            response_data["avatar_url"] = f"/media/{user_id}/{avatar.filename}"
        except HTTPException as exc:
            logger.info({"event":"failed_upload","user":user_id,"error":exc.detail})
            raise exc
        except Exception as exc:
            logger.error({"event":"failed_upload","user":user_id,"error":str(exc)})
            raise HTTPException(status_code=500, detail="Failed to upload avatar.")
    logger.info({"event":"profile_update","user":user_id,"fields":response_data})
    return UserProfileResponse(**response_data)
