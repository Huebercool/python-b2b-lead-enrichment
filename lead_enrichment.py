import os
import requests
import json

# RapidAPI Configuration
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY_HERE")
B2B_HOST = "b2b-domain-profiler.p.rapidapi.com" # Update to your exact host if needed

def enrich_domain(domain):
    url = f"https://{B2B_HOST}/"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": B2B_HOST
    }
    params = {"domain": domain}

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            print("⚠️ Quota Exceeded! Upgrade your plan on RapidAPI to continue.")
            return None
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return None

def main():
    target_domain = "stripe.com"
    print(f"--- Running B2B Enrichment for {target_domain} ---\n")
    
    result = enrich_domain(target_domain)
    if result and result.get("success"):
        print(json.dumps(result.get("data", {}), indent=2))
    else:
        print("Failed to retrieve enrichment data.")

if __name__ == "__main__":
    main()
