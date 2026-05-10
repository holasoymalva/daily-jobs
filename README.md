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
| Desarrollador Junior (1) | Automation (1) |
| Junior Front-end Engineer (1) | Typescript (1) |
| Ingeniero Junior (1) | Node (1) |

### Frontend

- **[Desarrollador Junior](https://www.getonbrd.com/jobs/desarrollador-junior-vti-uchile-santiago-8a40)** en GetOnBoard Company _(2026-05-07)_ - GetOnBoard
- **[Junior Front-end Engineer](https://www.getonbrd.com/jobs/junior-frontend-engineer-krunchbox-santiago)** en GetOnBoard Company _(2026-04-22)_ - GetOnBoard
- **[Ingeniero Junior](https://www.getonbrd.com/jobs/ingeniero-junior-khipu-remote-e6b1)** en GetOnBoard Company _(2026-04-08)_ - GetOnBoard
- **[AI Engineer](https://www.getonbrd.com/jobs/senior-ai-engineer-mas-analytics-puerto-montt-santiago-puerto-varas)** en GetOnBoard Company _(2026-03-09)_ - GetOnBoard
- **[Ruby on Rails Developer (Junior / Semi Senior)](https://www.getonbrd.com/jobs/semi-senior-ruby-on-rails-developer-saas-subscriptions-riolab-santiago)** en GetOnBoard Company _(2026-02-17)_ - GetOnBoard
- **[Junior Business Automation Manager (m/w/d) – Schwerpunkt KI & Prozessoptimierung](https://www.arbeitnow.com/jobs/companies/sportstech-brands-holding-gmbh/junior-business-automation-manager-schwerpunkt-ki-prozessoptimierung-berlin-440183)** en Sportstech Brands Holding GmbH _(2026-05-09)_ - Arbeitnow
- **[Senior Software Engineer (TypeScript, NestJS/Node.js) (m/f/x)](https://www.arbeitnow.com/jobs/companies/atolls/senior-software-engineer-typescript-nestjs-nodejs-berlin-82074)** en Atolls _(2026-05-08)_ - Arbeitnow
- **[Lead Software Engineer](https://remoteOK.com/remote-jobs/remote-lead-software-engineer-csc-generation-1131529)** en CSC Generation _(2026-05-09)_ - RemoteOK
- **[Junior Mid Full Stack Software Engineer](https://remoteOK.com/remote-jobs/remote-junior-mid-full-stack-software-engineer-black-canyon-consulting-1131437)** en Black Canyon Consulting _(2026-05-03)_ - RemoteOK

### Backend

- **[Ejecutivo de Onboarding Junior](https://www.getonbrd.com/jobs/ejecutivo-de-onboarding-trainee-agendapro-santiago-daf4)** en GetOnBoard Company _(2026-05-08)_ - GetOnBoard
- **[Ingeniero de Datos](https://www.getonbrd.com/jobs/ingeniero-de-datos-senior-foris-ai-remote)** en GetOnBoard Company _(2026-05-07)_ - GetOnBoard
- **[Analista de Proyectos TI y Automatización](https://www.getonbrd.com/jobs/analista-de-proyectos-ti-y-automatizacion-tcit-santiago-e09d)** en GetOnBoard Company _(2026-05-06)_ - GetOnBoard
- **[Business Analyst Junior](https://www.getonbrd.com/jobs/business-analyst-junior-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-04-22)_ - GetOnBoard
- **[Ingeniero Junior en Inteligencia Artificial](https://www.getonbrd.com/jobs/ingeniero-junior-en-inteligencia-artificial-bice-vida-santiago)** en GetOnBoard Company _(2026-04-21)_ - GetOnBoard
- **[Data Engineer Senior](https://www.getonbrd.com/jobs/data-engineer-senior-grupo-mariposa-remote-ba30)** en GetOnBoard Company _(2026-04-15)_ - GetOnBoard
- **[Product Owner Junior](https://www.getonbrd.com/jobs/product-owner-junior-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-04-15)_ - GetOnBoard
- **[Junior Growth Marketer (AI & Cloud Native)](https://www.getonbrd.com/jobs/senior-digital-marketing-growth-lead-ai-design-b2b-e-omnix-ai-corp-remote)** en GetOnBoard Company _(2026-03-26)_ - GetOnBoard
- **[Ingeniero/a de Machine Learning Junior](https://www.getonbrd.com/jobs/ingeniero-a-de-machine-learning-suncast-remote)** en GetOnBoard Company _(2026-03-19)_ - GetOnBoard
- **[Analista de Analítica Digital](https://www.getonbrd.com/jobs/analista-de-analitica-digital-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-03-05)_ - GetOnBoard
- **[Digital Quality Lead](https://www.getonbrd.com/jobs/digital-quality-lead-signant-health-remote)** en GetOnBoard Company _(2026-03-03)_ - GetOnBoard
- **[SRE / DevOps Engineer Junior](https://www.getonbrd.com/jobs/sre-devops-engineer-junior-bc-tecnologia-remote)** en GetOnBoard Company _(2026-02-24)_ - GetOnBoard
- **[Asesor de Contactabilidad Junior](https://www.getonbrd.com/jobs/asesor-educativo-comercial-junior-colectivo23-lima)** en GetOnBoard Company _(2026-02-02)_ - GetOnBoard
- **[Jr Sales Executive](https://www.getonbrd.com/jobs/jr-sales-executive-coderslab-io-ciudad-de-mexico)** en GetOnBoard Company _(2026-01-21)_ - GetOnBoard
- **[Ingeniero(a) Junior de Software y Robótica](https://www.getonbrd.com/jobs/ingeniero-a-junior-de-software-y-robotica-maquintel-robotic-services-santiago)** en GetOnBoard Company _(2026-01-19)_ - GetOnBoard
- **[Analista de Seguridad de la Información Junior](https://www.getonbrd.com/jobs/analista-de-seguridad-de-la-informacion-junior-bc-tecnologia-santiago-bb38)** en GetOnBoard Company _(2026-01-16)_ - GetOnBoard
- **[Analista de Seguridad de la Información Junior](https://www.getonbrd.com/jobs/analista-de-seguridad-de-la-informacion-junior-bc-tecnologia-santiago)** en GetOnBoard Company _(2025-12-22)_ - GetOnBoard
- **[AI Engineer](https://remotive.com/remote-jobs/artificial-intelligence/ai-engineer-2089958)** en Dry Ground AI _(2026-04-21)_ - Remotive
- **[Junior Consultant Operational AI / AI Engineering (m/w/d)](https://www.arbeitnow.com/jobs/companies/neurawork-gmbh-co-kg/junior-consultant-operational-ai-ai-engineering-ampfing-363384)** en Neurawork GmbH & Co. KG _(2026-05-09)_ - Arbeitnow
- **[Manager Collections &amp; Recoveries](https://remoteOK.com/remote-jobs/remote-manager-collections-amp-recoveries-forbright-bank-1131526)** en Forbright Bank _(2026-05-09)_ - RemoteOK
- **[UI Developer](https://remoteOK.com/remote-jobs/remote-ui-developer-rainfocus-1131473)** en RainFocus _(2026-05-05)_ - RemoteOK

### Mobile

- **[DevOps Junior (Latam )](https://www.getonbrd.com/jobs/devops-jr-remoto-latam-i2b-technologies-remote)** en GetOnBoard Company _(2026-04-28)_ - GetOnBoard

### Data

- **[SAP Fico Functional Consultant](https://www.getonbrd.com/jobs/sap-fico-functional-consultant-crest-it-resources-llc-remote)** en GetOnBoard Company _(2026-04-29)_ - GetOnBoard
- **[Soporte Operativo Junior](https://www.getonbrd.com/jobs/soporte-operativo-junior-bc-tecnologia-remote)** en GetOnBoard Company _(2026-03-31)_ - GetOnBoard

### QA

- **[Developer QA – Junior](https://www.getonbrd.com/jobs/developer-qa-junior-ameris-capital-santiago)** en GetOnBoard Company _(2026-04-07)_ - GetOnBoard

### Other

- **[Ejecutivo en Generación de Demanda (Junior)](https://www.getonbrd.com/jobs/ejecutivo-en-generacion-de-demanda-dynamic-devs-santiago-acbd)** en GetOnBoard Company _(2026-04-29)_ - GetOnBoard
- **[Auxiliar de Operaciones Jr](https://www.getonbrd.com/jobs/auxiliar-de-operaciones-jr-coderslab-io-lima)** en GetOnBoard Company _(2026-04-17)_ - GetOnBoard
- **[Junior Network Engineer (Presencial)](https://www.getonbrd.com/jobs/networking-presencial-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-04-02)_ - GetOnBoard
- **[Ejecutiva de Cuenta Marketing Junior](https://www.getonbrd.com/jobs/ejecutiva-de-cuenta-match-agencia-consultora-remote)** en GetOnBoard Company _(2026-03-18)_ - GetOnBoard
- **[Customer Success Executive Junior Técnico B2B/ IoT](https://www.getonbrd.com/jobs/customer-success-executive-junior-tecnico-b2b-iot-guinea-mobile-sac-cuy-movil-lima)** en GetOnBoard Company _(2026-02-10)_ - GetOnBoard
- **[Ejecutivo de Soporte Trainee](https://www.getonbrd.com/jobs/ejecutivo-de-soporte-trainee-agendapro-ciudad-de-mexico)** en GetOnBoard Company _(2026-01-19)_ - GetOnBoard
- **[ART DIRECTOR / SENIOR ART DIRECTOR (M/W/D)](https://www.arbeitnow.com/jobs/companies/dyadic-gmbh/art-director-senior-art-director-furth-428204)** en DYADIC GmbH _(2026-05-09)_ - Arbeitnow
- **[(Junior) HR Manager (m/w/d) - Schwerpunkt Recruiting](https://www.arbeitnow.com/jobs/companies/my-humancapital-gmbh/junior-hr-manager-schwerpunkt-recruiting-munich-125313)** en MY Humancapital GmbH _(2026-05-08)_ - Arbeitnow
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