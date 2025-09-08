from pydantic_settings import BaseSettings


# env settings for project
class Settings(BaseSettings):
    TESTS_DATABASE_URL: str
    JWT_SECRET_KEY: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: str
    AI_SECRET_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# project settings instance
settings = Settings()
