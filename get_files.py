import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://developer.api.autodesk.com"

def get_files_in_folder(token, project_id, folder_id):
    """
    Fetch files inside a folder.
    """
    headers = {"Authorization": f"Bearer {token}"}
    # https://aps.autodesk.com/en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-contents-GET/
    url = f"{BASE_URL}/data/v1/projects/{project_id}/folders/{folder_id}/contents"

    print(f"Fetching files from: {url}")

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        files = response.json().get("data", [])
        if files:
            print(f"Found {len(files)} files in folder {folder_id}")
            for file in files:
                print(f"File Name: {file['attributes']['displayName']}")
                print(f"File ID: {file['id']}")
        else:
            print(f"No files found in folder {folder_id}.")
    else:
        print(f"Error fetching files: {response.json()}")
