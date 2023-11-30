import httpx
import os

PRODUCTHUNT_DEV_TOKEN = os.environ.get("PRODUCTHUNT_DEV_TOKEN")

headers = {"Authorization": f"Bearer {PRODUCTHUNT_DEV_TOKEN}"}

redirect_urls = []
with httpx.Client(headers=headers) as client:
    r = client.get(
        "https://api.producthunt.com/v1/posts/all",
        params={"per_page": 50},
        timeout=20,
    )
    print(r)
    redirect_urls = [p['redirect_url'] for p in r.json()]

for redirect_url in redirect_urls:
    try:
        r2 = client.head(redirect_url, timeout=20)
        if r2.status_code == 301:
            original_url = r2.headers["Location"]
            print(f"{redirect_url} -> {original_url}")
    except Exception as e:
        print(f"{redirect_url} - {e}")

    try:
        r3 = client.head(original_url, timeout=20)
        print(f"Status Code: {r3.status_code}")
        for k, v in r3.headers.items():
            print(f"{k} - {v}")
    except Exception as e:
        print(f"{original_url} - {e}")