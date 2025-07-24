import requests
import sys
from concurrent.futures import ThreadPoolExecutor

# Load endpoints and extensions from files
with open("endpoints.txt") as f:
    endpoints = [line.strip() for line in f if line.strip()]

with open("extensions.txt") as f:
    extensions = [line.strip() for line in f if line.strip()]

# Base URL from CLI or fallback
base_url = sys.argv[1] if len(sys.argv) > 1 else "https://www.example.com"

print(f"🔍 Starting Web Cache Deception scan on: {base_url}\n")

def scan(url):
    try:
        response = requests.get(url, timeout=10)
        code = response.status_code
        size = len(response.content)
        cache_control = response.headers.get("Cache-Control", "⚠️ Not Present")

        result = f"[{code}] {url}\n"
        result += f"    ↪ Size: {size} bytes\n"
        result += f"    ↪ Cache-Control: {cache_control}\n"

        # Check for personal data leak indicators
        keywords = ["name", "email", "phone", "wallet", "order", "address"]
        content = response.text.lower()
        if any(keyword in content for keyword in keywords):
            result += "    🚨 Possible Personal Info Leak Detected\n"

        return result
    except requests.exceptions.RequestException as e:
        return f"[ERROR] {url} → {e}"

# Generate all URLs to test
urls = [base_url.rstrip("/") + ep + ext for ep in endpoints for ext in extensions]

# Run with multithreading
with ThreadPoolExecutor(max_workers=10) as executor:
    for output in executor.map(scan, urls):
        print(output)
