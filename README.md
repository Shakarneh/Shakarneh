<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,12,20&height=200&section=header&text=Mohammed%20Shakarneh&fontSize=48&fontColor=ffffff&animation=fadeIn&fontAlignY=32&desc=Software%20Development%20Engineer%20%C2%B7%20Python%20%C2%B7%20FastAPI%20%C2%B7%20Full-Stack&descSize=18&descAlignY=52" alt="banner"/>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3500&pause=800&color=58A6FF&center=true&vCenter=true&width=620&lines=Back-End+Developer+%7C+Python+%2B+FastAPI;Full-Stack+Delivery+%7C+React+%2B+Supabase;I+shipped+a+store+that+serves+real+customers;Clean+code%2C+real+products%2C+no+shortcuts" alt="typing intro">
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/mohammed-shakarneh"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://lolocosmetics.shop"><img src="https://img.shields.io/badge/Live_Project-lolocosmetics.shop-E75480?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Live project"></a>
  <a href="mailto:itshakarnehmohammed@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
  <img src="https://komarev.com/ghpvc/?username=Shakarneh&style=for-the-badge&color=58A6FF" alt="profile views">
</p>

---

## `GET` &nbsp;`/api/v1/developers/shakarneh`

```json
{
  "status": 200,
  "name": "Mohammed Shakarneh",
  "role": "Software Development Engineer",
  "focus": ["back-end", "REST APIs", "clean architecture"],
  "primary_stack": ["Python", "FastAPI", "SQLAlchemy", "PostgreSQL"],
  "also_ships": ["React", "TypeScript", "Supabase", "Cloudflare"],
  "experience": {
    "company": "Expert Choice CIS",
    "role": "Back-End Developer (Internship)",
    "built": "admin API — JWT auth, RBAC, CRUD, schedule conflict detection"
  },
  "in_production": "https://lolocosmetics.shop",
  "studying": "Software Engineering @ БГТУ им. В.Г. Шухова",
  "languages": ["Arabic (native)", "English", "Russian"],
  "currently_learning": ["OOP mastery", "clean code", "data structures & algorithms"],
  "open_to_work": true
}
```

---

## 🧭 How a request flows through the systems I build

> I can follow a request from the HTTP call through authentication, validation and business logic
> down to the database and back — and I know where it would break.

```mermaid
sequenceDiagram
    autonumber
    participant C as Client
    participant A as Auth · JWT
    participant V as Validation · Pydantic
    participant L as Business Logic
    participant D as Database

    C->>A: HTTP request + Bearer token
    A->>A: verify signature, check role
    A-->>C: 401 / 403 if not allowed
    A->>V: authorized request
    V->>V: parse and validate schema
    V-->>C: 422 if payload invalid
    V->>L: clean, typed data
    L->>L: rules, e.g. schedule conflict check
    L->>D: query inside a transaction
    D-->>L: rows
    L-->>C: 200 JSON response
```

---

## 🗺️ My engineering journey, as a commit history

```mermaid
gitGraph
    commit id: "first line of code"
    branch fundamentals
    checkout fundamentals
    commit id: "Java + OOP labs"
    commit id: "PHP + MySQL full-stack"
    checkout main
    merge fundamentals
    branch data
    checkout data
    commit id: "Pandas · 350K rows"
    commit id: "SQL analytics"
    checkout main
    merge data
    branch shipping
    checkout shipping
    commit id: "My Notes · desktop app"
    commit id: "Lolo Cosmetics · LIVE"
    checkout main
    merge shipping
    branch backend
    checkout backend
    commit id: "FastAPI internship"
    commit id: "JWT + RBAC + conflicts"
    checkout main
    merge backend
    commit id: "next: bigger systems" type: HIGHLIGHT
```

---

## 🛠️ Complete Tech Stack

