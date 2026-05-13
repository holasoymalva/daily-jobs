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
| AI Engineer (2) | Ruby (1) |
| Business Analyst Junior (2) | Data engineer (1) |
| Analista de Seguridad de la Información Junior (2) | Data (1) |
| Desarrollador Junior (1) | Machine learning (1) |
| Ingeniero Junior (1) | Qa (1) |

### Frontend

- **[Desarrollador Junior](https://www.getonbrd.com/jobs/desarrollador-junior-vti-uchile-santiago-8a40)** en GetOnBoard Company _(2026-05-07)_ - GetOnBoard
- **[Ingeniero Junior](https://www.getonbrd.com/jobs/ingeniero-junior-khipu-remote-e6b1)** en GetOnBoard Company _(2026-04-08)_ - GetOnBoard
- **[AI Engineer](https://www.getonbrd.com/jobs/senior-ai-engineer-mas-analytics-puerto-montt-santiago-puerto-varas)** en GetOnBoard Company _(2026-03-09)_ - GetOnBoard
- **[Ruby on Rails Developer (Junior / Semi Senior)](https://www.getonbrd.com/jobs/semi-senior-ruby-on-rails-developer-saas-subscriptions-riolab-santiago)** en GetOnBoard Company _(2026-02-17)_ - GetOnBoard
- **[Lead Software Engineer](https://remoteOK.com/remote-jobs/remote-lead-software-engineer-csc-generation-1131529)** en CSC Generation _(2026-05-09)_ - RemoteOK

### Backend

- **[Ejecutivo de Onboarding Junior](https://www.getonbrd.com/jobs/ejecutivo-de-onboarding-trainee-agendapro-santiago-daf4)** en GetOnBoard Company _(2026-05-08)_ - GetOnBoard
- **[Ingeniero de Datos](https://www.getonbrd.com/jobs/ingeniero-de-datos-senior-foris-ai-remote)** en GetOnBoard Company _(2026-05-07)_ - GetOnBoard
- **[Analista de Proyectos TI y Automatización](https://www.getonbrd.com/jobs/analista-de-proyectos-ti-y-automatizacion-tcit-santiago-e09d)** en GetOnBoard Company _(2026-05-06)_ - GetOnBoard
- **[UX Junior](https://www.getonbrd.com/jobs/ux-junior-tcit-santiago-ac7c)** en GetOnBoard Company _(2026-04-24)_ - GetOnBoard
- **[Business Analyst Junior](https://www.getonbrd.com/jobs/business-analyst-junior-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-04-22)_ - GetOnBoard
- **[Ingeniero Junior en Inteligencia Artificial](https://www.getonbrd.com/jobs/ingeniero-junior-en-inteligencia-artificial-bice-vida-santiago)** en GetOnBoard Company _(2026-04-21)_ - GetOnBoard
- **[Data Engineer Senior](https://www.getonbrd.com/jobs/data-engineer-senior-grupo-mariposa-remote-ba30)** en GetOnBoard Company _(2026-04-15)_ - GetOnBoard
- **[Product Owner Junior](https://www.getonbrd.com/jobs/product-owner-junior-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-04-15)_ - GetOnBoard
- **[Ingeniero/a de Machine Learning Junior](https://www.getonbrd.com/jobs/ingeniero-a-de-machine-learning-suncast-remote)** en GetOnBoard Company _(2026-03-19)_ - GetOnBoard
- **[Analista de Analítica Digital](https://www.getonbrd.com/jobs/analista-de-analitica-digital-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-03-05)_ - GetOnBoard
- **[Digital Quality Lead](https://www.getonbrd.com/jobs/digital-quality-lead-signant-health-remote)** en GetOnBoard Company _(2026-03-03)_ - GetOnBoard
- **[SRE / DevOps Engineer Junior](https://www.getonbrd.com/jobs/sre-devops-engineer-junior-bc-tecnologia-remote)** en GetOnBoard Company _(2026-02-24)_ - GetOnBoard
- **[Asesor de Contactabilidad Junior](https://www.getonbrd.com/jobs/asesor-educativo-comercial-junior-colectivo23-lima)** en GetOnBoard Company _(2026-02-02)_ - GetOnBoard
- **[Jr Sales Executive](https://www.getonbrd.com/jobs/jr-sales-executive-coderslab-io-ciudad-de-mexico)** en GetOnBoard Company _(2026-01-21)_ - GetOnBoard
- **[Ingeniero(a) Junior de Software y Robótica](https://www.getonbrd.com/jobs/ingeniero-a-junior-de-software-y-robotica-maquintel-robotic-services-santiago)** en GetOnBoard Company _(2026-01-19)_ - GetOnBoard
- **[Analista de Seguridad de la Información Junior](https://www.getonbrd.com/jobs/analista-de-seguridad-de-la-informacion-junior-bc-tecnologia-santiago-bb38)** en GetOnBoard Company _(2026-01-16)_ - GetOnBoard
- **[Analista de Seguridad de la Información Junior](https://www.getonbrd.com/jobs/analista-de-seguridad-de-la-informacion-junior-bc-tecnologia-santiago)** en GetOnBoard Company _(2025-12-22)_ - GetOnBoard
- **[Inside Sales Contractor](https://remotive.com/remote-jobs/sales/inside-sales-contractor-2086540)** en Credit Wellness, LLC _(2026-05-08)_ - Remotive
- **[AI Engineer](https://remotive.com/remote-jobs/artificial-intelligence/ai-engineer-2089958)** en Dry Ground AI _(2026-04-21)_ - Remotive
- **[Junior IT-Systemadministrator (w/m/d) - inhouse - German C1+](https://www.arbeitnow.com/jobs/companies/trigon-gruppe-gmbh/junior-it-systemadministrator-inhouse-german-c1-berlin-388670)** en Trigon Gruppe GmbH _(2026-05-13)_ - Arbeitnow
- **[Junior SEA Manager im Online-Marketing (m/w/d) in Berlin](https://www.arbeitnow.com/jobs/companies/suchmeisterei-gmbh/junior-sea-manager-im-online-marketing-in-berlin-85078)** en SUCHMEISTEREI GmbH _(2026-05-13)_ - Arbeitnow
- **[Junior Personalberater (m/f/d) - Düsseldorf](https://www.arbeitnow.com/jobs/companies/talentfluss/junior-personalberater-dusseldorf-202247)** en talentfluss _(2026-05-13)_ - Arbeitnow
- **[Manager Collections &amp; Recoveries](https://remoteOK.com/remote-jobs/remote-manager-collections-amp-recoveries-forbright-bank-1131526)** en Forbright Bank _(2026-05-09)_ - RemoteOK
- **[UI Developer](https://remoteOK.com/remote-jobs/remote-ui-developer-rainfocus-1131473)** en RainFocus _(2026-05-05)_ - RemoteOK

### Mobile

- **[DevOps Junior (Latam )](https://www.getonbrd.com/jobs/devops-jr-remoto-latam-i2b-technologies-remote)** en GetOnBoard Company _(2026-04-28)_ - GetOnBoard
- **[Amazon Advertising Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/adsmasters-gmbh/amazon-advertising-manager-dusseldorf-194406)** en Adsmasters GmbH _(2026-05-13)_ - Arbeitnow

### Data

- **[SAP Fico Functional Consultant](https://www.getonbrd.com/jobs/sap-fico-functional-consultant-crest-it-resources-llc-remote)** en GetOnBoard Company _(2026-04-29)_ - GetOnBoard
- **[Soporte Operativo Junior](https://www.getonbrd.com/jobs/soporte-operativo-junior-bc-tecnologia-remote)** en GetOnBoard Company _(2026-03-31)_ - GetOnBoard
- **[Business Analyst Junior](https://www.getonbrd.com/jobs/business-analyst-junior-apside-santiago)** en GetOnBoard Company _(2026-02-05)_ - GetOnBoard
- **[Online Hospitality Services Coordinator Entry Level](https://remoteOK.com/remote-jobs/remote-online-hospitality-services-coordinator-entry-level-aisles-amp-abroad-1131534)** en Aisles &amp; Abroad _(2026-05-10)_ - RemoteOK

### QA

- **[Developer QA – Junior](https://www.getonbrd.com/jobs/developer-qa-junior-ameris-capital-santiago)** en GetOnBoard Company _(2026-04-07)_ - GetOnBoard

### Other

- **[Ejecutivo en Generación de Demanda (Junior)](https://www.getonbrd.com/jobs/ejecutivo-en-generacion-de-demanda-dynamic-devs-santiago-acbd)** en GetOnBoard Company _(2026-04-29)_ - GetOnBoard
- **[Auxiliar de Operaciones Jr](https://www.getonbrd.com/jobs/auxiliar-de-operaciones-jr-coderslab-io-lima)** en GetOnBoard Company _(2026-04-17)_ - GetOnBoard
- **[Junior Network Engineer (Presencial)](https://www.getonbrd.com/jobs/networking-presencial-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-04-02)_ - GetOnBoard
- **[Ejecutiva de Cuenta Marketing Junior](https://www.getonbrd.com/jobs/ejecutiva-de-cuenta-match-agencia-consultora-remote)** en GetOnBoard Company _(2026-03-18)_ - GetOnBoard
- **[Customer Success Executive Junior Técnico B2B/ IoT](https://www.getonbrd.com/jobs/customer-success-executive-junior-tecnico-b2b-iot-guinea-mobile-sac-cuy-movil-lima)** en GetOnBoard Company _(2026-02-10)_ - GetOnBoard
- **[Ejecutivo de Soporte Trainee](https://www.getonbrd.com/jobs/ejecutivo-de-soporte-trainee-agendapro-ciudad-de-mexico)** en GetOnBoard Company _(2026-01-19)_ - GetOnBoard
- **[Werkstudent Vertrieb / Finanzberatung (m/w/d) – Praxis statt Theorie](https://www.arbeitnow.com/jobs/companies/shereen-patzelt/werkstudent-vertrieb-finanzberatung-praxis-statt-theorie-chemnitz-29242)** en Shereen Patzelt _(2026-05-13)_ - Arbeitnow
- **[PR Manager (m/w/d) – Remote oder Berlin](https://www.arbeitnow.com/jobs/companies/getpress/pr-manager-remote-oder-berlin-175658)** en getpress _(2026-05-13)_ - Arbeitnow
- **[(Junior) Content & AI Creative (m/w/d)](https://www.arbeitnow.com/jobs/companies/lowenzahn-organics-gmbh/junior-content-ai-creative-mainz-433349)** en Löwenzahn Organics GmbH _(2026-05-13)_ - Arbeitnow
- **[Werkstudent (m/w/d) – Finance & Beratung (unternehmerisch, leistungsbasiert)](https://www.arbeitnow.com/jobs/companies/kevin-kehr/werkstudent-finance-beratung-unternehmerisch-leistungsbasiert-hamburg-471393)** en Kevin Kehr _(2026-05-13)_ - Arbeitnow
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