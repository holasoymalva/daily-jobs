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
| Analista de Seguridad de la Información Junior (2) | Data (3) |
| Desarrollador/a Full-Stack Junior (1) | Data engineer (2) |
| Ingeniero Junior (1) | Ruby (1) |
| AI Engineer (1) | Angular (1) |
| Ruby on Rails Developer (Junior / Semi Senior) (1) | Java (1) |

### Frontend

- **[Desarrollador/a Full-Stack Junior](https://www.getonbrd.com/jobs/desarrollador-a-full-stack-junior-btrust-santiago)** en GetOnBoard Company _(2026-04-17)_ - GetOnBoard
- **[Ingeniero Junior](https://www.getonbrd.com/jobs/ingeniero-junior-khipu-remote-e6b1)** en GetOnBoard Company _(2026-04-08)_ - GetOnBoard
- **[AI Engineer](https://www.getonbrd.com/jobs/senior-ai-engineer-mas-analytics-puerto-montt-santiago-puerto-varas)** en GetOnBoard Company _(2026-03-09)_ - GetOnBoard
- **[Ruby on Rails Developer (Junior / Semi Senior)](https://www.getonbrd.com/jobs/semi-senior-ruby-on-rails-developer-saas-subscriptions-riolab-santiago)** en GetOnBoard Company _(2026-02-17)_ - GetOnBoard
- **[Desarrollador Angular](https://www.getonbrd.com/jobs/desarrollador-angular-defontana-remote-159e)** en GetOnBoard Company _(2025-09-25)_ - GetOnBoard
- **[Junior Project Coordinator](https://remotive.com/remote-jobs/project-management/junior-project-coordinator-2088663)** en C4Media Inc. _(2026-03-24)_ - Remotive
- **[Senior Product Manager Applied AI](https://remoteOK.com/remote-jobs/remote-senior-product-manager-applied-ai-smartsheet-1131233)** en Smartsheet _(2026-04-21)_ - RemoteOK
- **[Banking Full Stack Software Developer TSCM 43657](https://remoteOK.com/remote-jobs/remote-banking-full-stack-software-developer-tscm-43657-eleks-1131120)** en Eleks _(2026-04-15)_ - RemoteOK

### Backend

- **[Ingeniero Junior en Inteligencia Artificial](https://www.getonbrd.com/jobs/ingeniero-junior-en-inteligencia-artificial-bice-vida-santiago)** en GetOnBoard Company _(2026-04-21)_ - GetOnBoard
- **[Analista de Ciberseguridad Junior](https://www.getonbrd.com/jobs/analista-de-ciberseguridad-junior-hf-solutions-santiago)** en GetOnBoard Company _(2026-04-20)_ - GetOnBoard
- **[Data Engineer Senior](https://www.getonbrd.com/jobs/data-engineer-senior-grupo-mariposa-remote-ba30)** en GetOnBoard Company _(2026-04-15)_ - GetOnBoard
- **[Product Owner Junior](https://www.getonbrd.com/jobs/product-owner-junior-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-04-15)_ - GetOnBoard
- **[Jr SDR Outbound](https://www.getonbrd.com/jobs/jr-sdr-outbound-interfell-remote)** en GetOnBoard Company _(2026-04-21)_ - GetOnBoard
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
- **[Software Developer (Junior) - Java, Groovy, ScriptRunner, Forge (m/w/d)](https://www.arbeitnow.com/jobs/companies/meskru-gmbh/software-developer-junior-java-groovy-scriptrunner-forge-munich-360376)** en MESKRU GmbH _(2026-04-22)_ - Arbeitnow
- **[Junior Designer (m/w/d) Schwerpunkt Creative AI](https://www.arbeitnow.com/jobs/companies/mci-deutschland-gmbh/junior-designer-schwerpunkt-creative-ai-hamburg-381165)** en MCI Deutschland GmbH _(2026-04-22)_ - Arbeitnow
- **[Data Analyst](https://remoteOK.com/remote-jobs/remote-data-analyst-criptoro-1131219)** en Criptoro _(2026-04-19)_ - RemoteOK

### Mobile

- **[Salesforce Technical Consultant (Field Service)](https://www.getonbrd.com/jobs/salesforce-technical-consultant-field-service-niuro-remote)** en GetOnBoard Company _(2026-03-26)_ - GetOnBoard

### Data

- **[Soporte Operativo Junior](https://www.getonbrd.com/jobs/soporte-operativo-junior-bc-tecnologia-remote)** en GetOnBoard Company _(2026-03-31)_ - GetOnBoard

### QA

- **[Developer QA – Junior](https://www.getonbrd.com/jobs/developer-qa-junior-ameris-capital-santiago)** en GetOnBoard Company _(2026-04-07)_ - GetOnBoard

### Other

- **[Auxiliar de Operaciones Jr](https://www.getonbrd.com/jobs/auxiliar-de-operaciones-jr-coderslab-io-lima)** en GetOnBoard Company _(2026-04-17)_ - GetOnBoard
- **[Junior Network Engineer (Presencial)](https://www.getonbrd.com/jobs/networking-presencial-bc-tecnologia-santiago)** en GetOnBoard Company _(2026-04-02)_ - GetOnBoard
- **[Ejecutiva de Cuenta Marketing Junior](https://www.getonbrd.com/jobs/ejecutiva-de-cuenta-match-agencia-consultora-remote)** en GetOnBoard Company _(2026-03-18)_ - GetOnBoard
- **[Ejecutivo en Generación de Demanda (Junior)](https://www.getonbrd.com/jobs/ejecutivo-en-generacion-de-demanda-dynamic-devs-santiago-acbd)** en GetOnBoard Company _(2026-03-04)_ - GetOnBoard
- **[Customer Success Executive Junior Técnico B2B/ IoT](https://www.getonbrd.com/jobs/customer-success-executive-junior-tecnico-b2b-iot-guinea-mobile-sac-cuy-movil-lima)** en GetOnBoard Company _(2026-02-10)_ - GetOnBoard
- **[Ejecutivo de Soporte Trainee](https://www.getonbrd.com/jobs/ejecutivo-de-soporte-trainee-agendapro-ciudad-de-mexico)** en GetOnBoard Company _(2026-01-19)_ - GetOnBoard
- **[Junior IT Consultant (m/w/d)](https://www.arbeitnow.com/jobs/companies/meskru-gmbh/junior-it-consultant-munich-259587)** en MESKRU GmbH _(2026-04-22)_ - Arbeitnow
- **[Junior Recruiter (m/w/d)](https://www.arbeitnow.com/jobs/companies/medialine-eurotrade-ag/junior-recruiter-sobernheim-316917)** en Medialine EuroTrade AG _(2026-04-22)_ - Arbeitnow
- **[IT System Administrator (m/w/d) Stralsund](https://www.arbeitnow.com/jobs/companies/gecko-mbh/it-system-administrator-stralsund-300651)** en GECKO mbH _(2026-04-22)_ - Arbeitnow
- **[IT System Administrator (m/w/d) Rostock](https://www.arbeitnow.com/jobs/companies/gecko-mbh/it-system-administrator-rostock-475178)** en GECKO mbH _(2026-04-22)_ - Arbeitnow
- **[Werkstudent (m/w/d) – Finance & Beratung (unternehmerisch, leistungsbasiert)](https://www.arbeitnow.com/jobs/companies/kevin-kehr/werkstudent-finance-beratung-unternehmerisch-leistungsbasiert-hamburg-202967)** en Kevin Kehr _(2026-04-22)_ - Arbeitnow
- **[Trainee (m/w/d) Consulting](https://www.arbeitnow.com/jobs/companies/mlp-wirtschaftsberatung/trainee-consulting-bonn-297432)** en MLP Wirtschaftsberatung _(2026-04-22)_ - Arbeitnow
- **[Junior-Energieberater im Vetrieb (m/w/d)](https://www.arbeitnow.com/jobs/companies/viviania-gmbh/junior-energieberater-im-vetrieb-ulm-271822)** en viviania GmbH _(2026-04-21)_ - Arbeitnow

<!-- JOBS_END -->

---

## 🛠️ Stack Tecnológico
- Python 3 (`requests`, `beautifulsoup4`)
- GitHub Actions Automation Pipeline 
- Configuraciones parametrizadas vía JSON

## 🤝 Contribuir
Si conoces otras APIs abiertas para empleo Tech Junior, añade una fuente a `config.json` y su correspondiente mapeador a la carpeta `src/scrapers/`. 
_Hecho para la comunidad de Jr Devs._