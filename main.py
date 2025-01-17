import requests
import time
import os
from dotenv import load_dotenv


load_dotenv()

test_code = """
console.log("Hello, NodeJS!")
5
""" if os.getenv('AZ_SESSION_POOL_LANGUAGE') == 'nodejs' else """
print("Hello, Python!")
5
"""

url = f"https://{os.getenv('AZ_REGION')}.dynamicsessions.io/subscriptions/{os.getenv('AZ_SUBSCRIPTION_ID')}/resourceGroups/{os.getenv('AZ_RESOURCE_GROUP')}/sessionPools/{os.getenv('AZ_SESSION_POOL_NAME')}/code/execute?api-version=2024-02-02-preview&identifier={os.getenv('AZ_SESSION_IDENTIFIER')}"
headers={"Authorization": f"Bearer {os.getenv('AZ_TOKEN')}"}
body = {
    "properties": {
        "codeInputType": "inline",
        "executionType": "synchronous",
        "code": test_code
    }
}

start = time.perf_counter()
res = requests.post(url, json=body, headers=headers)
end = time.perf_counter()

print(res.status_code)
print(res.text)
print('Elapsed seconds: ', end - start)