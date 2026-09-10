import cloudscraper
import time

url = "https://remsmmprovider.kesug.com/cronjobs/order.php"

scraper = cloudscraper.create_scraper(
    browser={'browser': 'chrome', 'platform': 'windows', 'mobile': False}
)

print("Starting 2-Minute Sync Engine...")

# Ek run me ye 5-6 bar har 120s (2 min) par hit karega
for i in range(5):
    try:
        response = scraper.get(url, timeout=30)
        print(f"[{time.strftime('%H:%M:%S')}] Hit {i+1} | Status: {response.status_code}")
        print("Output:", response.text[:120].strip())
    except Exception as e:
        print("Error:", str(e))
    
    if i < 4:
        time.sleep(120) # 2 minute ka gap
