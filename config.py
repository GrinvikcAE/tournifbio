from dotenv import load_dotenv
import os


load_dotenv('.env-dev')

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

JWT_SECRET = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
COOKIE_NAME = os.getenv("COOKIE_NAME")

ADMIN = os.getenv("ADMIN")
PASWD = os.getenv("PASWD")
