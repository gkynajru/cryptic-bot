from pydantic import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    ZENDESK_BASE_URL: str = "https://support.optisigns.com"
    OUTPUT_DIR: str = "data/md"
    STATE_FILE: str = "data/state.json"
    VECTOR_STORE_NAME: str = "optibot-support-docs"

    class Config:
        env_file = ".env"

settings = Settings()