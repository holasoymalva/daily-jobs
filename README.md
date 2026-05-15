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
| Senior Software Engineer (Java/SpringBoot) (m/f/x) (2) | Java (4) |
| Senior Java Backend Engineer (m/f/x) (2) | Spring (2) |
| Trainee Artist Manager / Influencer Manager (m/w/d) (2) | Backend (2) |
| Junior Artist Manager / Influencer Manager (m/w/d) (2) | - |
| Senior Software Developer (gn) (1) | - |

### Frontend

- **[Senior Software Developer (gn)](https://www.arbeitnow.com/jobs/companies/bikeleasing-service-gmbh-co-kg/senior-software-developer-gn-berlin-348049)** en Bikeleasing-Service GmbH & Co. KG _(2026-05-15)_ - Arbeitnow
- **[Senior Software Engineer (Java/SpringBoot) (m/f/x)](https://www.arbeitnow.com/jobs/companies/atolls/senior-software-engineer-java-springboot-berlin-296260)** en Atolls _(2026-05-14)_ - Arbeitnow
- **[Senior Java Backend Engineer (m/f/x)](https://www.arbeitnow.com/jobs/companies/atolls/senior-java-backend-engineer-berlin-86502)** en Atolls _(2026-05-14)_ - Arbeitnow
- **[Senior Java Backend Engineer (m/f/x)](https://www.arbeitnow.com/jobs/companies/atolls/senior-java-backend-engineer-munich-153126)** en Atolls _(2026-05-14)_ - Arbeitnow
- **[Senior Software Engineer (Java/SpringBoot) (m/f/x)](https://www.arbeitnow.com/jobs/companies/atolls/senior-software-engineer-java-springboot-munich-342606)** en Atolls _(2026-05-14)_ - Arbeitnow
- **[Lead Software Engineer](https://remoteOK.com/remote-jobs/remote-lead-software-engineer-csc-generation-1131529)** en CSC Generation _(2026-05-09)_ - RemoteOK

### Backend

- **[Inside Sales Contractor](https://remotive.com/remote-jobs/sales/inside-sales-contractor-2086540)** en Credit Wellness, LLC _(2026-05-08)_ - Remotive
- **[AI Engineer](https://remotive.com/remote-jobs/artificial-intelligence/ai-engineer-2089958)** en Dry Ground AI _(2026-04-21)_ - Remotive
- **[Senior Medical Editor](https://remoteOK.com/remote-jobs/remote-senior-medical-editor-omnicom-health-1131571)** en Omnicom Health _(2026-05-13)_ - RemoteOK
- **[Manager Collections &amp; Recoveries](https://remoteOK.com/remote-jobs/remote-manager-collections-amp-recoveries-forbright-bank-1131526)** en Forbright Bank _(2026-05-09)_ - RemoteOK

### Data

- **[Online Hospitality Services Coordinator Entry Level](https://remoteOK.com/remote-jobs/remote-online-hospitality-services-coordinator-entry-level-aisles-amp-abroad-1131534)** en Aisles &amp; Abroad _(2026-05-10)_ - RemoteOK

### Other

- **[Projektassistenz / Junior Projektmanager im Bereich Grafik & Kreation - Teilzeit (m|w|d)](https://www.arbeitnow.com/jobs/companies/wiethe-content-gmbh/projektassistenz-junior-projektmanager-im-bereich-grafik-kreation-teilzeit-mwd-georgsmarienhutte-257522)** en Wiethe Content GmbH _(2026-05-15)_ - Arbeitnow
- **[Trainee Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/trainee-artist-manager-influencer-manager-mulheim-248860)** en Lionflence _(2026-05-15)_ - Arbeitnow
- **[Trainee Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/trainee-artist-manager-influencer-manager-berlin-290300)** en Lionflence _(2026-05-15)_ - Arbeitnow
- **[Junior Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/junior-artist-manager-influencer-manager-berlin-444148)** en Lionflence _(2026-05-15)_ - Arbeitnow
- **[Junior Artist Manager / Influencer Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/lionflence/junior-artist-manager-influencer-manager-mulheim-370187)** en Lionflence _(2026-05-15)_ - Arbeitnow
- **[Teamleitung Buchhaltung | Start Up](https://www.arbeitnow.com/jobs/companies/matera-gmbh/teamleitung-buchhaltung-start-up-berlin-1897)** en Matera GmbH _(2026-05-15)_ - Arbeitnow
- **[Junior PR Manager (m/w/d) – Remote oder Berlin](https://www.arbeitnow.com/jobs/companies/getpress/junior-pr-manager-remote-oder-berlin-19063)** en getpress _(2026-05-15)_ - Arbeitnow
- **[Junior Performance Marketing Manager in Teilzeit (m/w/d)](https://www.arbeitnow.com/jobs/companies/hey-marly-gmbh/junior-performance-marketing-manager-in-teilzeit-cologne-245097)** en Hey Marly GmbH _(2026-05-15)_ - Arbeitnow
- **[Senior IT-Techniker/-in (m/w/d) in Hannover](https://www.arbeitnow.com/jobs/companies/support-4-it-gmbh/senior-it-techniker-in-in-hannover-hanover-224795)** en Support-4-IT GmbH _(2026-05-14)_ - Arbeitnow
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