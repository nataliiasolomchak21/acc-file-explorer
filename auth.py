import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://developer.api.autodesk.com"

def get_autodesk_token():
    """
    Authenticate with Autodesk and get an access token.
    """
    autodesk_client_id = os.getenv("AUTODESK_CLIENT_ID")
    autodesk_client_secret = os.getenv("AUTODESK_CLIENT_SECRET")

    # OAuth 2.0 authentication URL
    # https://aps.autodesk.com/en/docs/oauth/v2/reference/http/gettoken-POST/
    auth_url = f"{BASE_URL}/authentication/v2/token"
    auth_data = {
        "client_id": autodesk_client_id,
        "client_secret": autodesk_client_secret,
        "grant_type": "client_credentials",
        "scope": "data:read data:write bucket:read bucket:create",
    }

    # Make the POST request for authentication
    response = requests.post(auth_url, data=auth_data)

    # Check the response status
    if response.status_code == 200:
        print("Authentication successful!")
        return response.json()["access_token"]
    else:
        print(f"Error during authentication: {response.json()}")
        return None
