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
| Analista de Seguridad de la Información Junior (2) | Back-end (1) |
| Trainee Artist Manager / Influencer Manager (m/w/d) (2) | Php (1) |
| Junior Artist Manager / Influencer Manager (m/w/d) (2) | Front-end (1) |
| Ingeniero Junior (1) | Ruby (1) |
| Desarrollador Back-end Junior (PHP) (1) | Angular (1) |

### Frontend

- **[Ingeniero Junior](https://www.getonbrd.com/jobs/ingeniero-junior-khipu-remote-e6b1)** en GetOnBoard Company _(2026-04-08)_ - GetOnBoard
- **[Desarrollador Back-end Junior (PHP)](https://www.getonbrd.com/jobs/desarrollador-backend-junior-php-braif-remote)** en GetOnBoard Company _(2026-04-06)_ - GetOnBoard
- **[Front-end Developer Junior](https://www.getonbrd.com/jobs/front-end-developer-junior-codeable-remote)** en GetOnBoard Company _(2026-03-31)_ - GetOnBoard
- **[AI Engineer](https://www.getonbrd.com/jobs/senior-ai-engineer-mas-analytics-puerto-montt-santiago-puerto-varas)** en GetOnBoard Company _(2026-03-09)_ - GetOnBoard
- **[Ruby on Rails Developer (Junior / Semi Senior)](https://www.getonbrd.com/jobs/semi-senior-ruby-on-rails-developer-saas-subscriptions-riolab-santiago)** en GetOnBoard Company _(2026-02-17)_ - GetOnBoard
- **[Desarrollador Angular](https://www.getonbrd.com/jobs/desarrollador-angular-defontana-remote-159e)** en GetOnBoard Company _(2025-09-25)_ - GetOnBoard
- **[Junior Project Coordinator](https://remotive.com/remote-jobs/project-management/junior-project-coordinator-2088663)** en C4Media Inc. _(2026-03-24)_ - Remotive
- **[Staff Software Engineer Full Stack](https://remoteOK.com/remote-jobs/remote-staff-software-engineer-full-stack-ternary-1131066)** en Ternary _(2026-04-10)_ - RemoteOK
- **[Senior front end developer](https://remoteOK.com/remote-jobs/remote-senior-front-end-developer-expatfile-tax-1131019)** en Expatfile.tax _(2026-04-07)_ - RemoteOK
- **[Intermediate Full Stack Engineer](https://remoteOK.com/remote-jobs/remote-intermediate-full-stack-engineer-runn-1130979)** en Runn _(2026-04-02)_ - RemoteOK
- **[Senior Full Stack Engineer](https://remoteOK.com/remote-jobs/remote-senior-full-stack-engineer-runn-1130978)** en Runn _(2026-04-02)_ - RemoteOK

### Backend

- **[Analista de Proyectos TI y Automatización](https://www.getonbrd.com/jobs/analista-de-proyectos-ti-y-automatizacion-tcit-santiago)** en GetOnBoard Company _(2026-03-30)_ - GetOnBoard
- **[Junior Growth Marketer (AI & Cloud Native)](https://www.getonbrd.com/jobs/senior-digital-marketing-growth-lead-ai-design-b2b-e-omnix-ai-corp-remote)** en GetOnBoard Company _(2026-03-26)_ - GetOnBoard
- **[Ícaro Sales – Trainee Program](https://www.getonbrd.com/jobs/icaro-sales-trainee-program-iconstruye-santiago)** en GetOnBoard Company _(2026-03-11)_ - GetOnBoard
- **[Analista de Analítica Digital](https://www.getonbrd.com/jobs/analista-de-analitica-digital-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-03-05)_ - GetOnBoard
- **[Digital Quality Lead](https://www.getonbrd.com/jobs/digital-quality-lead-signant-health-remote)** en GetOnBoard Company _(2026-03-03)_ - GetOnBoard
- **[Coordinador(a) Junior de Gobierno de Datos](https://www.getonbrd.com/jobs/coordinador-a-junior-de-gobierno-de-datos-bice-vida-santiago)** en GetOnBoard Company _(2026-02-26)_ - GetOnBoard
- **[SRE / DevOps Engineer Junior](https://www.getonbrd.com/jobs/sre-devops-engineer-junior-bc-tecnologia-remote)** en GetOnBoard Company _(2026-02-24)_ - GetOnBoard
- **[Asesor de Contactabilidad Junior](https://www.getonbrd.com/jobs/asesor-educativo-comercial-junior-colectivo23-lima)** en GetOnBoard Company _(2026-02-02)_ - GetOnBoard
- **[Jr Sales Executive](https://www.getonbrd.com/jobs/jr-sales-executive-coderslab-io-ciudad-de-mexico)** en GetOnBoard Company _(2026-01-21)_ - GetOnBoard
- **[Ingeniero(a) Junior de Software y Robótica](https://www.getonbrd.com/jobs/ingeniero-a-junior-de-software-y-robotica-maquintel-robotic-services-santiago)** en GetOnBoard Company _(2026-01-19)_ - GetOnBoard
- **[Analista de Seguridad de la Información Junior](https://www.getonbrd.com/jobs/analista-de-seguridad-de-la-informacion-junior-bc-tecnologia-santiago-bb38)** en GetOnBoard Company _(2026-01-16)_ - GetOnBoard
- **[Analista de Seguridad de la Información Junior](https://www.getonbrd.com/jobs/analista-de-seguridad-de-la-informacion-junior-bc-tecnologia-santiago)** en GetOnBoard Company _(2025-12-22)_ - GetOnBoard
- **[Junior PostSales Mitarbeiter / Fachinformatiker für Systemintegration (m/w/d)](https://www.arbeitnow.com/jobs/companies/hg-hansen-gieraths-edv-vertriebsgesellschaft-mbh/junior-postsales-mitarbeiter-fachinformatiker-fur-systemintegration-bonn-135316)** en H&G Hansen & Gieraths EDV Vertriebsgesellschaft mbH _(2026-04-13)_ - Arbeitnow
- **[Machine Learning Engineer](https://remoteOK.com/remote-jobs/remote-machine-learning-engineer-radformation-1131082)** en Radformation _(2026-04-11)_ - RemoteOK
- **[Junior Integration Manager US](https://remoteOK.com/remote-jobs/remote-junior-integration-manager-us-xsolla-1131071)** en Xsolla _(2026-04-10)_ - RemoteOK
- **[Senior FinCrime Support Analyst](https://remoteOK.com/remote-jobs/remote-senior-fincrime-support-analyst-apron-1131067)** en Apron _(2026-04-10)_ - RemoteOK

### Mobile

- **[Salesforce Technical Consultant (Field Service)](https://www.getonbrd.com/jobs/salesforce-technical-consultant-field-service-niuro-remote)** en GetOnBoard Company _(2026-03-26)_ - GetOnBoard

### Data

- **[Soporte Operativo Junior](https://www.getonbrd.com/jobs/soporte-operativo-junior-bc-tecnologia-remote)** en GetOnBoard Company _(2026-03-31)_ - GetOnBoard
- **[RevOps AI Analyst Intern](https://remoteOK.com/remote-jobs/remote-revops-ai-analyst-intern-actian-corporation-1130997)** en Actian Corporation _(2026-04-06)_ - RemoteOK

### QA

- **[Developer QA – Junior](https://www.getonbrd.com/jobs/developer-qa-junior-ameris-capital-santiago)** en GetOnBoard Company _(2026-04-07)_ - GetOnBoard
- **[Full-Stack & AI Developer](https://www.getonbrd.com/jobs/full-stack-ai-developer-geniesoft-inc-remote)** en GetOnBoard Company _(2026-04-13)_ - GetOnBoard

### Other

- **[Junior Network Engineer (Presencial)](https://www.getonbrd.com/jobs/networking-presencial-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-04-02)_ - GetOnBoard
- **[Ejecutiva de Cuenta Marketing Junior](https://www.getonbrd.com/jobs/ejecutiva-de-cuenta-match-agencia-consultora-remote)** en GetOnBoard Company _(2026-03-18)_ - GetOnBoard
- **[Ejecutivo en Generación de Demanda (Junior)](https://www.getonbrd.com/jobs/ejecutivo-en-generacion-de-demanda-dynamic-devs-santiago-acbd)** en GetOnBoard Company _(2026-03-04)_ - GetOnBoard
- **[Customer Success Executive Junior Técnico B2B/ IoT](https://www.getonbrd.com/jobs/customer-success-executive-junior-tecnico-b2b-iot-guinea-mobile-sac-cuy-movil-lima)** en GetOnBoard Company _(2026-02-10)_ - GetOnBoard
- **[Ejecutivo de Soporte Trainee](https://www.getonbrd.com/jobs/ejecutivo-de-soporte-trainee-agendapro-ciudad-de-mexico)** en GetOnBoard Company _(2026-01-19)_ - GetOnBoard
- **[Junior Consultant (m/w/d) - IT-Systeme, Prozesse & Datenflüsse](https://www.arbeitnow.com/jobs/companies/impecto-consulting-gmbh/junior-consultant-it-systeme-prozesse-datenflusse-dusseldorf-424711)** en Impecto-Consulting GmbH _(2026-04-13)_ - Arbeitnow
- **[Team Lead Accounting | Scaling Phase](https://www.arbeitnow.com/jobs/companies/matera-gmbh/team-lead-accounting-scaling-phase-berlin-63770)** en Matera GmbH _(2026-04-13)_ - Arbeitnow
- **[Junior IT-Administrator (m/w/d](https://www.arbeitnow.com/jobs/companies/klapp-cosmetics-gmbh/junior-it-administrator-hessisch-lichtenau-162424)** en Klapp Cosmetics GmbH _(2026-04-13)_ - Arbeitnow
- **[Teamleitung Buchhaltung | Wachstumsphase](https://www.arbeitnow.com/jobs/companies/matera-gmbh/teamleitung-buchhaltung-wachstumsphase-berlin-90046)** en Matera GmbH _(2026-04-13)_ - Arbeitnow
- **[Junior Performance Marketing Manager (w/m/d) - 100% remote - Deutschland](https://www.arbeitnow.com/jobs/companies/pynema/junior-performance-marketing-manager-100-remote-deutschland-munich-429585)** en PYNEMA _(2026-04-13)_ - Arbeitnow
- **[(Junior) Account Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/proconcept-sales-gmbh/junior-account-manager-cologne-172575)** en PROCONCEPT Sales GmbH _(2026-04-12)_ - Arbeitnow
- **[Trainee Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/trainee-artist-manager-influencer-manager-berlin-257850)** en Lionflence _(2026-04-12)_ - Arbeitnow
- **[Trainee Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/trainee-artist-manager-influencer-manager-mulheim-411369)** en Lionflence _(2026-04-12)_ - Arbeitnow
- **[Junior Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/junior-artist-manager-influencer-manager-mulheim-248286)** en Lionflence _(2026-04-12)_ - Arbeitnow
- **[Junior Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/junior-artist-manager-influencer-manager-berlin-272397)** en Lionflence _(2026-04-12)_ - Arbeitnow

<!-- JOBS_END -->

---

## 🛠️ Stack Tecnológico
- Python 3 (`requests`, `beautifulsoup4`)
- GitHub Actions Automation Pipeline 
- Configuraciones parametrizadas vía JSON

## 🤝 Contribuir
Si conoces otras APIs abiertas para empleo Tech Junior, añade una fuente a `config.json` y su correspondiente mapeador a la carpeta `src/scrapers/`. 
_Hecho para la comunidad de Jr Devs._