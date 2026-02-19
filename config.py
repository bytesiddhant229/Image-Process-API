import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "media/uploads")
    OUTPUT_FOLDER = os.path.join(BASE_DIR, "media/output")

    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  
