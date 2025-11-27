from pydantic import BaseModel, Field


####
class UserCreate(BaseModel):
    username: str = Field(...,min_length=3)
    password: str = Field(...,min_length=6)

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# Schéma pour la requête de traduction
# ... (Gardez les schémas UserCreate, UserLogin, Token existants)

# Schéma pour la requête de traduction
class TranslationRequest(BaseModel):
    text: str = Field(..., min_length=1)
    # Direction de traduction : 'fr-en' ou 'en-fr'
    direction: str = Field(..., pattern=r'^(fr-to-en|en-to-fr)$')

