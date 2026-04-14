from pydantic_settings import BaseSettings, SettingsConfigDict


# BaseSettings: os.environ から自動で値を読む
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    database_url: str  # DATABASE_URLが自動代入
    cors_origins: str = ""


# モジュールインポート時に1回インスタンス化
settings = Settings()  # type: ignore[call-arg]
