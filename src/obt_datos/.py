import requests

api_key = 'badd9d87a3msh268e94afba1b1c8p1f8621jsnbd311e2c0c3f'
url = 'https://partners.api.skyscanner.net/apiservices/browseroutes/v1.0/US/USD/en-US/SFO-sky/ORD-sky/2025-08-02?apiKey=' + api_key

response = requests.get(url)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")