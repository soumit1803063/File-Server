from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr


router = APIRouter()

class UserRegisterRequest(BaseModel):
    email: EmailStr
    password: str

class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str

@router.post("/register")
async def register(user: UserRegisterRequest):
    return {"message": f"User registered successfully with {user.email} and {user.password}"}

@router.post("/login")
async def login(user: UserLoginRequest):
    return {"message": f"User login successfully with {user.email} and {user.password}"}
