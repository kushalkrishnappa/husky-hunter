# Husky Hunter

A Python tool for scraping faculty data from Northeastern University's Khoury College directory.

## Features

- Scrape individual faculty member profiles
- Scrape all faculty profiles (hunt mode)
- Session-based requests with proper headers
- Configurable output directory
- Comprehensive logging

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Scrape Single Faculty Member
```bash
python3 husky_hunter.py single <faculty_url>
```

Example:
```bash
python3 husky_hunter.py single https://www.khoury.northeastern.edu/people/jonathan-bell/
```

### Scrape All Faculty (Hunt Mode)
```bash
python3 husky_hunter.py hunt <base_url>
```

## Output

- Scraped data is saved to the `hunted_data/` directory by default
- Logs are written to `scraper.log` and console

## Parameters

- `mode`: Either "single" or "hunt"
- `people_url`: URL to scrape faculty data from
- Output directory: Defaults to "hunted_data"
- Delay range: Defaults to (2, 5) seconds between requests
