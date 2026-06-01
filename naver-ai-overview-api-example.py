"""
Naver AI Overview API: A Quick Start Example
See more at: https://apify.com/johnvc/naver-ai-overview-api?fpr=9n7kx3
Input schema: https://apify.com/johnvc/naver-ai-overview-api/input-schema?fpr=9n7kx3

This script shows how to call the Naver AI Overview API on Apify from Python and
read its structured JSON output. It checks whether Naver shows an AI Overview for
a query and prints the answer and its cited sources. Inputs are kept small so
your first call stays cheap.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# Inputs are kept small (a single query) to keep this first run inexpensive:
# you are billed per query. Pass a `queries` list to check many terms at once
# once you know your budget.
run_input = {
    "query": "당뇨병 증상",  # a Korean informational query (diabetes symptoms)
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/naver-ai-overview-api").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset
# (apify-client 3.x returns a Run object; use .default_dataset_id, not run["..."])
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} row(s).\n")

# Show the AI Overview and its cited sources for each query.
for item in items:
    query = item.get("query", "")
    present = item.get("ai_overview_present")
    print(f"Query: {query}  (AI Overview present: {present})")
    markdown = item.get("markdown")
    if markdown:
        print("Answer (markdown):")
        print(markdown[:500] + ("..." if len(markdown) > 500 else ""))
    for ref in item.get("references", []):
        print(f"  source: {ref.get('title')}  {ref.get('link')}")
    print()
