import os
import zipfile
import requests

# List of URLs to try for downloading the file
file_urls = [
    "https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip",
    "http://web.archive.org/web/2/https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip",  # Wayback Machine
    # mirror URL
]

# Directory where you want to save the downloaded file and extract it
output_directory = "steamcmd"
# Path to the downloaded zip file
zip_file_path = os.path.join(output_directory, "steamcmd.zip")

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

download_successful = False

for url in file_urls:
    response = requests.get(url, allow_redirects=True)
    if response.status_code == 200:
        with open(zip_file_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {zip_file_path}")
        download_successful = True
        break
    else:
        print(f"Failed to download {url}")

if not download_successful:
    print("All download attempts failed. Exiting.")
    exit(1)

# Extract the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(output_directory)
    print(f"Extracted contents to {output_directory}")

# Delete the zip file
os.remove(zip_file_path)
print(f"Deleted {zip_file_path}")
