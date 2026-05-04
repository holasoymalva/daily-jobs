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
| Junior Artist Manager / Influencer Manager (m/w/d) (2) | Data (1) |
| Trainee Artist Manager / Influencer Manager (m/w/d) (2) | Data analyst (1) |
| Junior Mid Full Stack Software Engineer (1) | - |
| Engineer Software (1) | - |
| Software Engineer (1) | - |

### Frontend

- **[Junior Mid Full Stack Software Engineer](https://remoteOK.com/remote-jobs/remote-junior-mid-full-stack-software-engineer-black-canyon-consulting-1131437)** en Black Canyon Consulting _(2026-05-03)_ - RemoteOK
- **[Engineer Software](https://remoteOK.com/remote-jobs/remote-engineer-software-calabrio-1131345)** en Calabrio _(2026-04-27)_ - RemoteOK
- **[Software Engineer](https://remoteOK.com/remote-jobs/remote-software-engineer-finalis-1131328)** en Finalis _(2026-04-26)_ - RemoteOK

### Backend

- **[AI Engineer](https://remotive.com/remote-jobs/artificial-intelligence/ai-engineer-2089958)** en Dry Ground AI _(2026-04-21)_ - Remotive
- **[Inside Sales Contractor](https://remotive.com/remote-jobs/sales/inside-sales-contractor-2086540)** en Credit Wellness, LLC _(2026-04-13)_ - Remotive
- **[Baufinanzierungsberater / Bankkaufmann (m/w/d)](https://www.arbeitnow.com/jobs/companies/justhome-gmbh/baufinanzierungsberater-bankkaufmann-berlin-307462)** en Justhome GmbH _(2026-05-03)_ - Arbeitnow
- **[E-Commerce Support Marketing Manager Amazon/Shop (m/w/d) Minijob](https://www.arbeitnow.com/jobs/companies/thiru-gmbh/e-commerce-support-marketing-manager-amazon-shop-minijob-olpe-221082)** en Thiru GmbH _(2026-05-03)_ - Arbeitnow
- **[Legal Data Analyst Junior Vaga Afirmativa para PCD](https://remoteOK.com/remote-jobs/remote-legal-data-analyst-junior-vaga-afirmativa-para-pcd-jusbrasil-1131393)** en Jusbrasil _(2026-04-30)_ - RemoteOK
- **[Lite Controller Pathfinder Hospitality](https://remoteOK.com/remote-jobs/remote-lite-controller-pathfinder-hospitality-pathfinder-hospitality-1131385)** en Pathfinder Hospitality _(2026-04-29)_ - RemoteOK

### Mobile

- **[Firmenkundenberater Immobiliengeschäft (m/w/d)](https://www.arbeitnow.com/jobs/companies/sparkasse-karlsruhe/firmenkundenberater-immobiliengeschaft-karlsruhe-384522)** en Sparkasse Karlsruhe _(2026-05-04)_ - Arbeitnow
- **[Senior PR Berater:in (m/w/d) in Vollzeit (40h/Woche)](https://www.arbeitnow.com/jobs/companies/cleo-public-relations/senior-pr-beraterin-hamburg-443351)** en Cléo Public Relations _(2026-05-03)_ - Arbeitnow

### Data

- **[Entry Level Crypto Market Specialist](https://remoteOK.com/remote-jobs/remote-entry-level-crypto-market-specialist-infiniti-group-1131416)** en Infiniti Group _(2026-05-01)_ - RemoteOK

### Other

- **[Team Lead Accounting | Scaling Phase](https://www.arbeitnow.com/jobs/companies/matera-gmbh/team-lead-accounting-scaling-phase-berlin-446026)** en Matera GmbH _(2026-05-04)_ - Arbeitnow
- **[Teamleitung Buchhaltung | Wachstumsphase](https://www.arbeitnow.com/jobs/companies/matera-gmbh/teamleitung-buchhaltung-wachstumsphase-berlin-372881)** en Matera GmbH _(2026-05-04)_ - Arbeitnow
- **[Werkstudent (m/w/d) – Finance & Beratung (unternehmerisch, leistungsbasiert)](https://www.arbeitnow.com/jobs/companies/kevin-kehr/werkstudent-finance-beratung-unternehmerisch-leistungsbasiert-hamburg-111783)** en Kevin Kehr _(2026-05-04)_ - Arbeitnow
- **[Junior Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/junior-artist-manager-influencer-manager-mulheim-47683)** en Lionflence _(2026-05-04)_ - Arbeitnow
- **[Trainee Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/trainee-artist-manager-influencer-manager-mulheim-310442)** en Lionflence _(2026-05-04)_ - Arbeitnow
- **[Trainee Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/trainee-artist-manager-influencer-manager-berlin-296254)** en Lionflence _(2026-05-04)_ - Arbeitnow
- **[Junior Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/junior-artist-manager-influencer-manager-berlin-949)** en Lionflence _(2026-05-04)_ - Arbeitnow
- **[Junior Key Account Customer Success Manager - SaaS - B2B (all genders)](https://www.arbeitnow.com/jobs/companies/doozer-real-estate-systems-gmbh/junior-key-account-customer-success-manager-saas-b2b-all-genders-berlin-126446)** en Doozer Real Estate Systems GmbH _(2026-05-03)_ - Arbeitnow

<!-- JOBS_END -->

---

## 🛠️ Stack Tecnológico
- Python 3 (`requests`, `beautifulsoup4`)
- GitHub Actions Automation Pipeline 
- Configuraciones parametrizadas vía JSON

## 🤝 Contribuir
Si conoces otras APIs abiertas para empleo Tech Junior, añade una fuente a `config.json` y su correspondiente mapeador a la carpeta `src/scrapers/`. 
_Hecho para la comunidad de Jr Devs._