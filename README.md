# SerpApi to Airtable Automation

**This project uses SerpApi's Google Jobs API to fetch job search results and sends them to Airtable via Zapier. It automates job tracking and creates a no-code dashboard to visualize data in real time.** 

--- 

## Features

- Fetches job results using the SerpApi Google Jobs engine
- Parses and sends each result to a Zapier webhook
- Zapier forwards the data into Airtable or any other connected tool
- Real-time automation with no-code dashboard capabilities


## Tech Stack

- **Python** – for the CLI integration script
- **SerpApi** – to access Google Jobs search results
- **Zapier** – to automate forwarding data
- **Airtable** – to visualize and manage the incoming job data

## Demo

```bash
    python search_to_airtable.py --query "remote software developer" --location "Toronto" --max_results 3
```

## Requirements
~ SerpApi account and API key

~ Zapier account and Webhook trigger set up

~ Airtable base (optional, for job dashboard)

~ Python 3.7+

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/CloudDev777/Serpapi_to_Airtable_Automation.git
cd Serpapi_to_Airtable_Automation
```
2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create a .env file in the root directory and add your credentials:

```bash
SERPAPI_KEY=your_serpapi_api_key
ZAPIER_WEBHOOK_URL=your_zapier_webhook_url
```

## Troubleshooting
No results: Check your SerpApi key, query, or location.

Webhook issues: Ensure the Zap is published and the webhook URL is correct.

Airtable errors: Double-check that field names match the JSON keys.
