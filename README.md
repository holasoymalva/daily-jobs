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
| Analista de Seguridad de la Información Junior (2) | Ruby (1) |
| Trainee Artist Manager / Influencer Manager (m/w/d) (2) | Angular (1) |
| Junior Artist Manager / Influencer Manager (m/w/d) (2) | Data (1) |
| Desarrollador/a Full-Stack Junior (1) | Data engineer (1) |
| Ingeniero Junior (1) | Qa (1) |

### Frontend

- **[Desarrollador/a Full-Stack Junior](https://www.getonbrd.com/jobs/desarrollador-a-full-stack-junior-btrust-santiago)** en GetOnBoard Company _(2026-04-17)_ - GetOnBoard
- **[Ingeniero Junior](https://www.getonbrd.com/jobs/ingeniero-junior-khipu-remote-e6b1)** en GetOnBoard Company _(2026-04-08)_ - GetOnBoard
- **[Desarrollador Full-Stack Junior MERN/MEAN](https://www.getonbrd.com/jobs/desarrollador-fullstack-junior-mern-mean-agilistik-santiago)** en GetOnBoard Company _(2026-04-17)_ - GetOnBoard
- **[AI Engineer](https://www.getonbrd.com/jobs/senior-ai-engineer-mas-analytics-puerto-montt-santiago-puerto-varas)** en GetOnBoard Company _(2026-03-09)_ - GetOnBoard
- **[Ruby on Rails Developer (Junior / Semi Senior)](https://www.getonbrd.com/jobs/semi-senior-ruby-on-rails-developer-saas-subscriptions-riolab-santiago)** en GetOnBoard Company _(2026-02-17)_ - GetOnBoard
- **[Desarrollador Angular](https://www.getonbrd.com/jobs/desarrollador-angular-defontana-remote-159e)** en GetOnBoard Company _(2025-09-25)_ - GetOnBoard
- **[Junior Project Coordinator](https://remotive.com/remote-jobs/project-management/junior-project-coordinator-2088663)** en C4Media Inc. _(2026-03-24)_ - Remotive
- **[Banking Full Stack Software Developer TSCM 43657](https://remoteOK.com/remote-jobs/remote-banking-full-stack-software-developer-tscm-43657-eleks-1131120)** en Eleks _(2026-04-15)_ - RemoteOK

### Backend

- **[Data Engineer Senior](https://www.getonbrd.com/jobs/data-engineer-senior-grupo-mariposa-remote-ba30)** en GetOnBoard Company _(2026-04-15)_ - GetOnBoard
- **[Product Owner Junior](https://www.getonbrd.com/jobs/product-owner-junior-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-04-15)_ - GetOnBoard
- **[Analista de Proyectos TI y Automatización](https://www.getonbrd.com/jobs/analista-de-proyectos-ti-y-automatizacion-tcit-santiago)** en GetOnBoard Company _(2026-03-30)_ - GetOnBoard
- **[Junior Growth Marketer (AI & Cloud Native)](https://www.getonbrd.com/jobs/senior-digital-marketing-growth-lead-ai-design-b2b-e-omnix-ai-corp-remote)** en GetOnBoard Company _(2026-03-26)_ - GetOnBoard
- **[Analista de Analítica Digital](https://www.getonbrd.com/jobs/analista-de-analitica-digital-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-03-05)_ - GetOnBoard
- **[Digital Quality Lead](https://www.getonbrd.com/jobs/digital-quality-lead-signant-health-remote)** en GetOnBoard Company _(2026-03-03)_ - GetOnBoard
- **[Coordinador(a) Junior de Gobierno de Datos](https://www.getonbrd.com/jobs/coordinador-a-junior-de-gobierno-de-datos-bice-vida-santiago)** en GetOnBoard Company _(2026-02-26)_ - GetOnBoard
- **[SRE / DevOps Engineer Junior](https://www.getonbrd.com/jobs/sre-devops-engineer-junior-bc-tecnologia-remote)** en GetOnBoard Company _(2026-02-24)_ - GetOnBoard
- **[Asesor de Contactabilidad Junior](https://www.getonbrd.com/jobs/asesor-educativo-comercial-junior-colectivo23-lima)** en GetOnBoard Company _(2026-02-02)_ - GetOnBoard
- **[Jr Sales Executive](https://www.getonbrd.com/jobs/jr-sales-executive-coderslab-io-ciudad-de-mexico)** en GetOnBoard Company _(2026-01-21)_ - GetOnBoard
- **[Ingeniero(a) Junior de Software y Robótica](https://www.getonbrd.com/jobs/ingeniero-a-junior-de-software-y-robotica-maquintel-robotic-services-santiago)** en GetOnBoard Company _(2026-01-19)_ - GetOnBoard
- **[Analista de Seguridad de la Información Junior](https://www.getonbrd.com/jobs/analista-de-seguridad-de-la-informacion-junior-bc-tecnologia-santiago-bb38)** en GetOnBoard Company _(2026-01-16)_ - GetOnBoard
- **[Analista de Seguridad de la Información Junior](https://www.getonbrd.com/jobs/analista-de-seguridad-de-la-informacion-junior-bc-tecnologia-santiago)** en GetOnBoard Company _(2025-12-22)_ - GetOnBoard
- **[Freelance Junior Software Developer (m/f/d)](https://www.arbeitnow.com/jobs/companies/beyobie/freelance-junior-software-developer-berlin-231901)** en beyobie _(2026-04-20)_ - Arbeitnow
- **[Junior Controlling & Compliance Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/sevest/junior-controlling-compliance-manager-munich-179172)** en SEVEST _(2026-04-20)_ - Arbeitnow

### Mobile

- **[Salesforce Technical Consultant (Field Service)](https://www.getonbrd.com/jobs/salesforce-technical-consultant-field-service-niuro-remote)** en GetOnBoard Company _(2026-03-26)_ - GetOnBoard
- **[Junior Product Manager | Students Experience (m/w/d)](https://www.arbeitnow.com/jobs/companies/digitale-leute-school/junior-product-manager-students-experience-berlin-290644)** en Digitale Leute School _(2026-04-20)_ - Arbeitnow

### Data

- **[Soporte Operativo Junior](https://www.getonbrd.com/jobs/soporte-operativo-junior-bc-tecnologia-remote)** en GetOnBoard Company _(2026-03-31)_ - GetOnBoard

### QA

- **[Developer QA – Junior](https://www.getonbrd.com/jobs/developer-qa-junior-ameris-capital-santiago)** en GetOnBoard Company _(2026-04-07)_ - GetOnBoard

### Other

- **[Auxiliar de Operaciones Jr](https://www.getonbrd.com/jobs/auxiliar-de-operaciones-jr-coderslab-io-lima)** en GetOnBoard Company _(2026-04-17)_ - GetOnBoard
- **[Junior Network Engineer (Presencial)](https://www.getonbrd.com/jobs/networking-presencial-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-04-02)_ - GetOnBoard
- **[Ejecutiva de Cuenta Marketing Junior](https://www.getonbrd.com/jobs/ejecutiva-de-cuenta-match-agencia-consultora-remote)** en GetOnBoard Company _(2026-03-18)_ - GetOnBoard
- **[Ejecutivo en Generación de Demanda (Junior)](https://www.getonbrd.com/jobs/ejecutivo-en-generacion-de-demanda-dynamic-devs-santiago-acbd)** en GetOnBoard Company _(2026-03-04)_ - GetOnBoard
- **[Customer Success Executive Junior Técnico B2B/ IoT](https://www.getonbrd.com/jobs/customer-success-executive-junior-tecnico-b2b-iot-guinea-mobile-sac-cuy-movil-lima)** en GetOnBoard Company _(2026-02-10)_ - GetOnBoard
- **[Ejecutivo de Soporte Trainee](https://www.getonbrd.com/jobs/ejecutivo-de-soporte-trainee-agendapro-ciudad-de-mexico)** en GetOnBoard Company _(2026-01-19)_ - GetOnBoard
- **[Trainee Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/trainee-artist-manager-influencer-manager-berlin-89239)** en Lionflence _(2026-04-20)_ - Arbeitnow
- **[Trainee Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/trainee-artist-manager-influencer-manager-mulheim-41653)** en Lionflence _(2026-04-20)_ - Arbeitnow
- **[Junior Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/junior-artist-manager-influencer-manager-mulheim-312141)** en Lionflence _(2026-04-20)_ - Arbeitnow
- **[Junior Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/junior-artist-manager-influencer-manager-berlin-414850)** en Lionflence _(2026-04-20)_ - Arbeitnow

<!-- JOBS_END -->

---

## 🛠️ Stack Tecnológico
- Python 3 (`requests`, `beautifulsoup4`)
- GitHub Actions Automation Pipeline 
- Configuraciones parametrizadas vía JSON

## 🤝 Contribuir
Si conoces otras APIs abiertas para empleo Tech Junior, añade una fuente a `config.json` y su correspondiente mapeador a la carpeta `src/scrapers/`. 
_Hecho para la comunidad de Jr Devs._