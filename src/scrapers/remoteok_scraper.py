import requests
import datetime
from .base_scraper import BaseScraper
from typing import List, Dict

class RemoteOkScraper(BaseScraper):
    def fetch_jobs(self) -> List[Dict]:
        jobs = []
        try:
            headers = {
                "Accept": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
            response = requests.get(self.url, headers=headers, timeout=15)
            if response.status_code == 200:
                data = response.json()
                
                # RemoteOK sometimes returns a dict with 'legal' as first element if it's a list
                for job in data:
                    if "legal" in job:
                        continue
                        
                    pub_date = job.get("date", "")
                    if pub_date:
                        try:
                            # 2026-02-24T16:00:06+00:00
                            pub_date = pub_date.split('T')[0]
                        except:
                            pass
                            
                    jobs.append({
                        "title": job.get("position", ""),
                        "company": job.get("company", "Unknown"),
                        "url": job.get("url", ""),
                        "date": pub_date,
                        "description": job.get("description", ""),
                        "source": self.name
                    })
        except Exception as e:
            print(f"Error fetching from {self.name}: {e}")
            
        print(f"[{self.name}] Fetched {len(jobs)} jobs (before filtering)")
        return jobs
