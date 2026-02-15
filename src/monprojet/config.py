from dataclasses import dataclass

@dataclass(frozen=True)
class AppConfig:
    log_level: str = "INFO"
