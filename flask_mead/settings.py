import os
from pathlib import Path

from dotenv import load_dotenv

dot_env_path = f"{Path.cwd()}/.env"
dot_env_file_exists = Path(dot_env_path).exists()

if not dot_env_file_exists:
    raise OSError(
        ".env file does not exists, please create it."
        "A full example is available in the file dot.env.example"
    )
else:
    load_dotenv(dot_env_path)

user = os.getenv("DB_USER")
pwd = os.getenv("DB_USER_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
name = os.getenv("DB_NAME")
DATABASE_URI = f"postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{name}"


class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY")
    ENV = os.getenv("ENV")
    DATABASE_NAME = os.getenv("DB_NAME", "test")
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    POSTS_PER_PAGE = os.getenv("POSTS_PER_PAGE", 10)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = f"{Path.cwd()}/uploads"


class DevConfig(BaseConfig):
    DEBUG = True
    TESTING = True


class LiveConfig(BaseConfig):
    DEBUG = False
    TESTINNG = False


config = {
    "development": DevConfig,
    "production": LiveConfig,
}
