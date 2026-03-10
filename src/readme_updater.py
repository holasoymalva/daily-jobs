import os
from typing import Optional

def update_readme(jobs_grouped: dict, top_vacancies: Optional[list] = None, top_techs: Optional[list] = None, readme_path: str = "README.md"):
    """
    Lee el README.md, encuentra los marcadores y reemplaza el contenido entre ellos.
    """
    start_marker = "<!-- JOBS_START -->"
    end_marker = "<!-- JOBS_END -->"
    
    # Genera el markdown del banner
    banner_md = ""
    if top_vacancies and top_techs:
        banner_md += "### 📊 Análisis del Mercado (Top 5)\n\n"
        banner_md += "| 🏆 Vacantes más Demandadas | 💻 Tecnologías más Demandadas |\n"
        banner_md += "|:---|:---|\n"
        
        max_rows = max(min(len(top_vacancies), 5), min(len(top_techs), 5))
        for i in range(max_rows):
            vac_str = f"{top_vacancies[i][0]} ({top_vacancies[i][1]})" if i < len(top_vacancies) else "-"
            # Capitalizar el nombre de la tecnología y mostrar su conteo
            tech_str = f"{top_techs[i][0].capitalize()} ({top_techs[i][1]})" if i < len(top_techs) else "-"
            banner_md += f"| {vac_str} | {tech_str} |\n"
        banner_md += "\n"
    
    # Genera el markdown de las vacantes
    md_content = "\n" + banner_md
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
