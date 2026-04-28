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
| AI Engineer (2) | Front-end (1) |
| Analista de Seguridad de la Información Junior (2) | Ruby (1) |
| Trainee (m/w/d) Consulting (2) | Automation (1) |
| Junior Front-end Engineer (1) | Python (1) |
| Ingeniero Junior (1) | Backend (1) |

### Frontend

- **[Junior Front-end Engineer](https://www.getonbrd.com/jobs/junior-frontend-engineer-krunchbox-santiago)** en GetOnBoard Company _(2026-04-22)_ - GetOnBoard
- **[Ingeniero Junior](https://www.getonbrd.com/jobs/ingeniero-junior-khipu-remote-e6b1)** en GetOnBoard Company _(2026-04-08)_ - GetOnBoard
- **[AI Engineer](https://www.getonbrd.com/jobs/senior-ai-engineer-mas-analytics-puerto-montt-santiago-puerto-varas)** en GetOnBoard Company _(2026-03-09)_ - GetOnBoard
- **[Ruby on Rails Developer (Junior / Semi Senior)](https://www.getonbrd.com/jobs/semi-senior-ruby-on-rails-developer-saas-subscriptions-riolab-santiago)** en GetOnBoard Company _(2026-02-17)_ - GetOnBoard
- **[(Junior) Fullstack Developer (m/w/d)](https://www.arbeitnow.com/jobs/companies/dsb-deutsche-sanierungsberatung-gmbh/junior-fullstack-developer-berlin-9369)** en dsb Deutsche Sanierungsberatung GmbH _(2026-04-28)_ - Arbeitnow
- **[Senior Backend Engineer (Python / Azure) - Schnittstellen & Lagerautomation](https://www.arbeitnow.com/jobs/companies/altruan-gmbh/senior-backend-engineer-python-azure-schnittstellen-lagerautomation-massing-139183)** en Altruan GmbH _(2026-04-28)_ - Arbeitnow
- **[Software Engineer](https://remoteOK.com/remote-jobs/remote-software-engineer-finalis-1131328)** en Finalis _(2026-04-26)_ - RemoteOK
- **[Senior App &amp; Frontend Developer AS233](https://remoteOK.com/remote-jobs/remote-senior-app-amp-frontend-developer-as233-smart-working-solutions-1131268)** en Smart Working Solutions _(2026-04-22)_ - RemoteOK
- **[Senior Product Manager Applied AI](https://remoteOK.com/remote-jobs/remote-senior-product-manager-applied-ai-smartsheet-1131233)** en Smartsheet _(2026-04-21)_ - RemoteOK

### Backend

- **[Ingeniero Junior en Inteligencia Artificial](https://www.getonbrd.com/jobs/ingeniero-junior-en-inteligencia-artificial-bice-vida-santiago)** en GetOnBoard Company _(2026-04-21)_ - GetOnBoard
- **[Analista de Ciberseguridad Junior](https://www.getonbrd.com/jobs/analista-de-ciberseguridad-junior-hf-solutions-santiago)** en GetOnBoard Company _(2026-04-20)_ - GetOnBoard
- **[Product Owner Junior](https://www.getonbrd.com/jobs/product-owner-junior-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-04-15)_ - GetOnBoard
- **[Business Analyst Junior](https://www.getonbrd.com/jobs/business-analyst-junior-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-04-22)_ - GetOnBoard
- **[Coordinador(a) Junior de Gobierno de Datos](https://www.getonbrd.com/jobs/coordinador-a-junior-de-gobierno-de-datos-bice-vida-santiago)** en GetOnBoard Company _(2026-04-21)_ - GetOnBoard
- **[Junior Growth Marketer (AI & Cloud Native)](https://www.getonbrd.com/jobs/senior-digital-marketing-growth-lead-ai-design-b2b-e-omnix-ai-corp-remote)** en GetOnBoard Company _(2026-03-26)_ - GetOnBoard
- **[Analista de Analítica Digital](https://www.getonbrd.com/jobs/analista-de-analitica-digital-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-03-05)_ - GetOnBoard
- **[Digital Quality Lead](https://www.getonbrd.com/jobs/digital-quality-lead-signant-health-remote)** en GetOnBoard Company _(2026-03-03)_ - GetOnBoard
- **[SRE / DevOps Engineer Junior](https://www.getonbrd.com/jobs/sre-devops-engineer-junior-bc-tecnologia-remote)** en GetOnBoard Company _(2026-02-24)_ - GetOnBoard
- **[Asesor de Contactabilidad Junior](https://www.getonbrd.com/jobs/asesor-educativo-comercial-junior-colectivo23-lima)** en GetOnBoard Company _(2026-02-02)_ - GetOnBoard
- **[Jr Sales Executive](https://www.getonbrd.com/jobs/jr-sales-executive-coderslab-io-ciudad-de-mexico)** en GetOnBoard Company _(2026-01-21)_ - GetOnBoard
- **[Ingeniero(a) Junior de Software y Robótica](https://www.getonbrd.com/jobs/ingeniero-a-junior-de-software-y-robotica-maquintel-robotic-services-santiago)** en GetOnBoard Company _(2026-01-19)_ - GetOnBoard
- **[Analista de Seguridad de la Información Junior](https://www.getonbrd.com/jobs/analista-de-seguridad-de-la-informacion-junior-bc-tecnologia-santiago-bb38)** en GetOnBoard Company _(2026-01-16)_ - GetOnBoard
- **[Analista de Seguridad de la Información Junior](https://www.getonbrd.com/jobs/analista-de-seguridad-de-la-informacion-junior-bc-tecnologia-santiago)** en GetOnBoard Company _(2025-12-22)_ - GetOnBoard
- **[AI Engineer](https://remotive.com/remote-jobs/artificial-intelligence/ai-engineer-2089958)** en Dry Ground AI _(2026-04-21)_ - Remotive
- **[Werkstudent:in (m/w/d) Digital Marketing & Performance Advertising](https://www.arbeitnow.com/jobs/companies/luna-park-gmbh-digital-marketing-agentur/werkstudentin-digital-marketing-performance-advertising-cologne-82530)** en luna-park GmbH - Digital Marketing Agentur _(2026-04-28)_ - Arbeitnow
- **[Junior Performance Marketing Manager (all genders)](https://www.arbeitnow.com/jobs/companies/glow25-by-primal-state-performance-gmbh/junior-performance-marketing-manager-all-genders-berlin-155983)** en Glow25 (by Primal State Performance GmbH) _(2026-04-28)_ - Arbeitnow
- **[Junior Art Director (all genders)](https://www.arbeitnow.com/jobs/companies/adbaker/junior-art-director-all-genders-cologne-308400)** en ADBAKER _(2026-04-27)_ - Arbeitnow
- **[(Junior) Creative Designer - Statics (all genders)](https://www.arbeitnow.com/jobs/companies/adbaker/junior-creative-designer-statics-all-genders-cologne-239419)** en ADBAKER _(2026-04-27)_ - Arbeitnow
- **[Head of Government Sales](https://www.arbeitnow.com/jobs/companies/24industries/head-of-government-sales-munich-315796)** en 24Industries _(2026-04-28)_ - Arbeitnow
- **[Data Analyst](https://remoteOK.com/remote-jobs/remote-data-analyst-criptoro-1131219)** en Criptoro _(2026-04-19)_ - RemoteOK

### Mobile

- **[Salesforce Technical Consultant (Field Service)](https://www.getonbrd.com/jobs/salesforce-technical-consultant-field-service-niuro-remote)** en GetOnBoard Company _(2026-03-26)_ - GetOnBoard

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
- **[Junior Projektmanager (m/w/d) / POS-Erfahrung & Handels-Experience von Vorteil](https://www.arbeitnow.com/jobs/companies/revo-gmbh/junior-projektmanager-pos-erfahrung-handels-experience-von-vorteil-cologne-308333)** en REVO GmbH _(2026-04-28)_ - Arbeitnow
- **[Trainee (m/w/d) Consulting](https://www.arbeitnow.com/jobs/companies/mlp-wirtschaftsberatung/trainee-consulting-cologne-337476)** en MLP Wirtschaftsberatung _(2026-04-28)_ - Arbeitnow
- **[Trainee (m/w/d) Consulting](https://www.arbeitnow.com/jobs/companies/mlp-wirtschaftsberatung/trainee-consulting-bonn-449887)** en MLP Wirtschaftsberatung _(2026-04-28)_ - Arbeitnow

<!-- JOBS_END -->

---

## 🛠️ Stack Tecnológico
- Python 3 (`requests`, `beautifulsoup4`)
- GitHub Actions Automation Pipeline 
- Configuraciones parametrizadas vía JSON

## 🤝 Contribuir
Si conoces otras APIs abiertas para empleo Tech Junior, añade una fuente a `config.json` y su correspondiente mapeador a la carpeta `src/scrapers/`. 
_Hecho para la comunidad de Jr Devs._