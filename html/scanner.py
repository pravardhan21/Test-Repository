# scanner.py

import requests

url = 'http://127.0.0.1:5500/html/a.html#'
security_headers = ['Content-Security-Policy', 'X-Content-Type-Options']

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise HTTPError for bad requests
except requests.exceptions.RequestException as e:
    print("Error occurred:", e)
    exit()

missing_headers = []
for header in security_headers:
    if header not in response.headers:
        missing_headers.append(header)

if missing_headers:
    print("Missing security headers:")
    for header in missing_headers:
        print(header)
else:
    print("No missing security headers found.")
