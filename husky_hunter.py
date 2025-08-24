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

    def set_session(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })

    def create_output_directory(self):
        os.makedirs(self.output_dir, exist_ok=True)
