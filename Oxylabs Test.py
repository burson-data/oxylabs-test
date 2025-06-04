import requests
from pprint import pprint

# Structure payload.
payload = {
    'source': 'google_search',
    'query': 'adidas',
    'geo_location': 'Indonesia',
    'parse': True
}

# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('workup_N6eA3', 'Sc4malert~~~'),
    json=payload,
)

# Print prettified response to stdout.
pprint(response.json())