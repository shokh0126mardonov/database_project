import os
from dotenv import load_dotenv

load_dotenv()


HOST = os.getenv("DB_HOST")
USER = os.getenv("DB_USER")
NAME = os.getenv("DB_NAME")
PASSWORD = os.getenv("DB_PASSWORD")
PORT = os.getenv("DB_PORT")