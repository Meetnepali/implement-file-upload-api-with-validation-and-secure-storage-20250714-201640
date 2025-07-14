from fastapi import FastAPI
from app.routes import profiles

app = FastAPI(title="User Profile API with File Upload", description="API for uploading and updating user profile information and avatar images.")

app.include_router(profiles.router, prefix="/users", tags=["Profiles"])
