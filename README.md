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
| Analista de Seguridad de la Información Junior (2) | Ruby (2) |
| Controller (m/w/d) im Öffentlichen Dienst (2) | Data (2) |
| Ejecutivo de Soporte Trainee (2) | Data engineer (2) |
| Technical Project Manager (1) | Automation (1) |
| DevOps Engineer Junior (1) | Angular (1) |

### Frontend

- **[Technical Project Manager](https://www.getonbrd.com/jobs/technical-project-manager-waystone-software-altitude-remote)** en GetOnBoard Company _(2026-03-02)_ - GetOnBoard
- **[DevOps Engineer Junior](https://www.getonbrd.com/jobs/devops-engineer-junior-healthatom-santiago)** en GetOnBoard Company _(2026-02-23)_ - GetOnBoard
- **[Ruby on Rails Developer (Junior / Semi Senior)](https://www.getonbrd.com/jobs/semi-senior-ruby-on-rails-developer-saas-subscriptions-riolab-santiago)** en GetOnBoard Company _(2026-02-17)_ - GetOnBoard
- **[Junior Full-Stack Engineer (Ruby on Rails)](https://www.getonbrd.com/jobs/junior-full-stack-engineer-ruby-on-rails-autoraptor-remote)** en GetOnBoard Company _(2026-01-08)_ - GetOnBoard
- **[Junior Automation Developer (N8n, APIs, JS)](https://www.getonbrd.com/jobs/jjunior-automation-developer-n8n-apis-js-lumago-info-admyo-s-a-de-c-v-remote)** en GetOnBoard Company _(2025-11-29)_ - GetOnBoard
- **[Desarrollador Angular](https://www.getonbrd.com/jobs/desarrollador-angular-defontana-remote-159e)** en GetOnBoard Company _(2025-09-25)_ - GetOnBoard
- **[Shopify Engineer](https://remotive.com/remote-jobs/software-development/shopify-engineer-2088643)** en Nebulab _(2026-03-03)_ - Remotive
- **[Junior Software Entwickler KI-gestützte Webentwicklung (m/w/d)](https://www.arbeitnow.com/jobs/companies/galloverde-gmbh-co-kg/junior-software-entwickler-ki-gestutzte-webentwicklung-dreieich-228042)** en GalloVerde GmbH & Co. KG _(2026-03-13)_ - Arbeitnow
- **[Senior Full-Stack Engineer for Marketing / Growth (m/w/d)](https://www.arbeitnow.com/jobs/companies/accountable/senior-full-stack-engineer-for-marketing-growth-berlin-72962)** en Accountable _(2026-03-13)_ - Arbeitnow
- **[Senior Software Engineer React](https://remoteOK.com/remote-jobs/remote-senior-software-engineer-react-creative-chaos-1130645)** en Creative Chaos _(2026-03-05)_ - RemoteOK

### Backend

- **[Ingeniero Trainee Planta Alimentos Longovilo](https://www.getonbrd.com/jobs/ingeniero-trainee-planta-alimentos-longobilo-agrosuper-melipilla)** en GetOnBoard Company _(2026-03-12)_ - GetOnBoard
- **[Ingeniero Trainee Planta Alimentos la Calera](https://www.getonbrd.com/jobs/ingeniero-trainee-planta-alimentos-la-calera-agrosuper-valparaiso)** en GetOnBoard Company _(2026-03-12)_ - GetOnBoard
- **[Data Engineer (Junior o Mid)](https://www.getonbrd.com/jobs/data-engineer-junior-o-mid-lisit-remote)** en GetOnBoard Company _(2026-03-11)_ - GetOnBoard
- **[Digital Quality Lead](https://www.getonbrd.com/jobs/digital-quality-lead-signant-health-remote)** en GetOnBoard Company _(2026-03-03)_ - GetOnBoard
- **[Ícaro Sales – Trainee Program](https://www.getonbrd.com/jobs/icaro-sales-trainee-program-iconstruye-santiago)** en GetOnBoard Company _(2026-03-11)_ - GetOnBoard
- **[Analista de Analítica Digital](https://www.getonbrd.com/jobs/analista-de-analitica-digital-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-03-05)_ - GetOnBoard
- **[Coordinador(a) Junior de Gobierno de Datos](https://www.getonbrd.com/jobs/coordinador-a-junior-de-gobierno-de-datos-bice-vida-santiago)** en GetOnBoard Company _(2026-02-26)_ - GetOnBoard
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
- **[Junior Backend Software Developer (m/w/d) Java / Kotlin / Spring Boot](https://www.arbeitnow.com/jobs/companies/etalytics-gmbh/junior-backend-software-developer-java-kotlin-spring-boot-darmstadt-408183)** en etalytics GmbH _(2026-03-13)_ - Arbeitnow
- **[Junior Project & Operations Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/fc-viktoria-1889-berlin-frauen-fussball-gmbh/junior-project-operations-manager-berlin-236469)** en FC Viktoria 1889 Berlin Frauen-Fußball GmbH _(2026-03-13)_ - Arbeitnow
- **[Controller (m/w/d) im Öffentlichen Dienst](https://www.arbeitnow.com/jobs/companies/my-humancapital-gmbh/controller-im-offentlichen-dienst-munich-135402)** en MY Humancapital GmbH _(2026-03-13)_ - Arbeitnow
- **[Controller (m/w/d) im Öffentlichen Dienst](https://www.arbeitnow.com/jobs/companies/my-humancapital-gmbh/controller-im-offentlichen-dienst-munich-330811)** en MY Humancapital GmbH _(2026-03-13)_ - Arbeitnow
- **[Jr Social Media Manager](https://remoteOK.com/remote-jobs/remote-jr-social-media-manager-keywords-studios-1130655)** en Keywords Studios _(2026-03-06)_ - RemoteOK
- **[Cloud Architect](https://remoteOK.com/remote-jobs/remote-cloud-architect-accenture-federal-services-1130620)** en Accenture Federal Services _(2026-03-03)_ - RemoteOK

### Mobile

- **[Ingeniero Trainee Planta San Vicente](https://www.getonbrd.com/jobs/ingeniero-trainee-planta-san-vicente-agrosuper-san-vicente)** en GetOnBoard Company _(2026-03-12)_ - GetOnBoard

### QA

- **[Architect/Tech Lead (m/w/x) – Distributed Systems Application Software](https://www.arbeitnow.com/jobs/companies/k-tronik-gmbh/architect-tech-lead-distributed-systems-application-software-munich-348746)** en K-tronik GmbH _(2026-03-13)_ - Arbeitnow

### Other

- **[Ingeniero Trainee Industrial, Plantas Productivas Agrosuper](https://www.getonbrd.com/jobs/ingeniero-trainee-industrial-plantas-faenadoras-agrosuper-rancagua)** en GetOnBoard Company _(2026-03-09)_ - GetOnBoard
- **[Trainee Automatización Industrial (Plc)](https://www.getonbrd.com/jobs/trainee-planta-alimentos-agrosuper-rancagua)** en GetOnBoard Company _(2026-03-09)_ - GetOnBoard
- **[Treasury & Accounting Analyst Junior](https://www.getonbrd.com/jobs/treasury-accounting-analyst-junior-wherex-santiago)** en GetOnBoard Company _(2026-03-05)_ - GetOnBoard
- **[Ejecutivo en Generación de Demanda (Junior)](https://www.getonbrd.com/jobs/ejecutivo-en-generacion-de-demanda-dynamic-devs-santiago-acbd)** en GetOnBoard Company _(2026-03-04)_ - GetOnBoard
- **[Customer Success Executive Junior Técnico B2B/ IoT](https://www.getonbrd.com/jobs/customer-success-executive-junior-tecnico-b2b-iot-guinea-mobile-sac-cuy-movil-lima)** en GetOnBoard Company _(2026-02-10)_ - GetOnBoard
- **[Ejecutivo de Soporte Trainee](https://www.getonbrd.com/jobs/ejecutivo-de-soporte-trainee-agendapro-ciudad-de-mexico)** en GetOnBoard Company _(2026-01-19)_ - GetOnBoard
- **[Ejecutivo de Soporte Trainee](https://www.getonbrd.com/jobs/ejecutivo-de-soporte-trainee-agendapro-santiago)** en GetOnBoard Company _(2025-11-27)_ - GetOnBoard
- **[Teamleitung Buchhaltung | Wachstumsphase](https://www.arbeitnow.com/jobs/companies/matera-gmbh/teamleitung-buchhaltung-wachstumsphase-berlin-172621)** en Matera GmbH _(2026-03-13)_ - Arbeitnow
- **[Team Lead Accounting | Scaling Phase](https://www.arbeitnow.com/jobs/companies/matera-gmbh/team-lead-accounting-scaling-phase-berlin-128623)** en Matera GmbH _(2026-03-13)_ - Arbeitnow
- **[Junior HR Manager (m/w/d) – Schwerpunkt Recruiting](https://www.arbeitnow.com/jobs/companies/my-humancapital-gmbh/junior-hr-manager-schwerpunkt-recruiting-munich-151749)** en MY Humancapital GmbH _(2026-03-13)_ - Arbeitnow

<!-- JOBS_END -->

---

## 🛠️ Stack Tecnológico
- Python 3 (`requests`, `beautifulsoup4`)
- GitHub Actions Automation Pipeline 
- Configuraciones parametrizadas vía JSON

## 🤝 Contribuir
Si conoces otras APIs abiertas para empleo Tech Junior, añade una fuente a `config.json` y su correspondiente mapeador a la carpeta `src/scrapers/`. 
_Hecho para la comunidad de Jr Devs._