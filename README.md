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
| Analista de Seguridad de la Información Junior (2) | Typescript (1) |
| Junior DevOps Engineer (m/f/d) (2) | Javascript (1) |
| Ejecutivo de Soporte Trainee (2) | Java (1) |
| Desarrollador Full-Stack JavaScript/TypeScript Junior (1) | Ruby (1) |
| AI Engineer (1) | Angular (1) |

### Frontend

- **[Desarrollador Full-Stack JavaScript/TypeScript Junior](https://www.getonbrd.com/jobs/desarrollador-full-stack-javascript-typescript-junior-tcit-santiago)** en GetOnBoard Company _(2026-03-18)_ - GetOnBoard
- **[AI Engineer](https://www.getonbrd.com/jobs/senior-ai-engineer-mas-analytics-puerto-montt-santiago-puerto-varas)** en GetOnBoard Company _(2026-03-09)_ - GetOnBoard
- **[Ruby on Rails Developer (Junior / Semi Senior)](https://www.getonbrd.com/jobs/semi-senior-ruby-on-rails-developer-saas-subscriptions-riolab-santiago)** en GetOnBoard Company _(2026-02-17)_ - GetOnBoard
- **[Desarrollador Angular](https://www.getonbrd.com/jobs/desarrollador-angular-defontana-remote-159e)** en GetOnBoard Company _(2025-09-25)_ - GetOnBoard
- **[Junior Project Coordinator](https://remotive.com/remote-jobs/project-management/junior-project-coordinator-2088663)** en C4Media Inc. _(2026-03-24)_ - Remotive
- **[Shopify Engineer](https://remotive.com/remote-jobs/software-development/shopify-engineer-2088643)** en Nebulab _(2026-03-03)_ - Remotive
- **[Senior Developer Backend Search CD+E](https://remoteOK.com/remote-jobs/remote-senior-developer-backend-search-cd-e-ubiminds-1130881)** en Ubiminds _(2026-03-26)_ - RemoteOK

### Backend

- **[Analista de Proyectos TI y Automatización](https://www.getonbrd.com/jobs/analista-de-proyectos-ti-y-automatizacion-tcit-santiago)** en GetOnBoard Company _(2026-03-30)_ - GetOnBoard
- **[Junior Growth Marketer (AI & Cloud Native)](https://www.getonbrd.com/jobs/senior-digital-marketing-growth-lead-ai-design-b2b-e-omnix-ai-corp-remote)** en GetOnBoard Company _(2026-03-26)_ - GetOnBoard
- **[Data Engineer Senior](https://www.getonbrd.com/jobs/data-engineer-senior-grupo-mariposa-remote)** en GetOnBoard Company _(2026-03-30)_ - GetOnBoard
- **[Ingeniero Agrónomo Trainee Producción Cerdos](https://www.getonbrd.com/jobs/ingeniero-agronomo-trainee-produccion-cerdos-agrosuper-rancagua)** en GetOnBoard Company _(2026-03-19)_ - GetOnBoard
- **[Ícaro Sales – Trainee Program](https://www.getonbrd.com/jobs/icaro-sales-trainee-program-iconstruye-santiago)** en GetOnBoard Company _(2026-03-11)_ - GetOnBoard
- **[Analista de Analítica Digital](https://www.getonbrd.com/jobs/analista-de-analitica-digital-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-03-05)_ - GetOnBoard
- **[Digital Quality Lead](https://www.getonbrd.com/jobs/digital-quality-lead-signant-health-remote)** en GetOnBoard Company _(2026-03-03)_ - GetOnBoard
- **[Coordinador(a) Junior de Gobierno de Datos](https://www.getonbrd.com/jobs/coordinador-a-junior-de-gobierno-de-datos-bice-vida-santiago)** en GetOnBoard Company _(2026-02-26)_ - GetOnBoard
- **[SRE / DevOps Engineer Junior](https://www.getonbrd.com/jobs/sre-devops-engineer-junior-bc-tecnologia-remote)** en GetOnBoard Company _(2026-02-24)_ - GetOnBoard
- **[Asesor Educativo Comercial Junior](https://www.getonbrd.com/jobs/asesor-educativo-comercial-junior-colectivo23-lima)** en GetOnBoard Company _(2026-02-02)_ - GetOnBoard
- **[Software Engineer Back-end Developer Junior](https://www.getonbrd.com/jobs/software-engineer-back-end-developer-junior-2brains-remote)** en GetOnBoard Company _(2026-01-23)_ - GetOnBoard
- **[Jr Sales Executive](https://www.getonbrd.com/jobs/jr-sales-executive-coderslab-io-ciudad-de-mexico)** en GetOnBoard Company _(2026-01-21)_ - GetOnBoard
- **[Ingeniero(a) Junior de Software y Robótica](https://www.getonbrd.com/jobs/ingeniero-a-junior-de-software-y-robotica-maquintel-robotic-services-santiago)** en GetOnBoard Company _(2026-01-19)_ - GetOnBoard
- **[Analista de Seguridad de la Información Junior](https://www.getonbrd.com/jobs/analista-de-seguridad-de-la-informacion-junior-bc-tecnologia-santiago-bb38)** en GetOnBoard Company _(2026-01-16)_ - GetOnBoard
- **[Ingeniero Trainee Industrial](https://www.getonbrd.com/jobs/ingeniero-trainee-industrial-agrosuper-rancagua)** en GetOnBoard Company _(2025-12-29)_ - GetOnBoard
- **[Analista de Seguridad de la Información Junior](https://www.getonbrd.com/jobs/analista-de-seguridad-de-la-informacion-junior-bc-tecnologia-santiago)** en GetOnBoard Company _(2025-12-22)_ - GetOnBoard
- **[Inside Sales Contractor](https://remotive.com/remote-jobs/sales-business/inside-sales-contractor-2086540)** en Credit Wellness, LLC _(2026-03-08)_ - Remotive
- **[Trainee Paid Ads - Meta & Google (m/w/d)](https://www.arbeitnow.com/jobs/companies/shopwise-gmbh/trainee-paid-ads-meta-google-berlin-207244)** en Shopwise GmbH _(2026-03-31)_ - Arbeitnow
- **[Junior Paid Ads Manager - Meta & Google (m/w/d)](https://www.arbeitnow.com/jobs/companies/shopwise-gmbh/junior-paid-ads-manager-meta-google-berlin-185828)** en Shopwise GmbH _(2026-03-31)_ - Arbeitnow
- **[Junior DevOps Engineer (m/f/d)](https://www.arbeitnow.com/jobs/companies/flix/junior-devops-engineer-munich-303358)** en Flix _(2026-03-30)_ - Arbeitnow
- **[Junior DevOps Engineer (m/f/d)](https://www.arbeitnow.com/jobs/companies/flix/junior-devops-engineer-berlin-68648)** en Flix _(2026-03-30)_ - Arbeitnow
- **[Senior Payroll Associate Indian Payroll India](https://remoteOK.com/remote-jobs/remote-senior-payroll-associate-indian-payroll-india-deel-1130900)** en Deel _(2026-03-27)_ - RemoteOK

### Mobile

- **[Salesforce Technical Consultant (Field Service)](https://www.getonbrd.com/jobs/salesforce-technical-consultant-field-service-niuro-remote)** en GetOnBoard Company _(2026-03-26)_ - GetOnBoard
- **[Junior Manual QA Engineer](https://remoteOK.com/remote-jobs/remote-junior-manual-qa-engineer-topstep-1130823)** en Topstep _(2026-03-18)_ - RemoteOK

### Other

- **[Ejecutiva de Cuenta Marketing Junior](https://www.getonbrd.com/jobs/ejecutiva-de-cuenta-match-agencia-consultora-remote)** en GetOnBoard Company _(2026-03-18)_ - GetOnBoard
- **[Treasury & Accounting Analyst Junior](https://www.getonbrd.com/jobs/treasury-accounting-analyst-junior-wherex-santiago)** en GetOnBoard Company _(2026-03-05)_ - GetOnBoard
- **[Customer Success Executive Junior Técnico B2B/ IoT](https://www.getonbrd.com/jobs/customer-success-executive-junior-tecnico-b2b-iot-guinea-mobile-sac-cuy-movil-lima)** en GetOnBoard Company _(2026-02-10)_ - GetOnBoard
- **[Ejecutivo de Soporte Trainee](https://www.getonbrd.com/jobs/ejecutivo-de-soporte-trainee-agendapro-ciudad-de-mexico)** en GetOnBoard Company _(2026-01-19)_ - GetOnBoard
- **[Ejecutivo de Soporte Trainee](https://www.getonbrd.com/jobs/ejecutivo-de-soporte-trainee-agendapro-santiago)** en GetOnBoard Company _(2025-11-27)_ - GetOnBoard
- **[Junior HR & Assistenz (m/w/d) - 2 Jahre befristet](https://www.arbeitnow.com/jobs/companies/augustus-management-gmbh/junior-hr-assistenz-2-jahre-befristet-berlin-206189)** en Augustus Management GmbH _(2026-03-31)_ - Arbeitnow
- **[(Junior) KYC Analyst](https://www.arbeitnow.com/jobs/companies/tangany-gmbh/junior-kyc-analyst-munich-270143)** en Tangany GmbH _(2026-03-31)_ - Arbeitnow
- **[Marketing-Stratege (m/w/d) - Mini-Job](https://www.arbeitnow.com/jobs/companies/snipki/marketing-stratege-mini-job-berlin-138295)** en snipKI _(2026-03-31)_ - Arbeitnow
- **[Marketing-Spezialist (m/w/d) - Mini-Job](https://www.arbeitnow.com/jobs/companies/snipki/marketing-spezialist-mini-job-berlin-83124)** en snipKI _(2026-03-31)_ - Arbeitnow
- **[PR & Kommunikations-Spezialist (m/w/d) - Mini-Job](https://www.arbeitnow.com/jobs/companies/snipki/pr-kommunikations-spezialist-mini-job-berlin-18403)** en snipKI _(2026-03-31)_ - Arbeitnow
- **[Graphic & Web Design Spezialist (m/w/d) - Mini-Job](https://www.arbeitnow.com/jobs/companies/snipki/graphic-web-design-spezialist-mini-job-berlin-406302)** en snipKI _(2026-03-31)_ - Arbeitnow
- **[Junior Key Account Manager für mehr Wohnraum (all genders) - Hybrid - Berlin](https://www.arbeitnow.com/jobs/companies/doozer-real-estate-systems-gmbh/junior-key-account-manager-fur-mehr-wohnraum-all-genders-hybrid-berlin-11380)** en Doozer Real Estate Systems GmbH _(2026-03-31)_ - Arbeitnow

<!-- JOBS_END -->

---

## 🛠️ Stack Tecnológico
- Python 3 (`requests`, `beautifulsoup4`)
- GitHub Actions Automation Pipeline 
- Configuraciones parametrizadas vía JSON

## 🤝 Contribuir
Si conoces otras APIs abiertas para empleo Tech Junior, añade una fuente a `config.json` y su correspondiente mapeador a la carpeta `src/scrapers/`. 
_Hecho para la comunidad de Jr Devs._