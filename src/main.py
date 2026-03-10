import sys
import os
import json

# Directorio base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from src.scrapers.getonboard_scraper import GetOnBoardScraper
from src.scrapers.remotive_scraper import RemotiveScraper
from src.scrapers.arbeitnow_scraper import ArbeitnowScraper
from src.scrapers.remoteok_scraper import RemoteOkScraper
from src.processor import JobProcessor
from src.readme_updater import update_readme

def main():
    print("🚀 Iniciando scraper de vacantes...")
    
    config_path = os.path.join(BASE_DIR, "config.json")
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
        
    all_jobs = []
    
    # 1. Scraping iterando sobre las fuentes de configuración
    for source in config.get("sources", []):
        name = source.get("name")
        url = source.get("api_url")
        
        print(f"Obteniendo datos de {name}...")
        scraper = None
        if name == "GetOnBoard":
            scraper = GetOnBoardScraper(name=name, url=url)
        elif name == "Remotive":
            scraper = RemotiveScraper(name=name, url=url)
        elif name == "Arbeitnow":
            scraper = ArbeitnowScraper(name=name, url=url)
        elif name == "RemoteOK":
            scraper = RemoteOkScraper(name=name, url=url)
            
        if scraper:
            jobs = scraper.fetch_jobs()
            all_jobs.extend(jobs)
        
    print(f"Total de vacantes obtenidas en crudo: {len(all_jobs)}")
    
    # 2. Procesamiento, Filtrado (Junior) y Categorización
    processor = JobProcessor(config_path=config_path)
    grouped_jobs = processor.process_jobs(all_jobs)
    
    total_valid = sum(len(v) for v in grouped_jobs.values())
    print(f"Total de vacantes categorizadas válidas (Junior): {total_valid}")
    
    # 3. Actualización del README
    readme_path = os.path.join(BASE_DIR, "README.md")
    update_readme(grouped_jobs, readme_path=readme_path)
    print("✅ README.md actualizado con éxito.")

if __name__ == "__main__":
    main()
