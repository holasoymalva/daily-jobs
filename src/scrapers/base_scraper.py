from abc import ABC, abstractmethod
from typing import List, Dict

class BaseScraper(ABC):
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url
    
    @abstractmethod
    def fetch_jobs(self) -> List[Dict]:
        """
        Debe retornar una lista de diccionarios con las llaves:
        title, company, url, date, description, source
        """
        pass
