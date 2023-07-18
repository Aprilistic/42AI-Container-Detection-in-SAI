import requests
import argparse

def download_file(access_token, file_path, destination_path):
    headers = {
        "Authorization": "Bearer " + access_token,
        "Dropbox-API-Arg": '{"path": "' + file_path + '"}'
    }

    response = requests.post(
        "https://content.dropboxapi.com/2/files/download",
        headers=headers
    )

    if response.status_code == 200:
        with open(destination_path, "wb") as file:
            file.write(response.content)
        print("File downloaded successfully.")
    else:
        print("Failed to download file.")
        print(response.status_code)

def upload_file(access_token, file_path, destination_path):
    url = "https://content.dropboxapi.com/2/files/upload"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Dropbox-API-Arg": "{\"path\": \"" + destination_path + "\"}",
        "Content-Type": "application/octet-stream"
    }

    with open(file_path, "rb") as file:
        response = requests.post(url, headers=headers, data=file)

    if response.status_code == 200:
        print("File uploaded successfully.")
    else:
        print("Failed to upload file.")
        print(response.status_code)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Uploads/downloads a file to/from Dropbox.')
    # Add arguments
    parser.add_argument('--download', type=bool, help='1 if you need to download. 0 otherwise.')
    parser.add_argument('--file_path', type=str, help='Path to the file to upload/download.')
    parser.add_argument('--destination_path', type=str, help='Where to download/upload. ex)/Dropbox/Folder/filt.txt')

    # Parse the arguments
    args = parser.parse_args()

    # Access the values of the arguments
    access_token = 'sl.BibA18uPA7FbmKS1eWz_NjjoBq1jBteOQYHUUKDDZgrzX2Nt0yZS7VD6Cl9ThfFBeUdSHVIKLhjqGwzeLFSIrubbV2iWj-MFknD3hcmLqmgL6_QuJNJW7EpTwmgyhQCiUJeGTy1h'
    should_download = args.download
    file_path = args.file_path
    destination_path = args.destination_path
    if (should_download):
        download_file(access_token, file_path, destination_path)
    else:
        upload_file(access_token, file_path, destination_path)
