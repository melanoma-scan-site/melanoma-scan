from __future__ import annotations
from dataclasses import dataclass


@dataclass
class MelanomaStatus:
    percent: int
    is_melanoma: bool
    
    @staticmethod
    def get_from_float(percent: float) -> MelanomaStatus:
        is_melanoma = True if percent > 0.0 else False
        return MelanomaStatus(percent=int(percent * 100), is_melanoma=is_melanoma)