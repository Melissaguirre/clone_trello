import pydantic from BaseSettings

class Settings(BaseSettings):
    DB_URL: str


settings: Settings = Settings()
