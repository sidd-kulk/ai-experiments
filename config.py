import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
API_KEY = os.getenv("API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_TOKEN = os.getenv("SECRET_TOKEN")

# You can provide default values if the environment variable is not set
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
