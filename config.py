from pydantic_settings import BaseSettings , SettingsConfigDict

class Settings(BaseSettings):
    
    OPENAI_API_KEY: str
    
    MODEL_NAME: str = "gpt-4o"
    EMBEDDING_MODEL_NAME: str = "text-embedding-3-small"
    
    COLLECTION_NAME: str = "enterprise_docs"
    
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8",extra="ignore")
    
settings = Settings()

