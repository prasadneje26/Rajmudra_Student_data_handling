import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Database URL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://Synaptix:12345678@localhost:5432/studentdb")
