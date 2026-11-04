import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "change-me-in-production")
    APPWRITE_ENDPOINT = os.getenv(
        "APPWRITE_ENDPOINT", "https://cloud.appwrite.io/v1"
    )
    APPWRITE_PROJECT_ID = os.getenv("APPWRITE_PROJECT_ID")
    APPWRITE_API_KEY = os.getenv("APPWRITE_API_KEY")
    APPWRITE_DATABASE_ID = os.getenv("APPWRITE_DATABASE_ID", "stuntfree_db")
