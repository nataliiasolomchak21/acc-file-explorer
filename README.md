## Project Description

Authenticate with Autodesk Construction Cloud (ACC), fetch files from a project folder, and extract folder IDs from Autodesk URLs.

## Features

- **Authenticate with Autodesk Construction Cloud**: Secure authentication using client ID and secret.
- **Fetch Files**: Retrieve files from a specific project folder within Autodesk Construction Cloud.
- **Extract Folder ID**: Extract the folder ID from Autodesk URLs.

---

## Prerequisites

Before running the project, make sure you have the following:

- Python 3.7 or higher
- pip (Python package installer)
- Autodesk Construction Cloud & Autodesk Platform Services account (to obtain the necessary API credentials)

---

## Setup Instructions

### Install Dependencies:

Make sure you have `pip` installed. Then, run the following command to install the necessary dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

#### Set Up Environment Variables:
- Create a .env file in the project root directory and add the following:
```
AUTODESK_CLIENT_ID=your_client_id
AUTODESK_CLIENT_SECRET=your_client_secret
PROJECT_ID=your_project_id
FOLDER_ID=your_folder_id
```

- Running the Project:
```
python main.py
```
- To extract a folder ID from an Autodesk Construction Cloud URL
```
python extract_folder.py
```