**Languages**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![Java](https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=openjdk&logoColor=white)
![PHP](https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

**Back-End**

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-4B8BBE?style=for-the-badge&logo=python&logoColor=white)
![REST APIs](https://img.shields.io/badge/REST_APIs-005571?style=for-the-badge&logo=fastapi&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![bcrypt](https://img.shields.io/badge/bcrypt-338833?style=for-the-badge&logo=letsencrypt&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger%2FOpenAPI-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)

**Front-End**

![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![React Router](https://img.shields.io/badge/React_Router-CA4245?style=for-the-badge&logo=reactrouter&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)
![Framer Motion](https://img.shields.io/badge/Framer_Motion-0055FF?style=for-the-badge&logo=framer&logoColor=white)
![GSAP](https://img.shields.io/badge/GSAP-88CE02?style=for-the-badge&logo=greensock&logoColor=black)

**Databases & Cloud**

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3FCF8E?style=for-the-badge&logo=supabase&logoColor=white)
![Cloudflare Pages](https://img.shields.io/badge/Cloudflare_Pages-F38020?style=for-the-badge&logo=cloudflarepages&logoColor=white)
![Turnstile](https://img.shields.io/badge/Cloudflare_Turnstile-F38020?style=for-the-badge&logo=cloudflare&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-222222?style=for-the-badge&logo=githubpages&logoColor=white)

**Data & Analytics**

![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

**Desktop & Packaging**

![PyInstaller](https://img.shields.io/badge/PyInstaller-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Inno Setup](https://img.shields.io/badge/Inno_Setup-005799?style=for-the-badge&logo=windows&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white)

**Tools**

![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)

---

## 📌 Endpoints &nbsp;·&nbsp; my projects

| | Project | What it is | Stack |
|---|---|---|---|
| `200 LIVE` | **[Lolo Cosmetics](https://github.com/Shakarneh/lolo-cosmetics)** · [visit ↗](https://lolocosmetics.shop) | Production e-commerce for a real beauty brand — 267+ products, admin panel with analytics & review moderation, WhatsApp ordering, Arabic-first RTL | React · TypeScript · Vite · Supabase · Cloudflare |
| `201 BUILT` | **[Attendance Tracking System](https://github.com/Shakarneh/attendance-tracking-system)** | Back-end admin API for corporate training — JWT auth, role-based access, full CRUD, schedule conflict detection | Python · FastAPI · SQLAlchemy · SQLite |
| `201 BUILT` | **[AI Website](https://github.com/Shakarneh/AI-Website---Artificial-Intelligence)** | Full-stack site with session auth and an admin CRUD panel for users, pages, messages, reviews | PHP · MySQL · JavaScript |
| `200 SHIPPED` | **[My Notes](https://github.com/Shakarneh/My-Notes)** | Python-powered Windows desktop app — rich-text editor, Arabic RTL, dark/light themes, real installer | Python · PyInstaller · Inno Setup |
| `201 BUILT` | **[Java University Labs](https://github.com/Shakarneh/java-university-labs)** | OOP-focused Java labs — logging, regex, XML, MySQL | Java · MySQL |
| `201 BUILT` | **[Data Analysis](https://github.com/Shakarneh/covid-analysis)** | COVID-19 global analysis (350K-row Kaggle dataset), supermarket sales insights, SQL store analytics | Python · Pandas · Matplotlib · Jupyter |

---

## 📊 Stats

<p align="center">
  <img width="49%" src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=Shakarneh&theme=tokyonight" alt="profile details">
</p>

<p align="center">
  <img width="32%" src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=Shakarneh&theme=tokyonight" alt="repos per language">
  <img width="32%" src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=Shakarneh&theme=tokyonight" alt="most commit language">
  <img width="32%" src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=Shakarneh&theme=tokyonight" alt="stats">
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=Shakarneh&theme=tokyonight&hide_border=true" alt="GitHub streak">
</p>

<p align="center">
  <img width="95%" src="https://github-readme-activity-graph.vercel.app/graph?username=Shakarneh&theme=tokyo-night&hide_border=true&area=true" alt="Contribution graph">
</p>

---

<p align="center"><i>💼 Open to back-end and full-stack software engineering opportunities.</i></p>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,12,20&height=120&section=footer" alt="footer"/>
