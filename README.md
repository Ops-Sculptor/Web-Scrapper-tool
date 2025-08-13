# 🕵️‍♂️ Web Scraper Tool

A modular and maintainable Python tool for scraping **visiting card information** from websites.  
It supports both **static scraping** (`requests` + BeautifulSoup) and **dynamic scraping** (Selenium), applies intelligent tagging, and outputs results in Excel or JSON.

---

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

## 📂 Project Structure

Web-Scraper-tool/
│
├── main.py # Entry point
├── requirements.txt # Python dependencies
│
├── config/
│ ├── scraper_config.json # User settings for categories, selectors, filters
│ └── config_loader.py # Config loader and saver
│
├── core/
│ ├── models.py # VisitingCard dataclass
│ └── logger.py # Centralized logging setup
│
├── scraping/
│ ├── base_scraper.py # HTTP session setup
│ ├── requests_scraper.py # Static scraping logic
│ ├── selenium_scraper.py # Dynamic scraping logic
│ ├── extractors.py # HTML parsing & field extraction
│ ├── pagination.py # Pagination handling
│ └── dynamic_loading.py # Infinite scroll/load-more handling
│
├── processing/
│ ├── filters.py # Email/phone validation
│ ├── tagging.py # Auto-tagging by location
│ └── deduplication.py # Duplicate removal
│
└── output/
├── excel_writer.py # Save results to Excel
└── json_writer.py # Save results to JSON

yaml
Copy
Edit

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Ops-Sculptor/Web-Scrapper-tool.git
cd Web-Scrapper-tool
2️⃣ Create & activate a virtual environment
bash
Copy
Edit
python -m venv .venv

# Windows PowerShell
.\.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
3️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
🚀 Usage
1️⃣ Edit the configuration
Open config/scraper_config.json and set:

Categories & keywords to scrape

CSS selectors for extraction

Filters & validation rules

Selenium settings (headless mode, timeouts, etc.)

2️⃣ Run the scraper
bash
Copy
Edit
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

bash
Copy
Edit
git checkout -b feature/my-feature
Make changes

Commit and push:

bash
Copy
Edit
git commit -m "feat: add my new feature"
git push origin feature/my-feature
Open a pull request

📄 License
This project is licensed under the MIT License — see the LICENSE file for details.

📧 Contact
If you have questions or need help customizing this scraper, feel free to open an issue in the repository.

yaml
Copy
Edit

---

I kept it **professional but approachable**, added **code blocks** for commands, and explained the modular architecture so anyone can jump in.  

If you want, I can also add **example output screenshots** and **badges** (Python version, license, build status) so your GitHub page looks more polished. Would you like me to do that?
