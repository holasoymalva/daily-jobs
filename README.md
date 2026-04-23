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
| AI Engineer (2) | Data (4) |
| Analista de Seguridad de la Información Junior (2) | Data engineer (2) |
| Trainee Artist Manager / Influencer Manager (m/w/d) (2) | Front-end (1) |
| Junior Artist Manager / Influencer Manager (m/w/d) (2) | Ruby (1) |
| Junior Front-end Engineer (1) | Angular (1) |

### Frontend

- **[Junior Front-end Engineer](https://www.getonbrd.com/jobs/junior-frontend-engineer-krunchbox-santiago)** en GetOnBoard Company _(2026-04-22)_ - GetOnBoard
- **[Ingeniero Junior](https://www.getonbrd.com/jobs/ingeniero-junior-khipu-remote-e6b1)** en GetOnBoard Company _(2026-04-08)_ - GetOnBoard
- **[AI Engineer](https://www.getonbrd.com/jobs/senior-ai-engineer-mas-analytics-puerto-montt-santiago-puerto-varas)** en GetOnBoard Company _(2026-03-09)_ - GetOnBoard
- **[Ruby on Rails Developer (Junior / Semi Senior)](https://www.getonbrd.com/jobs/semi-senior-ruby-on-rails-developer-saas-subscriptions-riolab-santiago)** en GetOnBoard Company _(2026-02-17)_ - GetOnBoard
- **[Desarrollador Angular](https://www.getonbrd.com/jobs/desarrollador-angular-defontana-remote-159e)** en GetOnBoard Company _(2025-09-25)_ - GetOnBoard
- **[Junior Project Coordinator](https://remotive.com/remote-jobs/project-management/junior-project-coordinator-2088663)** en C4Media Inc. _(2026-03-24)_ - Remotive
- **[Junior Developer (m/w/d) - Fullstack, Data & AI - 100% Home Office möglich](https://www.arbeitnow.com/jobs/companies/dej-technology-gmbh/junior-developer-fullstack-data-ai-100-home-office-moglich-rostock-491473)** en DEJ Technology GmbH _(2026-04-23)_ - Arbeitnow
- **[Senior Product Manager Applied AI](https://remoteOK.com/remote-jobs/remote-senior-product-manager-applied-ai-smartsheet-1131233)** en Smartsheet _(2026-04-21)_ - RemoteOK

### Backend

- **[Ingeniero Junior en Inteligencia Artificial](https://www.getonbrd.com/jobs/ingeniero-junior-en-inteligencia-artificial-bice-vida-santiago)** en GetOnBoard Company _(2026-04-21)_ - GetOnBoard
- **[Analista de Ciberseguridad Junior](https://www.getonbrd.com/jobs/analista-de-ciberseguridad-junior-hf-solutions-santiago)** en GetOnBoard Company _(2026-04-20)_ - GetOnBoard
- **[Data Engineer Senior](https://www.getonbrd.com/jobs/data-engineer-senior-grupo-mariposa-remote-ba30)** en GetOnBoard Company _(2026-04-15)_ - GetOnBoard
- **[Product Owner Junior](https://www.getonbrd.com/jobs/product-owner-junior-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-04-15)_ - GetOnBoard
- **[Business Analyst Junior](https://www.getonbrd.com/jobs/business-analyst-junior-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-04-22)_ - GetOnBoard
- **[Coordinador(a) Junior de Gobierno de Datos](https://www.getonbrd.com/jobs/coordinador-a-junior-de-gobierno-de-datos-bice-vida-santiago)** en GetOnBoard Company _(2026-04-21)_ - GetOnBoard
- **[Data Engineer Junior/Semi Senior](https://www.getonbrd.com/jobs/data-engineer-junior-semi-senior-lisit-santiago)** en GetOnBoard Company _(2026-04-21)_ - GetOnBoard
- **[Junior Growth Marketer (AI & Cloud Native)](https://www.getonbrd.com/jobs/senior-digital-marketing-growth-lead-ai-design-b2b-e-omnix-ai-corp-remote)** en GetOnBoard Company _(2026-03-26)_ - GetOnBoard
- **[Analista de Analítica Digital](https://www.getonbrd.com/jobs/analista-de-analitica-digital-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-03-05)_ - GetOnBoard
- **[Digital Quality Lead](https://www.getonbrd.com/jobs/digital-quality-lead-signant-health-remote)** en GetOnBoard Company _(2026-03-03)_ - GetOnBoard
- **[SRE / DevOps Engineer Junior](https://www.getonbrd.com/jobs/sre-devops-engineer-junior-bc-tecnologia-remote)** en GetOnBoard Company _(2026-02-24)_ - GetOnBoard
- **[Asesor de Contactabilidad Junior](https://www.getonbrd.com/jobs/asesor-educativo-comercial-junior-colectivo23-lima)** en GetOnBoard Company _(2026-02-02)_ - GetOnBoard
- **[Jr Sales Executive](https://www.getonbrd.com/jobs/jr-sales-executive-coderslab-io-ciudad-de-mexico)** en GetOnBoard Company _(2026-01-21)_ - GetOnBoard
- **[Ingeniero(a) Junior de Software y Robótica](https://www.getonbrd.com/jobs/ingeniero-a-junior-de-software-y-robotica-maquintel-robotic-services-santiago)** en GetOnBoard Company _(2026-01-19)_ - GetOnBoard
- **[Analista de Seguridad de la Información Junior](https://www.getonbrd.com/jobs/analista-de-seguridad-de-la-informacion-junior-bc-tecnologia-santiago-bb38)** en GetOnBoard Company _(2026-01-16)_ - GetOnBoard
- **[Analista de Seguridad de la Información Junior](https://www.getonbrd.com/jobs/analista-de-seguridad-de-la-informacion-junior-bc-tecnologia-santiago)** en GetOnBoard Company _(2025-12-22)_ - GetOnBoard
- **[AI Engineer](https://remotive.com/remote-jobs/ai-ml/ai-engineer-2089958)** en Dry Ground AI _(2026-04-21)_ - Remotive
- **[Bankkaufmann/-frau (m/w/d)](https://www.arbeitnow.com/jobs/companies/justhome-gmbh/bankkaufmann-frau-berlin-179318)** en Justhome GmbH _(2026-04-23)_ - Arbeitnow
- **[(Junior) Projektmanager TikTok Shop - all genders](https://www.arbeitnow.com/jobs/companies/adbaker/junior-projektmanager-tiktok-shop-all-genders-cologne-436888)** en ADBAKER _(2026-04-23)_ - Arbeitnow
- **[(Junior) Social Commerce Manager - all genders](https://www.arbeitnow.com/jobs/companies/adbaker/junior-social-commerce-manager-all-genders-cologne-231837)** en ADBAKER _(2026-04-23)_ - Arbeitnow
- **[Junior Account Manager - Vollzeit (m/w/d)](https://www.arbeitnow.com/jobs/companies/adkochmarketing-gmbh/junior-account-manager-vollzeit-hamburg-24606)** en AdKochMarketing GmbH _(2026-04-23)_ - Arbeitnow
- **[(Junior) Controller (m/f/d)](https://www.arbeitnow.com/jobs/companies/1komma50/junior-controller-hamburg-233849)** en 1KOMMA5˚ _(2026-04-22)_ - Arbeitnow
- **[Data Analyst](https://remoteOK.com/remote-jobs/remote-data-analyst-criptoro-1131219)** en Criptoro _(2026-04-19)_ - RemoteOK

### Mobile

- **[Salesforce Technical Consultant (Field Service)](https://www.getonbrd.com/jobs/salesforce-technical-consultant-field-service-niuro-remote)** en GetOnBoard Company _(2026-03-26)_ - GetOnBoard
- **[Junior IT-Support Specialist (m/w/d)](https://www.arbeitnow.com/jobs/companies/muxon/junior-it-support-specialist-greifswald-399910)** en Muxon _(2026-04-22)_ - Arbeitnow

### Data

- **[Soporte Operativo Junior](https://www.getonbrd.com/jobs/soporte-operativo-junior-bc-tecnologia-remote)** en GetOnBoard Company _(2026-03-31)_ - GetOnBoard
- **[Junior Consultant Microsoft 365 & Copilot (m/w/d) - 100% Home Office möglich](https://www.arbeitnow.com/jobs/companies/dej-technology-gmbh/junior-consultant-microsoft-365-copilot-100-home-office-moglich-rostock-134896)** en DEJ Technology GmbH _(2026-04-23)_ - Arbeitnow

### QA

- **[Developer QA – Junior](https://www.getonbrd.com/jobs/developer-qa-junior-ameris-capital-santiago)** en GetOnBoard Company _(2026-04-07)_ - GetOnBoard
- **[Junior / No-Code Spezialist (m/w/d) Vollzeit oder Teilzeit (n8n,make,zapier)](https://www.arbeitnow.com/jobs/companies/adkochmarketing-gmbh/junior-no-code-spezialist-vollzeit-oder-teilzeit-n8nmakezapier-hamburg-214124)** en AdKochMarketing GmbH _(2026-04-23)_ - Arbeitnow

### Other

- **[Auxiliar de Operaciones Jr](https://www.getonbrd.com/jobs/auxiliar-de-operaciones-jr-coderslab-io-lima)** en GetOnBoard Company _(2026-04-17)_ - GetOnBoard
- **[Junior Network Engineer (Presencial)](https://www.getonbrd.com/jobs/networking-presencial-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-04-02)_ - GetOnBoard
- **[Ejecutiva de Cuenta Marketing Junior](https://www.getonbrd.com/jobs/ejecutiva-de-cuenta-match-agencia-consultora-remote)** en GetOnBoard Company _(2026-03-18)_ - GetOnBoard
- **[Ejecutivo en Generación de Demanda (Junior)](https://www.getonbrd.com/jobs/ejecutivo-en-generacion-de-demanda-dynamic-devs-santiago-acbd)** en GetOnBoard Company _(2026-03-04)_ - GetOnBoard
- **[Customer Success Executive Junior Técnico B2B/ IoT](https://www.getonbrd.com/jobs/customer-success-executive-junior-tecnico-b2b-iot-guinea-mobile-sac-cuy-movil-lima)** en GetOnBoard Company _(2026-02-10)_ - GetOnBoard
- **[Ejecutivo de Soporte Trainee](https://www.getonbrd.com/jobs/ejecutivo-de-soporte-trainee-agendapro-ciudad-de-mexico)** en GetOnBoard Company _(2026-01-19)_ - GetOnBoard
- **[Junior Linkbuilding Manager - 100% Remote](https://www.arbeitnow.com/jobs/companies/wolf-of-seo-fz-llc/junior-linkbuilding-manager-100-remote-munich-231085)** en WOLF OF SEO FZ LLC _(2026-04-23)_ - Arbeitnow
- **[Trainee Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/trainee-artist-manager-influencer-manager-berlin-213186)** en Lionflence _(2026-04-23)_ - Arbeitnow
- **[Trainee Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/trainee-artist-manager-influencer-manager-mulheim-44407)** en Lionflence _(2026-04-23)_ - Arbeitnow
- **[Junior Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/junior-artist-manager-influencer-manager-mulheim-463190)** en Lionflence _(2026-04-23)_ - Arbeitnow
- **[Junior Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/junior-artist-manager-influencer-manager-berlin-384254)** en Lionflence _(2026-04-23)_ - Arbeitnow
- **[Werksstudent:in -Junior Performance-Marketing Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/spacedome-media-gmbh/werksstudentin-junior-performance-marketing-manager-berlin-111647)** en Spacedome Media GmbH _(2026-04-23)_ - Arbeitnow
- **[Referent*in Politik & Kommunikation (m/w/d) (Teilzeit)](https://www.arbeitnow.com/jobs/companies/business-angels-deutschland-band-ev/referentin-politik-kommunikation-teilzeit-berlin-140688)** en Business Angels Deutschland (BAND) e.V. _(2026-04-22)_ - Arbeitnow

<!-- JOBS_END -->

---

## 🛠️ Stack Tecnológico
- Python 3 (`requests`, `beautifulsoup4`)
- GitHub Actions Automation Pipeline 
- Configuraciones parametrizadas vía JSON

## 🤝 Contribuir
Si conoces otras APIs abiertas para empleo Tech Junior, añade una fuente a `config.json` y su correspondiente mapeador a la carpeta `src/scrapers/`. 
_Hecho para la comunidad de Jr Devs._