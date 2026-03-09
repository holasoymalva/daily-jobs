import requests
from .base_scraper import BaseScraper
from typing import List, Dict
import datetime

class GetOnBoardScraper(BaseScraper):
    def fetch_jobs(self) -> List[Dict]:
        jobs = []
        try:
            headers = {"Accept": "application/json"}
            response = requests.get(self.url, headers=headers, timeout=15)
            if response.status_code == 200:
                data = response.json()
                for item in data.get("data", []):
                    attr = item.get("attributes", {})
                    company = item.get("relationships", {}).get("company", {}).get("data", {}).get("id", "Unknown") # The API returns company ID in relationships
                    
                    # Tratar de obtener el nombre de la empresa si está en included o attributes
                    # Por simplicidad, guardamos URL temporal o extraemos el título.
                    title = attr.get("title", "")
                    
                    jobs.append({
                        "title": title,
                        "company": "GetOnBoard Company" if company == "Unknown" else company,
                        "url": item.get("links", {}).get("public_url", f"https://www.getonbrd.com/jobs/{item.get('id', '')}"),
                        "date": datetime.datetime.fromtimestamp(attr.get("published_at", 0)).strftime('%Y-%m-%d') if attr.get("published_at") else "",
                        "description": attr.get("description", ""),
                        "source": self.name
                    })
        except Exception as e:
            print(f"Error fetching from {self.name}: {e}")
        return jobs
