from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Paul's Task API - Advanced"
    version: str = "3.0.0"
    secret_key: str = Field("change-me", env="SECRET_KEY")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = Field(60, env="ACCESS_TOKEN_EXPIRE_MINUTES")
    database_url: str = Field("sqlite:///./tasks.db", env="DATABASE_URL")
    cors_origins: str = Field("*", env="CORS_ORIGINS")

    model_config = {
        "env_file": ".env",
        "extra": "ignore",
    }

    def cors_list(self) -> list[str]:
        if not self.cors_origins:
            return ["*"]
        return [
            origin.strip() for origin in self.cors_origins.split(",") if origin.strip()
        ]


settings = Settings()
