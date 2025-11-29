from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import engine, Base, get_db
from app.models.user import User
from app.schemas.schemas import UserCreate, Token,TranslationRequest
from app.crud.crud import get_user_by_username, create_user
from app.auth.auth import verify_password, create_access_token, get_current_user, get_password_hash
from datetime import timedelta
import os
import httpx 
from app.translate_script import translate_text
# Durée d'expiration du token en minutes
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

# Création des tables dans la BDD au démarrage
Base.metadata.create_all(bind=engine)

app = FastAPI()
# Allow Swagger (or any front-end) to call your API
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://172.18.80.1:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





@app.post("/register", response_model=Token)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = create_user(db, user)

    access_token = create_access_token({"sub": new_user.username})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@app.post("/login")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_username(db, username=form_data.username)
    
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401,detail="Incorrect username or password")

    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=timedelta(minutes=30)
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post('/translate')
async def translate(request: TranslationRequest, token: str = Depends(get_current_user)):
    raw_response = await translate_text(request.text, request.direction)

    # Vérifier les différentes clés possibles
    if isinstance(raw_response, list) and len(raw_response) > 0:
        first_item = raw_response[0]
        translated_text = first_item.get('generated_text') or first_item.get('translation_text') or str(first_item)
    else:
        translated_text = str(raw_response)

    return {"translated_text": translated_text}
