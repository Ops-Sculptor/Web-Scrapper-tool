from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class VisitingCard:
    name: str = ""
    company: str = ""
    position: str = ""
    email: str = ""
    phone: str = ""
    website: str = ""
    address: str = ""
    city: str = ""
    state: str = ""
    country: str = ""
    category: str = ""
    tags: List[str] = None
    source_url: str = ""
    scraped_at: str = ""

    def __post_init__(self):
        if self.tags is None:
            self.tags = []
        if not self.scraped_at:
            self.scraped_at = datetime.now().isoformat()
