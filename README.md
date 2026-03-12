# 🇪🇸 Global Spain Business Scraper (Google Maps)

A professional-grade Lead Generation tool built with Python and Selenium. This scraper is designed to extract high-quality business data and professional services across all provinces in Spain directly from Google Maps.

## 🎯 Project Goals
The main objective of this project is to build a structured dataset of service providers (lawyers, doctors, real estate, etc.) operating in Spain, specifically targeting businesses that cater to international or multilingual clients.

## ✨ Key Features
- **Comprehensive Coverage**: Dynamically loops through all major Spanish cities and professional categories.
- **Smart Automation**: Handles infinite scrolling and dynamic loading using Selenium WebDriver.
- **Human-Like Behavior**: Integrated random delays and custom User-Agents to ensure stability and avoid detection.
- **Clean Data Output**: 
  - Automated deduplication using **Pandas**.
  - Direct export to **Excel (.xlsx)** with **Auto-Filters** enabled.
  - Secondary export to **CSV** for database compatibility.
- **Localization Ready**: Handles Spanish special characters (ñ, á, é, etc.) perfectly using `utf-8-sig` encoding.

## 🛠️ Technology Stack
- **Language**: Python 3.10+
- **Automation**: Selenium WebDriver
- **Driver Management**: Webdriver Manager (Auto-install for Chrome)
- **Data Processing**: Pandas & OpenPyXL

## 🚀 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/your-username/spain-business-leads-scraper.git](https://github.com/your-username/spain-business-leads-scraper.git)
   cd spain-business-leads-scraper
