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
| Junior Front-end Engineer (1) | Data (1) |
| Ingeniero Junior (1) | Data analyst (1) |
| Ruby on Rails Developer (Junior / Semi Senior) (1) | Qa (1) |

### Frontend

- **[Junior Front-end Engineer](https://www.getonbrd.com/jobs/junior-frontend-engineer-krunchbox-santiago)** en GetOnBoard Company _(2026-04-22)_ - GetOnBoard
- **[Ingeniero Junior](https://www.getonbrd.com/jobs/ingeniero-junior-khipu-remote-e6b1)** en GetOnBoard Company _(2026-04-08)_ - GetOnBoard
- **[AI Engineer](https://www.getonbrd.com/jobs/senior-ai-engineer-mas-analytics-puerto-montt-santiago-puerto-varas)** en GetOnBoard Company _(2026-03-09)_ - GetOnBoard
- **[Ruby on Rails Developer (Junior / Semi Senior)](https://www.getonbrd.com/jobs/semi-senior-ruby-on-rails-developer-saas-subscriptions-riolab-santiago)** en GetOnBoard Company _(2026-02-17)_ - GetOnBoard
- **[Junior Mid Full Stack Software Engineer](https://remoteOK.com/remote-jobs/remote-junior-mid-full-stack-software-engineer-black-canyon-consulting-1131437)** en Black Canyon Consulting _(2026-05-03)_ - RemoteOK
- **[Engineer Software](https://remoteOK.com/remote-jobs/remote-engineer-software-calabrio-1131345)** en Calabrio _(2026-04-27)_ - RemoteOK
- **[Software Engineer](https://remoteOK.com/remote-jobs/remote-software-engineer-finalis-1131328)** en Finalis _(2026-04-26)_ - RemoteOK

### Backend

- **[Ingeniero Junior en Inteligencia Artificial](https://www.getonbrd.com/jobs/ingeniero-junior-en-inteligencia-artificial-bice-vida-santiago)** en GetOnBoard Company _(2026-04-21)_ - GetOnBoard
- **[Business Analyst Junior](https://www.getonbrd.com/jobs/business-analyst-junior-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-04-22)_ - GetOnBoard
- **[Coordinador(a) Junior de Gobierno de Datos](https://www.getonbrd.com/jobs/coordinador-a-junior-de-gobierno-de-datos-bice-vida-santiago)** en GetOnBoard Company _(2026-04-21)_ - GetOnBoard
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
- **[Senior SEA Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/webworks/senior-sea-manager-berlin-99203)** en webworks _(2026-05-05)_ - Arbeitnow
- **[Senior Producer & Projektmanager (m/w/d)](https://www.arbeitnow.com/jobs/companies/yfood-labs-gmbh/senior-producer-projektmanager-munich-71578)** en yfood Labs GmbH _(2026-05-05)_ - Arbeitnow
- **[Legal Data Analyst Junior Vaga Afirmativa para PCD](https://remoteOK.com/remote-jobs/remote-legal-data-analyst-junior-vaga-afirmativa-para-pcd-jusbrasil-1131393)** en Jusbrasil _(2026-04-30)_ - RemoteOK
- **[Lite Controller Pathfinder Hospitality](https://remoteOK.com/remote-jobs/remote-lite-controller-pathfinder-hospitality-pathfinder-hospitality-1131385)** en Pathfinder Hospitality _(2026-04-29)_ - RemoteOK

### Mobile

- **[DevOps Junior (Latam )](https://www.getonbrd.com/jobs/devops-jr-remoto-latam-i2b-technologies-remote)** en GetOnBoard Company _(2026-04-28)_ - GetOnBoard
- **[Salesforce Technical Consultant (Field Service)](https://www.getonbrd.com/jobs/salesforce-technical-consultant-field-service-niuro-remote)** en GetOnBoard Company _(2026-03-26)_ - GetOnBoard
- **[Operations Manager (m/w/d) Healthcare | Backoffice & Administration](https://www.arbeitnow.com/jobs/companies/dhg-deutsche-horakustik-gmbh/operations-manager-healthcare-backoffice-administration-berlin-9809)** en DHG Deutsche Hörakustik GmbH _(2026-05-04)_ - Arbeitnow

### Data

- **[SAP Fico Functional Consultant](https://www.getonbrd.com/jobs/sap-fico-functional-consultant-crest-it-resources-llc-remote)** en GetOnBoard Company _(2026-04-29)_ - GetOnBoard
- **[Soporte Operativo Junior](https://www.getonbrd.com/jobs/soporte-operativo-junior-bc-tecnologia-remote)** en GetOnBoard Company _(2026-03-31)_ - GetOnBoard
- **[Senior IT Service Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/noris-network-ag/senior-it-service-manager-nuremberg-322242)** en noris network AG _(2026-05-05)_ - Arbeitnow
- **[Junior IT Service Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/noris-network-ag/junior-it-service-manager-nuremberg-145559)** en noris network AG _(2026-05-05)_ - Arbeitnow
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
- **[Sales & Business Development Trainee (B2B Finanzmentoring) - Remote - Vollzeit/ Teilzeit (m/w/d)](https://www.arbeitnow.com/jobs/companies/helmutbeckcom-by-mhb-consulting-gmbh/sales-business-development-trainee-b2b-finanzmentoring-remote-vollzeit-teilzeit-frankfurt-am-main-131637)** en helmutbeck.com - by MHB Consulting GmbH _(2026-05-05)_ - Arbeitnow
- **[International Expansion Manager - Conversion & Growth 100% (m/w/d)](https://www.arbeitnow.com/jobs/companies/sheko-gmbh/international-expansion-manager-conversion-growth-100-hamburg-224087)** en SHEKO GmbH _(2026-05-05)_ - Arbeitnow
- **[Junior Buchhalter (m/w/d)](https://www.arbeitnow.com/jobs/companies/fels-trader-gmbh/junior-buchhalter-kelkheim-153726)** en FELS trader GmbH _(2026-05-05)_ - Arbeitnow

<!-- JOBS_END -->

---

## 🛠️ Stack Tecnológico
- Python 3 (`requests`, `beautifulsoup4`)
- GitHub Actions Automation Pipeline 
- Configuraciones parametrizadas vía JSON

## 🤝 Contribuir
Si conoces otras APIs abiertas para empleo Tech Junior, añade una fuente a `config.json` y su correspondiente mapeador a la carpeta `src/scrapers/`. 
_Hecho para la comunidad de Jr Devs._