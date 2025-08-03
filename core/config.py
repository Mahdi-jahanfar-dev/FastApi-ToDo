from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    test : str
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        
settings = Settings()