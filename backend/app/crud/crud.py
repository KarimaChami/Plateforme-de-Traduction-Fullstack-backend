

from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.schemas import UserCreate
from app.auth.auth import get_password_hash


# def get_user_by_username():
#     return None

# def create_user():
#     return None

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate):
    db_user = get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, password_hash=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

