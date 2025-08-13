# 🕵️‍♂️ Web Scraper Tool

A modular and maintainable Python tool for scraping **visiting card information** from websites.  
It supports both **static scraping** (`requests` + BeautifulSoup) and **dynamic scraping** (Selenium), applies intelligent tagging, and outputs results in Excel or JSON.


## 📌 Features
- **Category-based scraping** — Healthcare, IT, Legal, Finance, Real Estate, and more.
- **Multi-method scraping** — Static (Requests) and Dynamic (Selenium) for JavaScript-heavy pages.
- **Multiple extraction strategies** — JSON-LD, contact sections, category-specific selectors, and generic patterns.
- **Data cleaning & processing**:
  - Email & phone validation
  - Duplicate removal
  - Location-based tagging
- **Flexible output** — Save results to Excel (`.xlsx`) or JSON.
- **Customizable configuration** via `scraper_config.json`.
---

## ⚙️ Installation
### 1️⃣ Clone the repository
git clone https://github.com/Ops-Sculptor/Web-Scrapper-tool.git
cd Web-Scrapper-tool
2️⃣ Create & activate a virtual environment
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt

🚀 Usage
1️⃣ Edit the configuration
Open config/scraper_config.json and set:
Categories & keywords to scrape
CSS selectors for extraction
Filters & validation rules
Selenium settings (headless mode, timeouts, etc.)
2️⃣ Run the scraper
python main.py
3️⃣ Output
Excel: output.xlsx
JSON: output.json
Logs: scraper.log

🛠 Customization
Add new categories → Edit scraper_config.json in config/
Change scraping method → Toggle "use_selenium": true in config
Add more output formats → Create new writer modules in output/

📜 Requirements
Python 3.8+
Google Chrome + ChromeDriver (for Selenium)
Internet connection

🤝 Contributing
Fork this repo

Create a new branch:
git checkout -b feature/my-feature
Make changes

Commit and push:
git commit -m "feat: add my new feature"
git push origin feature/my-feature
Open a pull request

📄 License
This project is licensed under the MIT License — see the LICENSE file for details.
