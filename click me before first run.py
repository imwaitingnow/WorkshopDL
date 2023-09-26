import os
import zipfile
import requests

# URL of the file to download
file_url = "https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip"
# Directory where you want to save the downloaded file and extract it
output_directory = "steamcmd"
# Path to the downloaded zip file
zip_file_path = os.path.join(output_directory, "steamcmd.zip")

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Download the file
response = requests.get(file_url)
if response.status_code == 200:
    with open(zip_file_path, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded {zip_file_path}")
else:
    print(f"Failed to download {file_url}")
    exit(1)

# Extract the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(output_directory)
    print(f"Extracted contents to {output_directory}")

# Delete the zip file
os.remove(zip_file_path)
print(f"Deleted {zip_file_path}")
