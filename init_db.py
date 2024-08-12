from db import engine, Base
from models import User, Data

# Create all tables
Base.metadata.create_all(bind=engine)

print("Database tables created successfully.")
