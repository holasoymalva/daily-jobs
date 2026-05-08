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
| Junior Artist Manager / Influencer Manager (m/w/d) (2) | Typescript (1) |
| Trainee Artist Manager / Influencer Manager (m/w/d) (2) | Data (1) |
| Sidebase Open-Source Contributor & Senior TS Dev (f/m/d) (1) | Data analyst (1) |
| Senior Typescript Developer (f/m/d) (1) | - |
| Senior Full-Stack Engineer (w/m/d) (1) | - |

### Frontend

- **[Sidebase Open-Source Contributor & Senior TS Dev (f/m/d)](https://www.arbeitnow.com/jobs/companies/sidestream/sidebase-open-source-contributor-senior-ts-dev-cologne-317648)** en Sidestream _(2026-05-08)_ - Arbeitnow
- **[Senior Typescript Developer (f/m/d)](https://www.arbeitnow.com/jobs/companies/sidestream/senior-typescript-developer-cologne-220463)** en Sidestream _(2026-05-08)_ - Arbeitnow
- **[Senior Full-Stack Engineer (w/m/d)](https://www.arbeitnow.com/jobs/companies/skalar/senior-full-stack-engineer-munich-194800)** en Skalar _(2026-05-07)_ - Arbeitnow
- **[Junior Mid Full Stack Software Engineer](https://remoteOK.com/remote-jobs/remote-junior-mid-full-stack-software-engineer-black-canyon-consulting-1131437)** en Black Canyon Consulting _(2026-05-03)_ - RemoteOK

### Backend

- **[AI Engineer](https://remotive.com/remote-jobs/artificial-intelligence/ai-engineer-2089958)** en Dry Ground AI _(2026-04-21)_ - Remotive
- **[Inside Sales Contractor](https://remotive.com/remote-jobs/sales/inside-sales-contractor-2086540)** en Credit Wellness, LLC _(2026-04-13)_ - Remotive
- **[Production Engineer – UAV Platform](https://www.arbeitnow.com/jobs/companies/24industries/production-engineer-uav-platform-munich-51663)** en 24Industries _(2026-05-07)_ - Arbeitnow
- **[IT & Security Manager](https://www.arbeitnow.com/jobs/companies/24industries/it-security-manager-munich-376913)** en 24Industries _(2026-05-07)_ - Arbeitnow
- **[UI Developer](https://remoteOK.com/remote-jobs/remote-ui-developer-rainfocus-1131473)** en RainFocus _(2026-05-05)_ - RemoteOK
- **[Legal Data Analyst Junior Vaga Afirmativa para PCD](https://remoteOK.com/remote-jobs/remote-legal-data-analyst-junior-vaga-afirmativa-para-pcd-jusbrasil-1131393)** en Jusbrasil _(2026-04-30)_ - RemoteOK

### Data

- **[Entry Level Crypto Market Specialist](https://remoteOK.com/remote-jobs/remote-entry-level-crypto-market-specialist-infiniti-group-1131416)** en Infiniti Group _(2026-05-01)_ - RemoteOK

### Other

- **[Junior Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/junior-artist-manager-influencer-manager-berlin-266822)** en Lionflence _(2026-05-08)_ - Arbeitnow
- **[Trainee Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/trainee-artist-manager-influencer-manager-berlin-305974)** en Lionflence _(2026-05-08)_ - Arbeitnow
- **[Trainee Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/trainee-artist-manager-influencer-manager-mulheim-78666)** en Lionflence _(2026-05-08)_ - Arbeitnow
- **[Junior Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/junior-artist-manager-influencer-manager-mulheim-374150)** en Lionflence _(2026-05-08)_ - Arbeitnow
- **[Trainee Management (m/w/d)](https://www.arbeitnow.com/jobs/companies/coolback-gmbh/trainee-management-nuthe-urstromtal-450010)** en coolback GmbH _(2026-05-08)_ - Arbeitnow
- **[Werkstudent (m/w/d) – Finance & Beratung (unternehmerisch, leistungsbasiert)](https://www.arbeitnow.com/jobs/companies/kevin-kehr/werkstudent-finance-beratung-unternehmerisch-leistungsbasiert-hamburg-3651)** en Kevin Kehr _(2026-05-08)_ - Arbeitnow
- **[Water Engineeer Trainee - Field Based Projects (Somaliland) No. 2603](https://www.arbeitnow.com/jobs/companies/ces-consulting-engineers-salzgitter-gmbh/water-engineeer-trainee-field-based-projects-somaliland-no-2603-braunschweig-102264)** en CES Consulting Engineers Salzgitter GmbH _(2026-05-08)_ - Arbeitnow
- **[Customer Service Representative Hotel Reservations Entry Level](https://remoteOK.com/remote-jobs/remote-customer-service-representative-hotel-reservations-entry-level-aisles-amp-abroad-1131496)** en Aisles &amp; Abroad _(2026-05-07)_ - RemoteOK

<!-- JOBS_END -->

---

## 🛠️ Stack Tecnológico
- Python 3 (`requests`, `beautifulsoup4`)
- GitHub Actions Automation Pipeline 
- Configuraciones parametrizadas vía JSON

## 🤝 Contribuir
Si conoces otras APIs abiertas para empleo Tech Junior, añade una fuente a `config.json` y su correspondiente mapeador a la carpeta `src/scrapers/`. 
_Hecho para la comunidad de Jr Devs._