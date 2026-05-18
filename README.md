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
| Ejecutivo de Onboarding Junior (2) | Ruby (1) |
| Analista de Seguridad de la Información Junior (2) | Python (1) |
| Junior Artist Manager / Influencer Manager (m/w/d) (2) | Data engineer (1) |
| Trainee Artist Manager / Influencer Manager (m/w/d) (2) | Data (1) |

### Frontend

- **[Junior Front-end Engineer](https://www.getonbrd.com/jobs/junior-frontend-engineer-krunchbox-santiago)** en GetOnBoard Company _(2026-04-22)_ - GetOnBoard
- **[Ingeniero Junior](https://www.getonbrd.com/jobs/ingeniero-junior-khipu-remote-e6b1)** en GetOnBoard Company _(2026-04-08)_ - GetOnBoard
- **[AI Engineer](https://www.getonbrd.com/jobs/senior-ai-engineer-mas-analytics-puerto-montt-santiago-puerto-varas)** en GetOnBoard Company _(2026-03-09)_ - GetOnBoard
- **[Ruby on Rails Developer (Junior / Semi Senior)](https://www.getonbrd.com/jobs/semi-senior-ruby-on-rails-developer-saas-subscriptions-riolab-santiago)** en GetOnBoard Company _(2026-02-17)_ - GetOnBoard
- **[Lead Software Engineer](https://remoteOK.com/remote-jobs/remote-lead-software-engineer-csc-generation-1131529)** en CSC Generation _(2026-05-09)_ - RemoteOK

### Backend

- **[Ejecutivo de Onboarding Junior](https://www.getonbrd.com/jobs/ejecutivo-de-onboarding-trainee-agendapro-santiago-daf4)** en GetOnBoard Company _(2026-05-08)_ - GetOnBoard
- **[Ingeniero de Datos](https://www.getonbrd.com/jobs/ingeniero-de-datos-senior-foris-ai-remote)** en GetOnBoard Company _(2026-05-07)_ - GetOnBoard
- **[Ejecutivo de Onboarding Junior](https://www.getonbrd.com/jobs/ejecutivo-de-onboarding-junior-agendapro-buenos-aires)** en GetOnBoard Company _(2026-05-18)_ - GetOnBoard
- **[Programador Junior Python](https://www.getonbrd.com/jobs/programador-junior-python-toc-biometrics-peru-lima)** en GetOnBoard Company _(2026-05-15)_ - GetOnBoard
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
- **[Junior Consultant Datenschutz / Compliance (m/w/d)](https://www.arbeitnow.com/jobs/companies/2b-advice-gmbh/junior-consultant-datenschutz-compliance-bonn-366186)** en 2B Advice GmbH _(2026-05-18)_ - Arbeitnow
- **[Sr Solution Architect Consultant Sales Engineer](https://remoteOK.com/remote-jobs/remote-sr-solution-architect-consultant-sales-engineer-cyara-1131610)** en Cyara _(2026-05-16)_ - RemoteOK
- **[Sales Development Representative Inbound](https://remoteOK.com/remote-jobs/remote-sales-development-representative-inbound-yuno-1131605)** en Yuno _(2026-05-15)_ - RemoteOK
- **[Senior Medical Editor](https://remoteOK.com/remote-jobs/remote-senior-medical-editor-omnicom-health-1131571)** en Omnicom Health _(2026-05-13)_ - RemoteOK
- **[Manager Collections &amp; Recoveries](https://remoteOK.com/remote-jobs/remote-manager-collections-amp-recoveries-forbright-bank-1131526)** en Forbright Bank _(2026-05-09)_ - RemoteOK

### Mobile

- **[DevOps Junior (Latam )](https://www.getonbrd.com/jobs/devops-jr-remoto-latam-i2b-technologies-remote)** en GetOnBoard Company _(2026-04-28)_ - GetOnBoard

### Data

- **[Soporte Operativo Junior](https://www.getonbrd.com/jobs/soporte-operativo-junior-bc-tecnologia-remote)** en GetOnBoard Company _(2026-03-31)_ - GetOnBoard
- **[Online Hospitality Services Coordinator Entry Level](https://remoteOK.com/remote-jobs/remote-online-hospitality-services-coordinator-entry-level-aisles-amp-abroad-1131534)** en Aisles &amp; Abroad _(2026-05-10)_ - RemoteOK

### QA

- **[Developer QA – Junior](https://www.getonbrd.com/jobs/developer-qa-junior-ameris-capital-santiago)** en GetOnBoard Company _(2026-04-07)_ - GetOnBoard

### Other

- **[Project Manager](https://www.getonbrd.com/jobs/analista-de-proyectos-ti-y-automatizacion-tcit-santiago-178e)** en GetOnBoard Company _(2026-05-15)_ - GetOnBoard
- **[Ejecutivo en Generación de Demanda (Junior)](https://www.getonbrd.com/jobs/ejecutivo-en-generacion-de-demanda-dynamic-devs-santiago-acbd)** en GetOnBoard Company _(2026-04-29)_ - GetOnBoard
- **[Auxiliar de Operaciones Jr](https://www.getonbrd.com/jobs/auxiliar-de-operaciones-jr-coderslab-io-lima)** en GetOnBoard Company _(2026-04-17)_ - GetOnBoard
- **[Junior Network Engineer (Presencial)](https://www.getonbrd.com/jobs/networking-presencial-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-04-02)_ - GetOnBoard
- **[Ejecutiva de Cuenta Marketing Junior](https://www.getonbrd.com/jobs/ejecutiva-de-cuenta-match-agencia-consultora-remote)** en GetOnBoard Company _(2026-03-18)_ - GetOnBoard
- **[Customer Success Executive Junior Técnico B2B/ IoT](https://www.getonbrd.com/jobs/customer-success-executive-junior-tecnico-b2b-iot-guinea-mobile-sac-cuy-movil-lima)** en GetOnBoard Company _(2026-02-10)_ - GetOnBoard
- **[Ejecutivo de Soporte Trainee](https://www.getonbrd.com/jobs/ejecutivo-de-soporte-trainee-agendapro-ciudad-de-mexico)** en GetOnBoard Company _(2026-01-19)_ - GetOnBoard
- **[Vertriebsassistent (m/w/d) - Trainee | 6 Std./Tag | Vor Ort | Stuttgart-Vaihingen](https://www.arbeitnow.com/jobs/companies/levent-akalin/vertriebsassistent-trainee-6-std-tag-vor-ort-stuttgart-vaihingen-39547)** en Levent Akalin _(2026-05-18)_ - Arbeitnow
- **[Junior Content Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/finment-gmbh/junior-content-manager-berlin-339172)** en FinMent GmbH _(2026-05-18)_ - Arbeitnow
- **[Junior Online Marketing (m/w/d)](https://www.arbeitnow.com/jobs/companies/finment-gmbh/junior-online-marketing-berlin-212227)** en FinMent GmbH _(2026-05-18)_ - Arbeitnow
- **[Content Marketing Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/finment-gmbh/content-marketing-manager-berlin-85271)** en FinMent GmbH _(2026-05-18)_ - Arbeitnow
- **[Online Marketing (m/w/d)](https://www.arbeitnow.com/jobs/companies/finment-gmbh/online-marketing-berlin-348967)** en FinMent GmbH _(2026-05-18)_ - Arbeitnow
- **[Werkstudent (m/w/d) – Finance & Beratung (unternehmerisch, leistungsbasiert)](https://www.arbeitnow.com/jobs/companies/kevin-kehr/werkstudent-finance-beratung-unternehmerisch-leistungsbasiert-hamburg-89584)** en Kevin Kehr _(2026-05-18)_ - Arbeitnow
- **[Junior Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/junior-artist-manager-influencer-manager-mulheim-265951)** en Lionflence _(2026-05-18)_ - Arbeitnow
- **[Junior Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/junior-artist-manager-influencer-manager-berlin-101428)** en Lionflence _(2026-05-18)_ - Arbeitnow
- **[Trainee Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/trainee-artist-manager-influencer-manager-berlin-333839)** en Lionflence _(2026-05-18)_ - Arbeitnow
- **[Trainee Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/trainee-artist-manager-influencer-manager-mulheim-250545)** en Lionflence _(2026-05-18)_ - Arbeitnow

<!-- JOBS_END -->

---

## 🛠️ Stack Tecnológico
- Python 3 (`requests`, `beautifulsoup4`)
- GitHub Actions Automation Pipeline 
- Configuraciones parametrizadas vía JSON

## 🤝 Contribuir
Si conoces otras APIs abiertas para empleo Tech Junior, añade una fuente a `config.json` y su correspondiente mapeador a la carpeta `src/scrapers/`. 
_Hecho para la comunidad de Jr Devs._