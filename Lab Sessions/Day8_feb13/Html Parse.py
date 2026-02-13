# 1. .Scrape product details from an e-commerce sample page:
# Product name
# Price
# Rating
# Availability


import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/static"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("div", class_="thumbnail")

for product in products:
    # Product name
    name = product.find("a", class_="title").text.strip()

    # Price
    price = product.find("h4", class_="price").text.strip()

    # Rating
    rating = len(product.find_all("span", class_="glyphicon-star"))

    # Availability (SAFE)
    availability_tag = product.find("p", class_="pull-right")
    availability = availability_tag.text.strip() if availability_tag else "Not available"

    print("Product Name:", name)
    print("Price:", price)
    print("Rating:", rating, "stars")
    print("Availability:", availability)

# 2.Extract all image URLs from a webpage.

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://webscraper.io/test-sites/e-commerce/static"
headers = {"User-Agent": "Mozilla/5.0"}

# Send GET request
response = requests.get(url, headers=headers)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all image tags
images = soup.find_all("img")

print("Image URLs:\n")

for img in images:
    src = img.get("src")

    if src:
        # Convert relative URL to absolute URL
        full_url = urljoin(url, src)
        print(full_url)

