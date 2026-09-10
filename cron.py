import cloudscraper
import sys

url = "https://remsmmprovider.kesug.com/cronjobs/order.php"

scraper = cloudscraper.create_scraper(
    browser={'browser': 'chrome', 'platform': 'windows', 'mobile': False}
)

try:
    response = scraper.get(url, timeout=30)
    print(f"Status Code: {response.status_code}")
    print("Response Output:", response.text[:200].strip())
except Exception as e:
    print("Error executing cron:", str(e))
    sys.exit(1)
  
