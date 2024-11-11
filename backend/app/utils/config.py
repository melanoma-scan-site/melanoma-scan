from __future__ import annotations

from dataclasses import dataclass
from os import getenv


@dataclass(frozen=True)
class Config:
    TF_MODEL_PATH: str
    
    @staticmethod
    def get_config() -> Config:
        TF_MODEL_PATH = getenv("TF_MODEL_PATH", "")
        
        if TF_MODEL_PATH == "":
            raise ValueError("TF_MODEL_PATH is not set")
        
        return Config(TF_MODEL_PATH)
    
CONFIG = Config.get_config()