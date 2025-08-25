#!/usr/bin/env python3
"""
Northeastern University Faculty Scraper - v1.0
"""
import os
import requests
import logging

# setup scrapper logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler()
    ]
)

class HuskyHunter:
    """
    HuskyHunter: A tool for scraping faculty data from Northeastern University.
    """

    def __init__(self, people_url: str, output_dir="hunted_data", delay_range=(2, 5)):
        logging.info("HuskyHunter initialized.")
        self.people_url = people_url
        self.output_dir = output_dir
        self.delay_range = delay_range
        self.session = self.set_session()
        self.create_output_directory()

    def set_session(self) -> requests.Session:
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
        return session

    def create_output_directory(self) -> None:
        os.makedirs(self.output_dir, exist_ok=True)

    def scrape_single_faculty(self):
        """
        Scrape data for a single faculty member.
        """
        logging.info(f"Scraping single faculty member from: {self.people_url}")
        response = self.session.get(self.people_url)
        if response.status_code == 200:
            # Process the response content
            logging.info("Successfully fetched faculty data.")
        else:
            logging.error(f"Failed to fetch faculty data: {response.status_code}")

    def scrape_all_faculty(self):
        """
        Scrape data for all faculty members.
        """
        logging.info("Scraping all faculty members.")
        response = self.session.get(self.people_url)
        if response.status_code == 200:
            # Process the response content
            logging.info("Successfully fetched all faculty data.")
        else:
            logging.error(f"Failed to fetch all faculty data: {response.status_code}")

def main():
    """
    Main function to start the HuskyHunter scraper.
    """
    import sys

    if len(sys.argv) < 3:
        logging.error("Usage: python husky_hunter.py <mode> <people_url>")
        sys.exit(1)

    mode = sys.argv[1]
    people_url = sys.argv[2]

    if mode not in ["single", "hunt"]:
        logging.error("Invalid mode: Use 'single' or 'hunt'.")
        sys.exit(1)

    husky_hunter = HuskyHunter(people_url)
    if mode == "single":
        husky_hunter.scrape_single_faculty()
    elif mode == "hunt":
        husky_hunter.scrape_all_faculty()


if __name__ == "__main__":
    main()