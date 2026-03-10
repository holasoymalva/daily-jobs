import requests
import datetime
from .base_scraper import BaseScraper
from typing import List, Dict

class RemotiveScraper(BaseScraper):
    def fetch_jobs(self) -> List[Dict]:
        jobs = []
        try:
            headers = {"Accept": "application/json"}
            response = requests.get(self.url, headers=headers, timeout=15)
            if response.status_code == 200:
                data = response.json()
                for job in data.get("jobs", []):
                    
                    pub_date = job.get("publication_date", "")
                    if pub_date:
                        try:
                            # Remotive date format: '2026-03-02T20:01:28'
                            pub_date = pub_date.split('T')[0]
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
