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
| Analista de Seguridad de la Información Junior (2) | Php (1) |
| Senior Plattform Engineer (m/w/d) (2) | Back-end (1) |
| Desarrollador Back-end Junior (PHP) (1) | Front-end (1) |
| Front-end Developer Junior (1) | Java (1) |
| Desarrollador Full-Stack JavaScript/TypeScript Junior (1) | Javascript (1) |

### Frontend

- **[Desarrollador Back-end Junior (PHP)](https://www.getonbrd.com/jobs/desarrollador-backend-junior-php-braif-remote)** en GetOnBoard Company _(2026-04-06)_ - GetOnBoard
- **[Front-end Developer Junior](https://www.getonbrd.com/jobs/front-end-developer-junior-codeable-remote)** en GetOnBoard Company _(2026-03-31)_ - GetOnBoard
- **[Desarrollador Full-Stack JavaScript/TypeScript Junior](https://www.getonbrd.com/jobs/desarrollador-full-stack-javascript-typescript-junior-tcit-santiago)** en GetOnBoard Company _(2026-03-18)_ - GetOnBoard
- **[AI Engineer](https://www.getonbrd.com/jobs/senior-ai-engineer-mas-analytics-puerto-montt-santiago-puerto-varas)** en GetOnBoard Company _(2026-03-09)_ - GetOnBoard
- **[Ruby on Rails Developer (Junior / Semi Senior)](https://www.getonbrd.com/jobs/semi-senior-ruby-on-rails-developer-saas-subscriptions-riolab-santiago)** en GetOnBoard Company _(2026-02-17)_ - GetOnBoard
- **[Desarrollador Angular](https://www.getonbrd.com/jobs/desarrollador-angular-defontana-remote-159e)** en GetOnBoard Company _(2025-09-25)_ - GetOnBoard
- **[Junior Project Coordinator](https://remotive.com/remote-jobs/project-management/junior-project-coordinator-2088663)** en C4Media Inc. _(2026-03-24)_ - Remotive
- **[Intermediate Full Stack Engineer](https://remoteOK.com/remote-jobs/remote-intermediate-full-stack-engineer-runn-1130979)** en Runn _(2026-04-02)_ - RemoteOK
- **[Senior Full Stack Engineer](https://remoteOK.com/remote-jobs/remote-senior-full-stack-engineer-runn-1130978)** en Runn _(2026-04-02)_ - RemoteOK
- **[Senior Developer Backend Search CD+E](https://remoteOK.com/remote-jobs/remote-senior-developer-backend-search-cd-e-ubiminds-1130881)** en Ubiminds _(2026-03-26)_ - RemoteOK

### Backend

- **[Analista de Proyectos TI y Automatización](https://www.getonbrd.com/jobs/analista-de-proyectos-ti-y-automatizacion-tcit-santiago)** en GetOnBoard Company _(2026-03-30)_ - GetOnBoard
- **[Junior Growth Marketer (AI & Cloud Native)](https://www.getonbrd.com/jobs/senior-digital-marketing-growth-lead-ai-design-b2b-e-omnix-ai-corp-remote)** en GetOnBoard Company _(2026-03-26)_ - GetOnBoard
- **[Data Engineer Senior](https://www.getonbrd.com/jobs/data-engineer-senior-grupo-mariposa-remote)** en GetOnBoard Company _(2026-03-30)_ - GetOnBoard
- **[Ícaro Sales – Trainee Program](https://www.getonbrd.com/jobs/icaro-sales-trainee-program-iconstruye-santiago)** en GetOnBoard Company _(2026-03-11)_ - GetOnBoard
- **[Analista de Analítica Digital](https://www.getonbrd.com/jobs/analista-de-analitica-digital-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-03-05)_ - GetOnBoard
- **[Digital Quality Lead](https://www.getonbrd.com/jobs/digital-quality-lead-signant-health-remote)** en GetOnBoard Company _(2026-03-03)_ - GetOnBoard
- **[Coordinador(a) Junior de Gobierno de Datos](https://www.getonbrd.com/jobs/coordinador-a-junior-de-gobierno-de-datos-bice-vida-santiago)** en GetOnBoard Company _(2026-02-26)_ - GetOnBoard
- **[SRE / DevOps Engineer Junior](https://www.getonbrd.com/jobs/sre-devops-engineer-junior-bc-tecnologia-remote)** en GetOnBoard Company _(2026-02-24)_ - GetOnBoard
- **[Asesor Educativo Comercial Junior](https://www.getonbrd.com/jobs/asesor-educativo-comercial-junior-colectivo23-lima)** en GetOnBoard Company _(2026-02-02)_ - GetOnBoard
- **[Jr Sales Executive](https://www.getonbrd.com/jobs/jr-sales-executive-coderslab-io-ciudad-de-mexico)** en GetOnBoard Company _(2026-01-21)_ - GetOnBoard
- **[Ingeniero(a) Junior de Software y Robótica](https://www.getonbrd.com/jobs/ingeniero-a-junior-de-software-y-robotica-maquintel-robotic-services-santiago)** en GetOnBoard Company _(2026-01-19)_ - GetOnBoard
- **[Analista de Seguridad de la Información Junior](https://www.getonbrd.com/jobs/analista-de-seguridad-de-la-informacion-junior-bc-tecnologia-santiago-bb38)** en GetOnBoard Company _(2026-01-16)_ - GetOnBoard
- **[Analista de Seguridad de la Información Junior](https://www.getonbrd.com/jobs/analista-de-seguridad-de-la-informacion-junior-bc-tecnologia-santiago)** en GetOnBoard Company _(2025-12-22)_ - GetOnBoard
- **[Inside Sales Contractor](https://remotive.com/remote-jobs/sales-business/inside-sales-contractor-2086540)** en Credit Wellness, LLC _(2026-03-08)_ - Remotive
- **[Campaign Coordinator:in Influencer Marketing](https://www.arbeitnow.com/jobs/companies/rsa-media-gmbh/campaign-coordinatorin-influencer-marketing-berlin-437447)** en rsa Media GmbH _(2026-04-07)_ - Arbeitnow
- **[Senior Plattform Engineer (m/w/d)](https://www.arbeitnow.com/jobs/companies/jetztjob/senior-plattform-engineer-munich-226692)** en JetztJob _(2026-04-07)_ - Arbeitnow
- **[Senior Plattform Engineer (m/w/d)](https://www.arbeitnow.com/jobs/companies/aramaz-digital/senior-plattform-engineer-munchen-161657)** en Aramaz Digital _(2026-04-07)_ - Arbeitnow
- **[Senior Payroll Associate Indian Payroll India](https://remoteOK.com/remote-jobs/remote-senior-payroll-associate-indian-payroll-india-deel-1130900)** en Deel _(2026-03-27)_ - RemoteOK

### Mobile

- **[Salesforce Technical Consultant (Field Service)](https://www.getonbrd.com/jobs/salesforce-technical-consultant-field-service-niuro-remote)** en GetOnBoard Company _(2026-03-26)_ - GetOnBoard
- **[Junior Crypto Analyst & Trader](https://remoteOK.com/remote-jobs/remote-junior-crypto-analyst-trader-whitebridge-ltd-1130961)** en WhiteBridge-Ltd _(2026-04-01)_ - RemoteOK

### Data

- **[Soporte Operativo Junior](https://www.getonbrd.com/jobs/soporte-operativo-junior-bc-tecnologia-remote)** en GetOnBoard Company _(2026-03-31)_ - GetOnBoard
- **[AI Automation Engineer (Junior / Entry Level)](https://www.arbeitnow.com/jobs/companies/vetaion-gmbh/ai-automation-engineer-junior-entry-level-garching-213468)** en Vetaion GmbH _(2026-04-07)_ - Arbeitnow
- **[RevOps AI Analyst Intern](https://remoteOK.com/remote-jobs/remote-revops-ai-analyst-intern-actian-corporation-1130997)** en Actian Corporation _(2026-04-06)_ - RemoteOK

### QA

- **[Developer QA – Junior](https://www.getonbrd.com/jobs/developer-qa-junior-ameris-capital-santiago)** en GetOnBoard Company _(2026-04-01)_ - GetOnBoard

### Other

- **[Junior Network Engineer (Presencial)](https://www.getonbrd.com/jobs/networking-presencial-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-04-02)_ - GetOnBoard
- **[Ejecutiva de Cuenta Marketing Junior](https://www.getonbrd.com/jobs/ejecutiva-de-cuenta-match-agencia-consultora-remote)** en GetOnBoard Company _(2026-03-18)_ - GetOnBoard
- **[Ejecutivo en Generación de Demanda (Junior)](https://www.getonbrd.com/jobs/ejecutivo-en-generacion-de-demanda-dynamic-devs-santiago-acbd)** en GetOnBoard Company _(2026-03-04)_ - GetOnBoard
- **[Customer Success Executive Junior Técnico B2B/ IoT](https://www.getonbrd.com/jobs/customer-success-executive-junior-tecnico-b2b-iot-guinea-mobile-sac-cuy-movil-lima)** en GetOnBoard Company _(2026-02-10)_ - GetOnBoard
- **[Ejecutivo de Soporte Trainee](https://www.getonbrd.com/jobs/ejecutivo-de-soporte-trainee-agendapro-ciudad-de-mexico)** en GetOnBoard Company _(2026-01-19)_ - GetOnBoard
- **[Team Lead Accounting | Scaling Phase](https://www.arbeitnow.com/jobs/companies/matera-gmbh/team-lead-accounting-scaling-phase-berlin-206025)** en Matera GmbH _(2026-04-07)_ - Arbeitnow
- **[Teamleitung Buchhaltung | Wachstumsphase](https://www.arbeitnow.com/jobs/companies/matera-gmbh/teamleitung-buchhaltung-wachstumsphase-berlin-428453)** en Matera GmbH _(2026-04-07)_ - Arbeitnow
- **[Teamleitung (Fach-) Bauüberwacher Bahn LST (m/w/d)](https://www.arbeitnow.com/jobs/companies/con-ing-gmbh/teamleitung-fach-bauuberwacher-bahn-lst-karlsruhe-321206)** en CON-iNG GmbH _(2026-04-07)_ - Arbeitnow
- **[Fachinformatiker (m/w/d) – Junior IT Support & Infrastructure](https://www.arbeitnow.com/jobs/companies/dekographics-gmbh/fachinformatiker-junior-it-support-infrastructure-sankt-leon-rot-226717)** en dekoGraphics GmbH _(2026-04-07)_ - Arbeitnow
- **[Junior PR Manager (m/w/d) – Remote oder Berlin](https://www.arbeitnow.com/jobs/companies/getpress/junior-pr-manager-remote-oder-berlin-186642)** en getpress _(2026-04-06)_ - Arbeitnow

<!-- JOBS_END -->

---

## 🛠️ Stack Tecnológico
- Python 3 (`requests`, `beautifulsoup4`)
- GitHub Actions Automation Pipeline 
- Configuraciones parametrizadas vía JSON

## 🤝 Contribuir
Si conoces otras APIs abiertas para empleo Tech Junior, añade una fuente a `config.json` y su correspondiente mapeador a la carpeta `src/scrapers/`. 
_Hecho para la comunidad de Jr Devs._