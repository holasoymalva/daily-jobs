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
| Full Stack Web-Developer/Tester (m/w/d) (1) | Tester (1) |
| Engineer Software (1) | Frontend (1) |
| Software Engineer (1) | Data (1) |
| Senior App &amp; Frontend Developer AS233 (1) | Data engineer (1) |
| AI Engineer (1) | - |

### Frontend

- **[Full Stack Web-Developer/Tester (m/w/d)](https://www.arbeitnow.com/jobs/companies/it-labs-gmbh/full-stack-web-developer-tester-furth-281028)** en IT-Labs GmbH _(2026-04-30)_ - Arbeitnow
- **[Engineer Software](https://remoteOK.com/remote-jobs/remote-engineer-software-calabrio-1131345)** en Calabrio _(2026-04-27)_ - RemoteOK
- **[Software Engineer](https://remoteOK.com/remote-jobs/remote-software-engineer-finalis-1131328)** en Finalis _(2026-04-26)_ - RemoteOK
- **[Senior App &amp; Frontend Developer AS233](https://remoteOK.com/remote-jobs/remote-senior-app-amp-frontend-developer-as233-smart-working-solutions-1131268)** en Smart Working Solutions _(2026-04-22)_ - RemoteOK

### Backend

- **[AI Engineer](https://remotive.com/remote-jobs/artificial-intelligence/ai-engineer-2089958)** en Dry Ground AI _(2026-04-21)_ - Remotive
- **[Online Marketing Trainee (m/w/d) SEA & Paid Media](https://www.arbeitnow.com/jobs/companies/klickkonzept-by-labelium/online-marketing-trainee-sea-paid-media-frankfurt-am-main-428637)** en Klickkonzept by Labelium _(2026-04-30)_ - Arbeitnow
- **[Senior Data Engineer](https://www.arbeitnow.com/jobs/companies/trustyou/senior-data-engineer-munich-176349)** en TrustYou _(2026-04-30)_ - Arbeitnow

### Other

- **[Content Marketing Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/finment-gmbh/content-marketing-manager-berlin-288500)** en FinMent GmbH _(2026-04-30)_ - Arbeitnow
- **[Online Marketing (m/w/d)](https://www.arbeitnow.com/jobs/companies/finment-gmbh/online-marketing-berlin-384716)** en FinMent GmbH _(2026-04-30)_ - Arbeitnow
- **[Influencer & Social Media & PR-Manager (m/w/d)](https://www.arbeitnow.com/jobs/companies/ad-publica-public-relations-gmbh/influencer-social-media-pr-manager-hamburg-180753)** en ad publica Public Relations GmbH _(2026-04-30)_ - Arbeitnow
- **[(Junior) Debitorenbuchhalter (m/w/d)](https://www.arbeitnow.com/jobs/companies/indie-solutions-gmbh/junior-debitorenbuchhalter-berlin-111944)** en INDIE Solutions GmbH _(2026-04-30)_ - Arbeitnow
- **[Junior (m/w/d) Customer Success & Client Onboarding](https://www.arbeitnow.com/jobs/companies/linkster-gmbh/junior-customer-success-client-onboarding-hamburg-234300)** en Linkster GmbH _(2026-04-29)_ - Arbeitnow

<!-- JOBS_END -->

---

## 🛠️ Stack Tecnológico
- Python 3 (`requests`, `beautifulsoup4`)
- GitHub Actions Automation Pipeline 
- Configuraciones parametrizadas vía JSON

## 🤝 Contribuir
Si conoces otras APIs abiertas para empleo Tech Junior, añade una fuente a `config.json` y su correspondiente mapeador a la carpeta `src/scrapers/`. 
_Hecho para la comunidad de Jr Devs._