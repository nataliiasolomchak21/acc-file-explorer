import re
import urllib.parse

def extract_folder_id(url):
    """
    Takes a URL as input and extracts the folder ID after decoding.
    """
    # Decode the URL to handle URL encoding
    decoded_url = urllib.parse.unquote(url)
    
    # Define the regular expression pattern to extract the folder ID
    folder_id_pattern = r"folderUrn=urn:adsk\.(wipprod|wipmea):fs\.folder:co\.(\S+)"
    
    # Use regex to search for the folder ID in the decoded URL
    match = re.search(folder_id_pattern, decoded_url)
    
    if match:
        # Extract the folder ID from the match
        # Folder ID part after "folderUrn="
        folder_id = match.group(0).split('=')[1] 
        
        # Remove any additional query parameters like &viewModel
        folder_id_cleaned = folder_id.split('&')[0]
        
        print(f"Folder ID extracted: {folder_id_cleaned}")
    else:
        print("No valid folder ID found in the URL.")

if __name__ == "__main__":
    url = input("Please enter the Autodesk folder URL: ")

    extract_folder_id(url)
