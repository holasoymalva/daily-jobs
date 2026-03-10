import requests
import datetime
from .base_scraper import BaseScraper
from typing import List, Dict

class ArbeitnowScraper(BaseScraper):
    def fetch_jobs(self) -> List[Dict]:
        jobs = []
        try:
            headers = {"Accept": "application/json"}
            response = requests.get(self.url, headers=headers, timeout=15)
            if response.status_code == 200:
                data = response.json()
                for job in data.get("data", []):
                    
                    created_at = job.get("created_at", 0)
                    pub_date = ""
                    if created_at:
                        try:
                            # Arbeitnow uses Unix timestamp
                            pub_date = datetime.datetime.fromtimestamp(created_at).strftime('%Y-%m-%d')
                        except:
                            pass
                            
                    jobs.append({
                        "title": job.get("title", ""),
                        "company": job.get("company_name", "Unknown"),
                        "url": job.get("url", ""),
                        "date": pub_date,
                        "description": job.get("description", ""),
                        "source": self.name
                    })
        except Exception as e:
            print(f"Error fetching from {self.name}: {e}")
            
        print(f"[{self.name}] Fetched {len(jobs)} jobs (before filtering)")
        return jobs
