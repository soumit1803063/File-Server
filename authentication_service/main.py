from fastapi import FastAPI
# main.py

from .routes.auth_routes import router as auth_router


app = FastAPI()


# Include authentication routes
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

@app.get("/")
def home():
    return {"message": "Welcome to the Authentication Service"}
