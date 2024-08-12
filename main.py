from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import or_
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session


from models import User, Data
from auth import hash_password, get_current_user, login_user
from db import get_db
from schemas import UserCreate, UserSignIn, DeliveryGuy

from fastapi.security import OAuth2PasswordRequestForm
from auth import authenticate_user, create_access_token

app = FastAPI()

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/users/signup", response_model=None)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        existing_user = db.query(User).filter(
            or_(User.username == user.username, User.email == user.email)
        ).first()
        if existing_user:
            raise HTTPException(
                status_code=400, detail="Username or email already registered")
        hashed_password = hash_password(user.password)
        user.password = hashed_password
        db_user = User(**user.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return {"message": f"User created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/users/login", response_model=None)
def check_user(user: UserSignIn, db: Session = Depends(get_db)):
    try:
        return login_user(db, user.username, user.password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/delivery/", response_model=None)
def delivery_guy(user: DeliveryGuy, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    current_user = get_current_user(db, token)
    # user.id = current_user.id
    data = Data(**user.model_dump())
    db.add(data)
    db.commit()
    db.refresh(data)
    return {"message": "Delivery guy added successfully"}


@app.post("/market/", response_model=None)
def market_people(user: UserCreate, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post("/token", response_model=None)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
