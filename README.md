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
| Ingeniero Trainee Planta San Vicente (2) | Data engineer (2) |
| Ejecutivo de Soporte Trainee (2) | Data (2) |
| Steuerfachangestellter / Steuerfachwirt / Bilanzbuchhalter / Trainee Steuerberatung (m/w/d) (2) | Automation (1) |
| Junior Artist Manager / Influencer Manager (m/w/d) (2) | Angular (1) |

### Frontend

- **[Technical Project Manager](https://www.getonbrd.com/jobs/technical-project-manager-waystone-software-altitude-remote)** en GetOnBoard Company _(2026-03-02)_ - GetOnBoard
- **[DevOps Engineer Junior](https://www.getonbrd.com/jobs/devops-engineer-junior-healthatom-santiago)** en GetOnBoard Company _(2026-02-23)_ - GetOnBoard
- **[Ruby on Rails Developer (Junior / Semi Senior)](https://www.getonbrd.com/jobs/semi-senior-ruby-on-rails-developer-saas-subscriptions-riolab-santiago)** en GetOnBoard Company _(2026-02-17)_ - GetOnBoard
- **[Junior Full-Stack Engineer (Ruby on Rails)](https://www.getonbrd.com/jobs/junior-full-stack-engineer-ruby-on-rails-autoraptor-remote)** en GetOnBoard Company _(2026-01-08)_ - GetOnBoard
- **[Junior Automation Developer (N8n, APIs, JS)](https://www.getonbrd.com/jobs/jjunior-automation-developer-n8n-apis-js-lumago-info-admyo-s-a-de-c-v-remote)** en GetOnBoard Company _(2025-11-29)_ - GetOnBoard
- **[Desarrollador Angular](https://www.getonbrd.com/jobs/desarrollador-angular-defontana-remote-159e)** en GetOnBoard Company _(2025-09-25)_ - GetOnBoard
- **[Shopify Engineer](https://remotive.com/remote-jobs/software-development/shopify-engineer-2088643)** en Nebulab _(2026-03-03)_ - Remotive

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
- **[Operations Specialist, Fleet Account Management](https://www.arbeitnow.com/jobs/companies/wolt-english/operations-specialist-fleet-account-management-berlin-11480)** en Wolt - English _(2026-03-15)_ - Arbeitnow

### Mobile

- **[Ingeniero Trainee Planta San Vicente](https://www.getonbrd.com/jobs/ingeniero-trainee-planta-san-vicente-agrosuper-san-vicente)** en GetOnBoard Company _(2026-03-12)_ - GetOnBoard
- **[Ingeniero Trainee Planta la Calera](https://www.getonbrd.com/jobs/ingeniero-trainee-planta-la-calera-agrosuper-valparaiso)** en GetOnBoard Company _(2026-03-13)_ - GetOnBoard

### Data

- **[Entry Level Crypto Market Specialist](https://remoteOK.com/remote-jobs/remote-entry-level-crypto-market-specialist-elemental-terra-1130759)** en ELEMENTAL TERRA _(2026-03-13)_ - RemoteOK

### Other

- **[Ingeniero Trainee Industrial, Plantas Productivas Agrosuper](https://www.getonbrd.com/jobs/ingeniero-trainee-industrial-plantas-faenadoras-agrosuper-rancagua)** en GetOnBoard Company _(2026-03-09)_ - GetOnBoard
- **[Trainee Automatización Industrial (Plc)](https://www.getonbrd.com/jobs/trainee-planta-alimentos-agrosuper-rancagua)** en GetOnBoard Company _(2026-03-09)_ - GetOnBoard
- **[Treasury & Accounting Analyst Junior](https://www.getonbrd.com/jobs/treasury-accounting-analyst-junior-wherex-santiago)** en GetOnBoard Company _(2026-03-05)_ - GetOnBoard
- **[Ejecutivo en Generación de Demanda (Junior)](https://www.getonbrd.com/jobs/ejecutivo-en-generacion-de-demanda-dynamic-devs-santiago-acbd)** en GetOnBoard Company _(2026-03-04)_ - GetOnBoard
- **[Ingeniero Trainee Planta San Vicente](https://www.getonbrd.com/jobs/ingeniero-trainee-planta-san-vicente-agrosuper-san-vicente-fc44)** en GetOnBoard Company _(2026-03-13)_ - GetOnBoard
- **[Customer Success Executive Junior Técnico B2B/ IoT](https://www.getonbrd.com/jobs/customer-success-executive-junior-tecnico-b2b-iot-guinea-mobile-sac-cuy-movil-lima)** en GetOnBoard Company _(2026-02-10)_ - GetOnBoard
- **[Ejecutivo de Soporte Trainee](https://www.getonbrd.com/jobs/ejecutivo-de-soporte-trainee-agendapro-ciudad-de-mexico)** en GetOnBoard Company _(2026-01-19)_ - GetOnBoard
- **[Ejecutivo de Soporte Trainee](https://www.getonbrd.com/jobs/ejecutivo-de-soporte-trainee-agendapro-santiago)** en GetOnBoard Company _(2025-11-27)_ - GetOnBoard
- **[Steuerfachangestellter / Steuerfachwirt / Bilanzbuchhalter / Trainee Steuerberatung (m/w/d)](https://www.arbeitnow.com/jobs/companies/sbc-steuerberater-rechtsanwalte-gbr/steuerfachangestellter-steuerfachwirt-bilanzbuchhalter-trainee-steuerberatung-bad-homburg-214008)** en SBC Steuerberater Rechtsanwälte GbR _(2026-03-16)_ - Arbeitnow
- **[Steuerfachangestellter / Steuerfachwirt / Bilanzbuchhalter / Trainee Steuerberatung (m/w/d)](https://www.arbeitnow.com/jobs/companies/sbc-steuerberater-rechtsanwalte-gbr/steuerfachangestellter-steuerfachwirt-bilanzbuchhalter-trainee-steuerberatung-darmstadt-248978)** en SBC Steuerberater Rechtsanwälte GbR _(2026-03-16)_ - Arbeitnow
- **[Junior Produktmanager (m/w/d) in Voll- oder Teilzeit (ab 25 Stunden/Woche)](https://www.arbeitnow.com/jobs/companies/petlando-gmbh/junior-produktmanager-in-voll-oder-teilzeit-ab-25-stunden-woche-mering-494400)** en Petlando GmbH _(2026-03-16)_ - Arbeitnow
- **[(Junior) Onlinemarketing Manager (M/W/D) Schwerpunkt Social Media](https://www.arbeitnow.com/jobs/companies/plantamedium-gmbh/junior-onlinemarketing-manager-schwerpunkt-social-media-warendorf-60392)** en plantamedium GmbH _(2026-03-16)_ - Arbeitnow
- **[Junior Performance Marketing Manager (m/w/d) | Remote | Werkstudent / Teilzeit](https://www.arbeitnow.com/jobs/companies/smartkundigen-ohg/junior-performance-marketing-manager-remote-werkstudent-teilzeit-neuss-130613)** en smartkündigen OHG _(2026-03-16)_ - Arbeitnow
- **[Junior Social Ads Manager (m/w/d) | Remote | Werkstudent / Teilzeit](https://www.arbeitnow.com/jobs/companies/smartkundigen-ohg/junior-social-ads-manager-remote-werkstudent-teilzeit-neuss-312629)** en smartkündigen OHG _(2026-03-16)_ - Arbeitnow
- **[Trainee Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/trainee-artist-manager-influencer-manager-mulheim-421589)** en Lionflence _(2026-03-15)_ - Arbeitnow
- **[Junior Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/junior-artist-manager-influencer-manager-berlin-272606)** en Lionflence _(2026-03-15)_ - Arbeitnow
- **[Junior Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/junior-artist-manager-influencer-manager-mulheim-136998)** en Lionflence _(2026-03-15)_ - Arbeitnow

<!-- JOBS_END -->

---

## 🛠️ Stack Tecnológico
- Python 3 (`requests`, `beautifulsoup4`)
- GitHub Actions Automation Pipeline 
- Configuraciones parametrizadas vía JSON

## 🤝 Contribuir
Si conoces otras APIs abiertas para empleo Tech Junior, añade una fuente a `config.json` y su correspondiente mapeador a la carpeta `src/scrapers/`. 
_Hecho para la comunidad de Jr Devs._