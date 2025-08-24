#!/usr/bin/env python3
"""
Northeastern University Khoury College Faculty Scraper
This script scrapes faculty data from all pages of the Khoury College people directory
and creates individual JSON files for each faculty member.
"""

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
