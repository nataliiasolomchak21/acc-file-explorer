import os
from auth import get_autodesk_token
from get_files import get_files_in_folder

def main():
    #  Authenticate and get token
    token = get_autodesk_token()
    if not token:
        print("Failed to authenticate. Exiting.")
        exit()

    # Fetch projects and folder IDs from environment variables
    project_id = os.getenv("PROJECT_ID")  
    folder_id = os.getenv("FOLDER_ID") 

    # Fetch files inside the folder
    get_files_in_folder(token, project_id, folder_id)

if __name__ == "__main__":
    main()
