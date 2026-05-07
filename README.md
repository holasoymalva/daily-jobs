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
| AI Engineer (2) | Data (2) |
| Analista de Seguridad de la Información Junior (2) | Front-end (1) |
| Junior Front-end Engineer (1) | Ruby (1) |
| Ingeniero Junior (1) | Data engineer (1) |
| Ruby on Rails Developer (Junior / Semi Senior) (1) | Data analyst (1) |

### Frontend

- **[Junior Front-end Engineer](https://www.getonbrd.com/jobs/junior-frontend-engineer-krunchbox-santiago)** en GetOnBoard Company _(2026-04-22)_ - GetOnBoard
- **[Ingeniero Junior](https://www.getonbrd.com/jobs/ingeniero-junior-khipu-remote-e6b1)** en GetOnBoard Company _(2026-04-08)_ - GetOnBoard
- **[AI Engineer](https://www.getonbrd.com/jobs/senior-ai-engineer-mas-analytics-puerto-montt-santiago-puerto-varas)** en GetOnBoard Company _(2026-03-09)_ - GetOnBoard
- **[Ruby on Rails Developer (Junior / Semi Senior)](https://www.getonbrd.com/jobs/semi-senior-ruby-on-rails-developer-saas-subscriptions-riolab-santiago)** en GetOnBoard Company _(2026-02-17)_ - GetOnBoard
- **[Junior Mid Full Stack Software Engineer](https://remoteOK.com/remote-jobs/remote-junior-mid-full-stack-software-engineer-black-canyon-consulting-1131437)** en Black Canyon Consulting _(2026-05-03)_ - RemoteOK

### Backend

- **[Analista de Proyectos TI y Automatización](https://www.getonbrd.com/jobs/analista-de-proyectos-ti-y-automatizacion-tcit-santiago-e09d)** en GetOnBoard Company _(2026-05-06)_ - GetOnBoard
- **[Business Analyst Junior](https://www.getonbrd.com/jobs/business-analyst-junior-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-04-22)_ - GetOnBoard
- **[Coordinador(a) Junior de Gobierno de Datos](https://www.getonbrd.com/jobs/coordinador-a-junior-de-gobierno-de-datos-bice-vida-santiago)** en GetOnBoard Company _(2026-04-21)_ - GetOnBoard
- **[Ingeniero Junior en Inteligencia Artificial](https://www.getonbrd.com/jobs/ingeniero-junior-en-inteligencia-artificial-bice-vida-santiago)** en GetOnBoard Company _(2026-04-21)_ - GetOnBoard
- **[Data Engineer Senior](https://www.getonbrd.com/jobs/data-engineer-senior-grupo-mariposa-remote-ba30)** en GetOnBoard Company _(2026-04-15)_ - GetOnBoard
- **[Product Owner Junior](https://www.getonbrd.com/jobs/product-owner-junior-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-04-15)_ - GetOnBoard
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
- **[Inside Sales Contractor](https://remotive.com/remote-jobs/sales/inside-sales-contractor-2086540)** en Credit Wellness, LLC _(2026-04-13)_ - Remotive
- **[Junior E-Commerce Content Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/tectake-gmbh/junior-e-commerce-content-manager-hochberg-227559)** en TecTake GmbH _(2026-05-07)_ - Arbeitnow
- **[Senior Analytics Engineer - Growth (m/f/d)](https://www.arbeitnow.com/jobs/companies/1komma50/senior-analytics-engineer-growth-berlin-355947)** en 1KOMMA5˚ _(2026-05-06)_ - Arbeitnow
- **[UI Developer](https://remoteOK.com/remote-jobs/remote-ui-developer-rainfocus-1131473)** en RainFocus _(2026-05-05)_ - RemoteOK
- **[Legal Data Analyst Junior Vaga Afirmativa para PCD](https://remoteOK.com/remote-jobs/remote-legal-data-analyst-junior-vaga-afirmativa-para-pcd-jusbrasil-1131393)** en Jusbrasil _(2026-04-30)_ - RemoteOK
- **[Lite Controller Pathfinder Hospitality](https://remoteOK.com/remote-jobs/remote-lite-controller-pathfinder-hospitality-pathfinder-hospitality-1131385)** en Pathfinder Hospitality _(2026-04-29)_ - RemoteOK

### Mobile

- **[DevOps Junior (Latam )](https://www.getonbrd.com/jobs/devops-jr-remoto-latam-i2b-technologies-remote)** en GetOnBoard Company _(2026-04-28)_ - GetOnBoard

### Data

- **[SAP Fico Functional Consultant](https://www.getonbrd.com/jobs/sap-fico-functional-consultant-crest-it-resources-llc-remote)** en GetOnBoard Company _(2026-04-29)_ - GetOnBoard
- **[Soporte Operativo Junior](https://www.getonbrd.com/jobs/soporte-operativo-junior-bc-tecnologia-remote)** en GetOnBoard Company _(2026-03-31)_ - GetOnBoard
- **[Entry Level Crypto Market Specialist](https://remoteOK.com/remote-jobs/remote-entry-level-crypto-market-specialist-infiniti-group-1131416)** en Infiniti Group _(2026-05-01)_ - RemoteOK

### QA

- **[Developer QA – Junior](https://www.getonbrd.com/jobs/developer-qa-junior-ameris-capital-santiago)** en GetOnBoard Company _(2026-04-07)_ - GetOnBoard

### Other

- **[Ejecutivo en Generación de Demanda (Junior)](https://www.getonbrd.com/jobs/ejecutivo-en-generacion-de-demanda-dynamic-devs-santiago-acbd)** en GetOnBoard Company _(2026-04-29)_ - GetOnBoard
- **[Commercial & Technical Pre Sales Associate](https://www.getonbrd.com/jobs/commercial-technical-pre-sales-associate-solvia-analytics-remote)** en GetOnBoard Company _(2026-05-03)_ - GetOnBoard
- **[Auxiliar de Operaciones Jr](https://www.getonbrd.com/jobs/auxiliar-de-operaciones-jr-coderslab-io-lima)** en GetOnBoard Company _(2026-04-17)_ - GetOnBoard
- **[Junior Network Engineer (Presencial)](https://www.getonbrd.com/jobs/networking-presencial-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-04-02)_ - GetOnBoard
- **[Ejecutiva de Cuenta Marketing Junior](https://www.getonbrd.com/jobs/ejecutiva-de-cuenta-match-agencia-consultora-remote)** en GetOnBoard Company _(2026-03-18)_ - GetOnBoard
- **[Customer Success Executive Junior Técnico B2B/ IoT](https://www.getonbrd.com/jobs/customer-success-executive-junior-tecnico-b2b-iot-guinea-mobile-sac-cuy-movil-lima)** en GetOnBoard Company _(2026-02-10)_ - GetOnBoard
- **[Ejecutivo de Soporte Trainee](https://www.getonbrd.com/jobs/ejecutivo-de-soporte-trainee-agendapro-ciudad-de-mexico)** en GetOnBoard Company _(2026-01-19)_ - GetOnBoard
- **[Senior Inhouse Berater SAP und EDI (m/w/d)](https://www.arbeitnow.com/jobs/companies/hubside-die-recruitingwerkstatt/senior-inhouse-berater-sap-und-edi-eching-399210)** en hubside - Die Recruitingwerkstatt _(2026-05-07)_ - Arbeitnow
- **[Junior Sales Development Manager:in B2B SaaS / RegTech (JSD)](https://www.arbeitnow.com/jobs/companies/central-agency-for-green-commerce-gmbh/junior-sales-development-managerin-b2b-saas-regtech-jsd-hamburg-340171)** en Central Agency for Green Commerce GmbH _(2026-05-07)_ - Arbeitnow
- **[Management Trainee (m/w/d)](https://www.arbeitnow.com/jobs/companies/avs-services-gmbh/management-trainee-berlin-111884)** en AVS Services GmbH _(2026-05-07)_ - Arbeitnow
- **[Junior Influencer & Creator Relations ManagerIn (m/w/d)](https://www.arbeitnow.com/jobs/companies/hey-marly-gmbh/junior-influencer-creator-relations-managerin-cologne-420253)** en Hey Marly GmbH _(2026-05-06)_ - Arbeitnow

<!-- JOBS_END -->

---

## 🛠️ Stack Tecnológico
- Python 3 (`requests`, `beautifulsoup4`)
- GitHub Actions Automation Pipeline 
- Configuraciones parametrizadas vía JSON

## 🤝 Contribuir
Si conoces otras APIs abiertas para empleo Tech Junior, añade una fuente a `config.json` y su correspondiente mapeador a la carpeta `src/scrapers/`. 
_Hecho para la comunidad de Jr Devs._