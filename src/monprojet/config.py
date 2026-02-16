from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    env: str = "dev"
    log_level: str = "INFO"


settings = Settings()
