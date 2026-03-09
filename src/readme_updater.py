import os

def update_readme(jobs_grouped: dict, readme_path: str = "README.md"):
    """
    Lee el README.md, encuentra los marcadores y reemplaza el contenido entre ellos.
    """
    start_marker = "<!-- JOBS_START -->"
    end_marker = "<!-- JOBS_END -->"
    
    # Genera el markdown
    md_content = "\n"
    if not jobs_grouped:
        md_content += "_No se encontraron vacantes junior nuevas hoy._\n\n"
    else:
        for category, jobs in jobs_grouped.items():
            md_content += f"### {category}\n\n"
            for job in jobs:
                md_content += f"- **[{job['title']}]({job['url']})** en {job['company']} _({job['date']})_ - {job['source']}\n"
            md_content += "\n"
            
    # Lee o crea el README.md
    if not os.path.exists(readme_path):
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(f"# Vacantes Junior\n\n{start_marker}\n{md_content}{end_marker}\n")
        return
        
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    if start_marker in content and end_marker in content:
        before = content.split(start_marker)[0]
        after = content.split(end_marker)[1]
        new_content = f"{before}{start_marker}{md_content}{end_marker}{after}"
    else:
        # Si no tiene los marcadores, los agrega al final
        new_content = f"{content}\n\n{start_marker}{md_content}{end_marker}\n"
        
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)
