# 🇪🇸 Global Spain Business Scraper
**Professional-Grade B2B Lead Generation for the Spanish Market**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python)
![Selenium](https://img.shields.io/badge/Automation-Selenium-red.svg?style=for-the-badge&logo=selenium)
![Market](https://img.shields.io/badge/Market-Spain_EU-yellow.svg?style=for-the-badge)
![Data](https://img.shields.io/badge/Encoding-UTF--8--SIG-green.svg?style=for-the-badge)

---

## 🎯 Project Overview
This high-performance automation engine is engineered to penetrate the European professional services market. It systematically crawls **Google Maps** across all Spanish provinces (Madrid, Barcelona, Valencia, etc.), focusing on high-ticket service providers like **Lawyers, Medical Specialists, and Real Estate Agencies** that cater to international clientele.

---

## ✨ High-End Features

### 🌍 Comprehensive Iberian Coverage
The scraper doesn't just search "Spain"; it dynamically loops through every major province and professional category, ensuring no business entity is left behind in the urban or coastal regions.

### 🛡️ Smart Stealth Automation
* **Human-Mimicry Logic**: Integrated randomized jitter and custom User-Agent rotation to bypass bot detection.
* **Infinite Scroll Handling**: Advanced Selenium logic to capture all "hidden" results that only appear on deep-scroll.

### 🧹 Premium Data Sanitization
* **Deduplication Engine**: Built-in **Pandas** logic to ensure every lead is unique.
* **Special Character Support**: Perfect handling of Spanish typography (ñ, á, é, í, ó, ú) using `utf-8-sig` encoding—**no more messy text.**
* **Dual-Format Export**: Generates filtered **Excel (.xlsx)** for sales teams and **CSV** for CRM compatibility.

---

## 🛠️ Technical Tech Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Language** | Python 3.10+ | Core Logic & Scripting |
| **Automation** | Selenium WebDriver | Dynamic Web Interaction |
| **Driver Management** | Webdriver Manager | Automatic Chrome Binary Setup |
| **Data Engineering** | Pandas & OpenPyXL | Cleaning & Excel Orchestration |

---

## 📂 Project Structure

```text
├── src/
│   ├── scraper_engine.py    # The Core: Selenium Search Logic
│   └── data_processor.py    # The Polisher: Deduplication & Encoding
├── output/
│   └── spain_leads_final.xlsx # Filtered & Ready-to-Use Leads
├── requirements.txt
└── README.md
