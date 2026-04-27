# 🚀 Scraper de Vacantes Junior Auto-Actualizable

Este repositorio es un **bot automatizado** construido con Python y GitHub Actions que, todos los días, extrae vacantes de programación enfocadas en perfiles Junior/Trainee y actualiza este README con los resultados en vivo.

¡Ideal para desarrolladores que buscan su primera oportunidad laboral!

## 🔧 ¿Cómo funciona?
1. Un workflow en GitHub Actions corre todos los días de forma automática.
2. Un script de Python (`src/main.py`) solicita datos a portales de empleo (Ej: GetOnBoard).
3. Se filtran las ofertas mediante palabras clave predefinidas (`Junior`, `Trainee`, `Sin experiencia`, etc.) usando `config.json`.
4. Se agrupan en categorías tecnológicas populares (Frontend, Backend, Móvil, Data, QA).
5. El bot sobreescribe y formatea el resultado en este `README.md` y hace un `git push` automático.

---

## 💼 Ofertas de Empleo (Actualizadas Diariamente)

<!-- JOBS_START -->
### 📊 Análisis del Mercado (Top 5)

| 🏆 Vacantes más Demandadas | 💻 Tecnologías más Demandadas |
|:---|:---|
| Junior Artist Manager / Influencer Manager (m/w/d) (2) | Frontend (1) |
| Trainee Artist Manager / Influencer Manager (m/w/d) (2) | Data (1) |
| Software Engineer (1) | Data analyst (1) |
| Senior App &amp; Frontend Developer AS233 (1) | - |
| Senior Product Manager Applied AI (1) | - |

### Frontend

- **[Software Engineer](https://remoteOK.com/remote-jobs/remote-software-engineer-finalis-1131328)** en Finalis _(2026-04-26)_ - RemoteOK
- **[Senior App &amp; Frontend Developer AS233](https://remoteOK.com/remote-jobs/remote-senior-app-amp-frontend-developer-as233-smart-working-solutions-1131268)** en Smart Working Solutions _(2026-04-22)_ - RemoteOK
- **[Senior Product Manager Applied AI](https://remoteOK.com/remote-jobs/remote-senior-product-manager-applied-ai-smartsheet-1131233)** en Smartsheet _(2026-04-21)_ - RemoteOK

### Backend

- **[AI Engineer](https://remotive.com/remote-jobs/ai-ml/ai-engineer-2089958)** en Dry Ground AI _(2026-04-21)_ - Remotive
- **[OCM Lead ( Change Management) - German Speaking](https://www.arbeitnow.com/jobs/companies/kryptos-technologies-limited/ocm-lead-change-management-german-speaking-frankfurt-am-main-481432)** en Kryptos Technologies limited _(2026-04-27)_ - Arbeitnow
- **[IT-Systemadministrator (m/w/d)](https://www.arbeitnow.com/jobs/companies/24industries/it-systemadministrator-munich-439982)** en 24Industries _(2026-04-27)_ - Arbeitnow
- **[Data Analyst](https://remoteOK.com/remote-jobs/remote-data-analyst-criptoro-1131219)** en Criptoro _(2026-04-19)_ - RemoteOK

### Mobile

- **[Junior Recruiter (m/w/d) Bankwesen](https://www.arbeitnow.com/jobs/companies/matchworks/junior-recruiter-bankwesen-hamburg-111600)** en MatchWorks _(2026-04-26)_ - Arbeitnow

### Other

- **[Teamleitung Buchhaltung | Wachstumsphase](https://www.arbeitnow.com/jobs/companies/matera-gmbh/teamleitung-buchhaltung-wachstumsphase-berlin-19466)** en Matera GmbH _(2026-04-27)_ - Arbeitnow
- **[Team Lead Accounting | Scaling Phase](https://www.arbeitnow.com/jobs/companies/matera-gmbh/team-lead-accounting-scaling-phase-berlin-259456)** en Matera GmbH _(2026-04-27)_ - Arbeitnow
- **[Finance Associate - Remote (m/w/d)](https://www.arbeitnow.com/jobs/companies/finton-advisors-by-efpinai-gmbh/finance-associate-remote-nottensdorf-385549)** en Finton Advisors by EFPINAI GmbH _(2026-04-27)_ - Arbeitnow
- **[Finance Associate (m/w/d)](https://www.arbeitnow.com/jobs/companies/finton-advisors-by-efpinai-gmbh/finance-associate-cologne-279021)** en Finton Advisors by EFPINAI GmbH _(2026-04-27)_ - Arbeitnow
- **[Junior Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/junior-artist-manager-influencer-manager-berlin-387114)** en Lionflence _(2026-04-27)_ - Arbeitnow
- **[Trainee Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/trainee-artist-manager-influencer-manager-berlin-282211)** en Lionflence _(2026-04-27)_ - Arbeitnow
- **[Junior Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/junior-artist-manager-influencer-manager-mulheim-311876)** en Lionflence _(2026-04-27)_ - Arbeitnow
- **[Trainee Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/trainee-artist-manager-influencer-manager-mulheim-10046)** en Lionflence _(2026-04-27)_ - Arbeitnow

<!-- JOBS_END -->

---

## 🛠️ Stack Tecnológico
- Python 3 (`requests`, `beautifulsoup4`)
- GitHub Actions Automation Pipeline 
- Configuraciones parametrizadas vía JSON

## 🤝 Contribuir
Si conoces otras APIs abiertas para empleo Tech Junior, añade una fuente a `config.json` y su correspondiente mapeador a la carpeta `src/scrapers/`. 
_Hecho para la comunidad de Jr Devs._