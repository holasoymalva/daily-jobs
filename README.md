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
### Frontend

- **[Technical Project Manager](https://www.getonbrd.com/jobs/technical-project-manager-waystone-software-altitude-remote)** en GetOnBoard Company _(2026-03-02)_ - GetOnBoard
- **[Desarrollador Junior IA para Incubadora de Software](https://www.getonbrd.com/jobs/desarrollador-junior-ia-para-incubadora-de-software-construckit-santiago)** en GetOnBoard Company _(2026-03-05)_ - GetOnBoard
- **[DevOps Engineer Junior](https://www.getonbrd.com/jobs/devops-engineer-junior-healthatom-santiago)** en GetOnBoard Company _(2026-02-23)_ - GetOnBoard
- **[Front-end UI Developer (Junior / Mid)](https://www.getonbrd.com/jobs/frontend-ui-developer-junior-mid-i2b-technologies-remote)** en GetOnBoard Company _(2026-02-19)_ - GetOnBoard
- **[Ruby on Rails Developer (Junior / Semi Senior)](https://www.getonbrd.com/jobs/semi-senior-ruby-on-rails-developer-saas-subscriptions-riolab-santiago)** en GetOnBoard Company _(2026-02-17)_ - GetOnBoard
- **[Junior Full-Stack Engineer (Ruby on Rails)](https://www.getonbrd.com/jobs/junior-full-stack-engineer-ruby-on-rails-autoraptor-remote)** en GetOnBoard Company _(2026-01-08)_ - GetOnBoard
- **[Junior Automation Developer (N8n, APIs, JS)](https://www.getonbrd.com/jobs/jjunior-automation-developer-n8n-apis-js-lumago-info-admyo-s-a-de-c-v-remote)** en GetOnBoard Company _(2025-11-28)_ - GetOnBoard
- **[Desarrollador Angular](https://www.getonbrd.com/jobs/desarrollador-angular-defontana-remote-159e)** en GetOnBoard Company _(2025-09-25)_ - GetOnBoard
- **[Shopify Engineer](https://remotive.com/remote-jobs/software-development/shopify-engineer-2088643)** en Nebulab _(2026-03-03)_ - Remotive
- **[UX/ UI Designer (m/w/d), Vollzeit](https://www.arbeitnow.com/jobs/companies/atharicommerce/ux-ui-designer-vollzeit-cologne-247158)** en AthariCommerce _(2026-03-09)_ - Arbeitnow
- **[Senior Software Engineer React](https://remoteOK.com/remote-jobs/remote-senior-software-engineer-react-creative-chaos-1130645)** en Creative Chaos _(2026-03-05)_ - RemoteOK

### Backend

- **[Digital Quality Lead](https://www.getonbrd.com/jobs/digital-quality-lead-signant-health-remote)** en GetOnBoard Company _(2026-03-03)_ - GetOnBoard
- **[Coordinador(a) Junior de Gobierno de Datos](https://www.getonbrd.com/jobs/coordinador-a-junior-de-gobierno-de-datos-bice-vida-santiago)** en GetOnBoard Company _(2026-02-26)_ - GetOnBoard
- **[Desarrollador Junior](https://www.getonbrd.com/jobs/desarrollador-junior-ser-q-santiago)** en GetOnBoard Company _(2026-02-25)_ - GetOnBoard
- **[Analista de Analítica Digital](https://www.getonbrd.com/jobs/analista-de-analitica-digital-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-03-05)_ - GetOnBoard
- **[SRE / DevOps Engineer Junior](https://www.getonbrd.com/jobs/sre-devops-engineer-junior-bc-tecnologia-remote)** en GetOnBoard Company _(2026-02-24)_ - GetOnBoard
- **[Lead Cloud Data Engineer](https://www.getonbrd.com/jobs/lead-cloud-data-engineer-signant-health-remote)** en GetOnBoard Company _(2026-02-09)_ - GetOnBoard
- **[Asesor Educativo Comercial Junior](https://www.getonbrd.com/jobs/asesor-educativo-comercial-junior-colectivo23-lima)** en GetOnBoard Company _(2026-02-02)_ - GetOnBoard
- **[Software Engineer Back-end Developer Junior](https://www.getonbrd.com/jobs/software-engineer-back-end-developer-junior-2brains-remote)** en GetOnBoard Company _(2026-01-23)_ - GetOnBoard
- **[Jr Sales Executive](https://www.getonbrd.com/jobs/jr-sales-executive-coderslab-io-ciudad-de-mexico)** en GetOnBoard Company _(2026-01-21)_ - GetOnBoard
- **[Ingeniero(a) Junior de Software y Robótica](https://www.getonbrd.com/jobs/ingeniero-a-junior-de-software-y-robotica-maquintel-robotic-services-santiago)** en GetOnBoard Company _(2026-01-19)_ - GetOnBoard
- **[Analista de Seguridad de la Información Junior](https://www.getonbrd.com/jobs/analista-de-seguridad-de-la-informacion-junior-bc-tecnologia-santiago-bb38)** en GetOnBoard Company _(2026-01-16)_ - GetOnBoard
- **[Ingeniero Trainee Industrial](https://www.getonbrd.com/jobs/ingeniero-trainee-industrial-agrosuper-rancagua)** en GetOnBoard Company _(2025-12-29)_ - GetOnBoard
- **[Analista de Seguridad de la Información Junior](https://www.getonbrd.com/jobs/analista-de-seguridad-de-la-informacion-junior-bc-tecnologia-santiago)** en GetOnBoard Company _(2025-12-22)_ - GetOnBoard
- **[Inside Sales Contractor](https://remotive.com/remote-jobs/sales-business/inside-sales-contractor-2086540)** en Credit Wellness, LLC _(2026-03-08)_ - Remotive
- **[Junior Enterprise Service Management Expert (m/w/d)](https://www.arbeitnow.com/jobs/companies/labtagon-gmbh/junior-enterprise-service-management-expert-monchengladbach-297135)** en Labtagon GmbH _(2026-03-09)_ - Arbeitnow
- **[Jr Social Media Manager](https://remoteOK.com/remote-jobs/remote-jr-social-media-manager-keywords-studios-1130655)** en Keywords Studios _(2026-03-06)_ - RemoteOK
- **[Cloud Architect](https://remoteOK.com/remote-jobs/remote-cloud-architect-accenture-federal-services-1130620)** en Accenture Federal Services _(2026-03-03)_ - RemoteOK

### Mobile

- **[Junior Ticketing Marketing Manager (d/w/m) I DACH](https://www.arbeitnow.com/jobs/companies/hyrox-world-gmbh/junior-ticketing-marketing-manager-i-dach-hamburg-356221)** en HYROX World GmbH _(2026-03-09)_ - Arbeitnow
- **[Crypto Market Operations Trainee](https://remoteOK.com/remote-jobs/remote-crypto-market-operations-trainee-begini-1130604)** en Begini _(2026-03-03)_ - RemoteOK
- **[Junior Live Ops Game Designer](https://remoteOK.com/remote-jobs/remote-junior-live-ops-game-designer-a-thinking-ape-1130577)** en A Thinking Ape _(2026-02-28)_ - RemoteOK

### Data

- **[Berufseinsteiger / Junior Softwareentwickler (m/w/d) herzlich willkommen](https://www.arbeitnow.com/jobs/companies/intercon-solutions-gmbh/berufseinsteiger-junior-softwareentwickler-herzlich-willkommen-munich-473378)** en Intercon Solutions GmbH _(2026-03-09)_ - Arbeitnow

### QA

- **[Head of Technology & AI (m/w/d)](https://www.arbeitnow.com/jobs/companies/webmatch-gmbh/head-of-technology-ai-cologne-63724)** en Webmatch GmbH _(2026-03-09)_ - Arbeitnow

### Other

- **[Ingeniero Trainee Industrial, Plantas Productivas Agrosuper](https://www.getonbrd.com/jobs/ingeniero-trainee-industrial-plantas-faenadoras-agrosuper-rancagua)** en GetOnBoard Company _(2026-03-09)_ - GetOnBoard
- **[Trainee Automatización Industrial (Plc)](https://www.getonbrd.com/jobs/trainee-planta-alimentos-agrosuper-rancagua)** en GetOnBoard Company _(2026-03-09)_ - GetOnBoard
- **[Treasury & Accounting Analyst Junior](https://www.getonbrd.com/jobs/treasury-accounting-analyst-junior-wherex-santiago)** en GetOnBoard Company _(2026-03-05)_ - GetOnBoard
- **[Ejecutivo en Generación de Demanda (Junior)](https://www.getonbrd.com/jobs/ejecutivo-en-generacion-de-demanda-dynamic-devs-santiago-acbd)** en GetOnBoard Company _(2026-03-04)_ - GetOnBoard
- **[Customer Success Executive Junior Técnico B2B/ IoT](https://www.getonbrd.com/jobs/customer-success-executive-junior-tecnico-b2b-iot-guinea-mobile-sac-cuy-movil-lima)** en GetOnBoard Company _(2026-02-09)_ - GetOnBoard
- **[Ejecutivo de Soporte Trainee](https://www.getonbrd.com/jobs/ejecutivo-de-soporte-trainee-agendapro-ciudad-de-mexico)** en GetOnBoard Company _(2026-01-19)_ - GetOnBoard
- **[Ejecutivo de Soporte Trainee](https://www.getonbrd.com/jobs/ejecutivo-de-soporte-trainee-agendapro-santiago)** en GetOnBoard Company _(2025-11-27)_ - GetOnBoard
- **[Junior Assistant Sales & Partnerships (m/w/d) Full Remote](https://www.arbeitnow.com/jobs/companies/jbconsulting/junior-assistant-sales-partnerships-full-remote-grunkraut-265190)** en JBConsulting _(2026-03-09)_ - Arbeitnow
- **[Teamleitung Buchhaltung | Wachstumsphase](https://www.arbeitnow.com/jobs/companies/matera-gmbh/teamleitung-buchhaltung-wachstumsphase-berlin-249511)** en Matera GmbH _(2026-03-09)_ - Arbeitnow
- **[Team Lead Accounting | Scaling Phase](https://www.arbeitnow.com/jobs/companies/matera-gmbh/team-lead-accounting-scaling-phase-berlin-373604)** en Matera GmbH _(2026-03-09)_ - Arbeitnow

<!-- JOBS_END -->

---

## 🛠️ Stack Tecnológico
- Python 3 (`requests`, `beautifulsoup4`)
- GitHub Actions Automation Pipeline 
- Configuraciones parametrizadas vía JSON

## 🤝 Contribuir
Si conoces otras APIs abiertas para empleo Tech Junior, añade una fuente a `config.json` y su correspondiente mapeador a la carpeta `src/scrapers/`. 
_Hecho para la comunidad de Jr Devs._