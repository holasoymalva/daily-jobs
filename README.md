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
- **[Desarrollador/a Full-Stack Junior](https://www.getonbrd.com/jobs/desarrollador-a-full-stack-junior-wizz-life-santiago)** en GetOnBoard Company _(2026-02-24)_ - GetOnBoard
- **[DevOps Engineer Junior](https://www.getonbrd.com/jobs/devops-engineer-junior-healthatom-santiago)** en GetOnBoard Company _(2026-02-23)_ - GetOnBoard
- **[Desarrollador Junior IA para Incubadora de Software](https://www.getonbrd.com/jobs/desarrollador-junior-ia-para-incubadora-de-software-construckit-santiago)** en GetOnBoard Company _(2026-03-05)_ - GetOnBoard
- **[Diseñador/a Gráfico Digital Junior](https://www.getonbrd.com/jobs/disenador-a-grafico-digital-junior-bh-studios-remote)** en GetOnBoard Company _(2026-03-02)_ - GetOnBoard
- **[Front-end UI Developer (Junior / Mid)](https://www.getonbrd.com/jobs/frontend-ui-developer-junior-mid-i2b-technologies-remote)** en GetOnBoard Company _(2026-02-19)_ - GetOnBoard
- **[Ruby on Rails Developer (Junior / Semi Senior)](https://www.getonbrd.com/jobs/semi-senior-ruby-on-rails-developer-saas-subscriptions-riolab-santiago)** en GetOnBoard Company _(2026-02-17)_ - GetOnBoard
- **[Junior Full-Stack Engineer (Ruby on Rails)](https://www.getonbrd.com/jobs/junior-full-stack-engineer-ruby-on-rails-autoraptor-remote)** en GetOnBoard Company _(2026-01-08)_ - GetOnBoard
- **[Scripter – Java (Web Junior) con Inglés Avanzado](https://www.getonbrd.com/jobs/scripter-analyst-ocr-web-con-ingles-avanzado-remoto-i2b-technologies-remote)** en GetOnBoard Company _(2025-12-01)_ - GetOnBoard
- **[Junior Automation Developer (N8n, APIs, JS)](https://www.getonbrd.com/jobs/jjunior-automation-developer-n8n-apis-js-lumago-info-admyo-s-a-de-c-v-remote)** en GetOnBoard Company _(2025-11-28)_ - GetOnBoard
- **[Desarrollador Angular](https://www.getonbrd.com/jobs/desarrollador-angular-defontana-remote-159e)** en GetOnBoard Company _(2025-09-25)_ - GetOnBoard

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

### Other

- **[Treasury & Accounting Analyst Junior](https://www.getonbrd.com/jobs/treasury-accounting-analyst-junior-wherex-santiago)** en GetOnBoard Company _(2026-03-05)_ - GetOnBoard
- **[Ejecutivo en Generación de Demanda (Junior)](https://www.getonbrd.com/jobs/ejecutivo-en-generacion-de-demanda-dynamic-devs-santiago-acbd)** en GetOnBoard Company _(2026-03-04)_ - GetOnBoard
- **[Customer Success Executive Junior Técnico B2B/ IoT](https://www.getonbrd.com/jobs/customer-success-executive-junior-tecnico-b2b-iot-guinea-mobile-sac-cuy-movil-lima)** en GetOnBoard Company _(2026-02-09)_ - GetOnBoard
- **[Ejecutivo de Soporte Trainee](https://www.getonbrd.com/jobs/ejecutivo-de-soporte-trainee-agendapro-ciudad-de-mexico)** en GetOnBoard Company _(2026-01-19)_ - GetOnBoard
- **[Ejecutivo de Soporte Trainee](https://www.getonbrd.com/jobs/ejecutivo-de-soporte-trainee-agendapro-santiago)** en GetOnBoard Company _(2025-11-27)_ - GetOnBoard

<!-- JOBS_END -->

---

## 🛠️ Stack Tecnológico
- Python 3 (`requests`, `beautifulsoup4`)
- GitHub Actions Automation Pipeline 
- Configuraciones parametrizadas vía JSON

## 🤝 Contribuir
Si conoces otras APIs abiertas para empleo Tech Junior, añade una fuente a `config.json` y su correspondiente mapeador a la carpeta `src/scrapers/`. 
_Hecho para la comunidad de Jr Devs._