import requests
from dotenv import load_dotenv
import os
import argparse

# Load .env file
load_dotenv()

# Get values from environment
YOUR_SERPAPI_KEY = os.getenv("SERPAPI_KEY")
YOUR_WEBHOOK_URL = os.getenv("ZAPIER_WEBHOOK_URL")

def send_jobs_to_zap(search_term, location, api_key, webhook_url, max_results=3):
    # Step 1: Request Google Jobs results from SerpApi
    params = {
        "engine": "google_jobs",    # Use Google Jobs engine explicitly
        "q": search_term,
        "location": location,
        "api_key": api_key
    }

    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()

    # Step 2: Extract jobs list
    jobs = data.get("jobs_results", [])
    if not jobs:
        print("⚠️ No job results found.")
        return

    # Step 3: Send each job as a separate record to Zapier
    for job in jobs[:max_results]:
        title = job.get("title", "No title")
        company = job.get("company_name", "No company")
        job_location = job.get("location", "No location")
        description = job.get("description", "No summary")
        posted_date = job.get("posted_date", "No date")
        job_link = job.get("link", "No link")

        payload = {
            "Search Term": search_term,
            "Location": location,
            "Job Title": title,
            "Company": company,
            "Summary": description,
            "Job URL": job_link
        }

        zap_response = requests.post(webhook_url, json=payload)

        if zap_response.status_code == 200:
            print(f"✅ Sent job '{title}' successfully!")
        else:
            print(f"❌ Failed to send job '{title}': {zap_response.status_code} {zap_response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send Google Jobs data to Zapier via SerpApi")
    parser.add_argument('--query', type=str, required=True, help="Search query")
    parser.add_argument('--location', type=str, default="Lagos, Nigeria", help="Search location")

    args = parser.parse_args()

    if not YOUR_SERPAPI_KEY or not YOUR_WEBHOOK_URL:
        print("⚠️ Error: Make sure your .env file includes SERPAPI_KEY and ZAPIER_WEBHOOK_URL")
    else:
        send_jobs_to_zap(args.query, args.location, YOUR_SERPAPI_KEY, YOUR_WEBHOOK_URL)
