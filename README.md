# Setup:

1. Create Azure resources:
    - Create a [resource group](https://portal.azure.com/?quickstart=true#browse/resourcegroups)
    - Create a [Container App Session Pool](https://portal.azure.com/?quickstart=true#create/hub)
    - Create an access token
    
        ```
        az login
        az account get-access-token --resource https://dynamicsessions.io
        ```
2. Set up environment variables `cp .env.sample .env`
3. Copy values from the Azure portal to the environment file
4. Run the POC

    ```bash
    python3 -m venv ./venv
    source ./venv/bin/activate
    pip install -r requirements.txt
    
    python main.py
    ```