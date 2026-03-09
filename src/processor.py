import json
import os

class JobProcessor:
    def __init__(self, config_path: str = "config.json"):
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found: {config_path}")
            
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)
            
        self.keywords = [k.lower() for k in self.config.get("keywords", [])]
        self.categories = {k: [v.lower() for v in vals] for k, vals in self.config.get("categories", {}).items()}
        
    def is_junior(self, job: dict) -> bool:
        """Verifica si la oferta es para perfiles Junior basándose en título y descripción."""
        text = f"{job.get('title', '')} {job.get('description', '')}".lower()
        return any(keyword in text for keyword in self.keywords)
        
    def categorize(self, job: dict) -> str:
        """Clasifica la vacante en una categoría de software."""
        text = f"{job.get('title', '')} {job.get('description', '')}".lower()
        for cat, terms in self.categories.items():
            if any(term in text for term in terms):
                return cat
        return "Other"
        
    def process_jobs(self, jobs: list) -> dict:
        """Filtra y agrupa las vacantes por categoría."""
        categorized = {cat: [] for cat in self.categories.keys()}
        categorized["Other"] = []
        
        seen_urls = set()
        
        for job in jobs:
            if not job.get("url") or job["url"] in seen_urls:
                continue
                
            if self.is_junior(job):
                cat = self.categorize(job)
                # Remueve la descripción para no llenar el README con texto innecesario
                job_clean = {
                    "title": job.get("title"),
                    "company": job.get("company"),
                    "url": job.get("url"),
                    "date": job.get("date"),
                    "source": job.get("source")
                }
                categorized[cat].append(job_clean)
                seen_urls.add(job["url"])
                
        # Remueve categorías vacías
        return {k: v for k, v in categorized.items() if len(v) > 0}
