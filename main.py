import requests
import time
import os
from dotenv import load_dotenv


test_python_code = """
print("Hello, World!")
5
"""


load_dotenv()
url = f"https://{os.getenv('AZ_REGION')}.dynamicsessions.io/subscriptions/{os.getenv('AZ_SUBSCRIPTION_ID')}/resourceGroups/{os.getenv('AZ_RESOURCE_GROUP')}/sessionPools/{os.getenv('AZ_SESSION_POOL_NAME')}/code/execute?api-version=2024-02-02-preview&identifier={os.getenv('AZ_SESSION_IDENTIFIER')}"

body = {
    "properties": {
        "codeInputType": "inline",
        "executionType": "synchronous",
        "code": test_python_code
    }
}

start = time.perf_counter()
res = requests.post(url, json=body, headers={"Authorization": f"Bearer {os.getenv('AZ_TOKEN')}"})
end = time.perf_counter()


print(res.text)
print('Elapsed seconds: ', end - start)