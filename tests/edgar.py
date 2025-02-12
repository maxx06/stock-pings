from sec_api import QueryApi
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

queryApi = QueryApi(api_key=api_key)

ticker = "TSLA"

query = {
    "query": { "query_string": { 
        "query": f'formType:"4" AND ticker:"{ticker}"',
    }},
    "from": "0",
    "size": "10",
    "sort": [{"filedAt": {"order": "desc"}}]  # Sort by most recent filings
}

response = queryApi.get_filings(query)

# Print first few results
for filing in response['filings']:
    print(filing)
    print(f"Date: {filing['filedAt']}, Insider: {filing['entities'][0]['name']}, Link: {filing['link']}")