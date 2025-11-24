from fastapi import FastAPI, Depends,HTTPException,status
from database import Base,engine,get_db
from models import User
from schemas import UserCreate, Token
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from auth import verify_password, create_access_token
from crud import get_user_by_username, create_user
from datetime import timedelta
Base.metadata.create_all(bind=engine)

app = FastAPI()

#  Endpoint POST /register 


#  Endpoint POST /login 
@app.post("/login",response_model=Token)
def login_access_token(form_data: OAuth2PasswordRequestForm = Depends(), #recupere username et password 
                       db:Session = Depends(get_db)):
    user = get_user_by_username(db, username=form_data.username) #recupere user par username et chercher dans la base de donnee un user qui a ce nom/Si l’utilisateur n’existe pas → erreur.
    if not user or not verify_password(form_data.password, user.password_hash): #verifier le password/On compare : Le mot de passe tapé par l’utilisateur et Le hash stocké dans la base
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        ) 
    access_token = create_access_token(
        {"sub": user.username}, expires_delta=timedelta(minutes=30) # sub = identifiant du user dans le token.
    )# creer un token d’acces
    return {"access_token": access_token, "token_type": "bearer"} # Retourner le token