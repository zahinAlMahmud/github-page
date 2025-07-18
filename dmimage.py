import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL of the page containing images
url = "https://example.com"  # 🔥 Change this to your target link

# Folder to save images
os.makedirs("downloaded_images", exist_ok=True)

# Get the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all image tags
for img in soup.find_all("img"):
    img_url = urljoin(url, img.get("src"))  # Handle relative URLs
    img_name = os.path.basename(img_url)

    try:
        img_data = requests.get(img_url).content
        with open(f"downloaded_images/{img_name}", "wb") as f:
            f.write(img_data)
        print(f"✅ Downloaded: {img_name}")
    except Exception as e:
        print(f"❌ Failed to download {img_url}: {e}")
