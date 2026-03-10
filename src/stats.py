import json
import os
from collections import Counter
from datetime import datetime

def generate_and_save_stats(grouped_jobs, config_path, base_dir):
    # Load config for tech keywords
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
        
    tech_keywords = []
    for terms in config.get("categories", {}).values():
        tech_keywords.extend([t.lower() for t in terms])
        
    all_valid_jobs = []
    for jobs in grouped_jobs.values():
        all_valid_jobs.extend(jobs)
        
    # Vacantes mas demandadas
    title_counts = Counter(job["title"] for job in all_valid_jobs)
    top_vacancies = title_counts.most_common(10)
    
    # Tecnologias mas demandadas
    tech_counts = Counter()
    for job in all_valid_jobs:
        title_lower = job["title"].lower()
        found_techs = set()
        for tech in tech_keywords:
            # We look for tech as an exact word or part of it, since 'c#' and 'go' are short,
            # we should be careful. To keep it simple, just exact match in string.
            # A better approach is matching word boundaries for short words.
            if len(tech) <= 2:
                # Basic check for exact word for short ones like 'go', 'c#', 'qa'
                words = title_lower.split()
                if tech in words:
                    found_techs.add(tech)
            else:
                if tech in title_lower:
                    found_techs.add(tech)
                    
        for tech in found_techs:
            tech_counts[tech] += 1
            
    top_techs = tech_counts.most_common(10)
    
    # Save to JSON history
    stats_data = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "total_jobs": len(all_valid_jobs),
        "top_vacancies": [{"title": t[0], "count": t[1]} for t in top_vacancies],
        "top_technologies": [{"tech": t[0], "count": t[1]} for t in top_techs]
    }
    
    # Create data directory if it doesn't exist
    data_dir = os.path.join(base_dir, "data")
    os.makedirs(data_dir, exist_ok=True)
    stats_file = os.path.join(data_dir, "daily_stats.json")
    
    history = []
    if os.path.exists(stats_file):
        try:
            with open(stats_file, "r", encoding="utf-8") as f:
                history = json.load(f)
        except:
            history = []
            
    history.append(stats_data)
    
    with open(stats_file, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)
        
    return top_vacancies, top_techs
