import dropbox
from dropbox.exceptions import AuthError

# Your Dropbox access token
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'

# Path to the file you want to upload
file_path = '/path/to/large_file.txt'

def upload_large_file(file_path, dest, access_token):
    # Initialize Dropbox client
    dbx = dropbox.Dropbox(access_token)

    # Open the file in binary mode for reading
    with open(file_path, 'rb') as file:
        # Start an upload session
        session_start_result = dbx.files_upload_session_start(file.read(1024))

        # Get the session ID
        session_id = session_start_result.session_id

        # Upload chunks in 4MB increments
        chunk_size = 4 * 1024 * 1024
        cursor = dropbox.files.UploadSessionCursor(session_id, offset=1024)

        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                # No more data to upload, finish the session
                dbx.files_upload_session_finish('', cursor, dropbox.files.CommitInfo(path=dest))
                break

            # Append the chunk to the upload session
            dbx.files_upload_session_append_v2(chunk, cursor)
            cursor.offset += len(chunk)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Uploads/downloads a file to/from Dropbox.')
    # Add arguments
    parser.add_argument('--file', type=str, help='Path to the file to upload.')
    parser.add_argument('--dest', type=str, help='Where to upload. ex)/Folder/filt.txt')

    # Parse the arguments
    args = parser.parse_args()
    file_path = args.file
    dest = args.dest
    ACCESS_TOKEN = 'sl.BixGO1j0qMrVrBdmgnEZtR479UsnvVGn9-OSZc3qxlFC-QqXVeCcxzvbtePJsFRnPsNHssN0ZgZ-7-K0RJ8Zt1GV07dQ0xrcH-YEcN6DaovfFrfgeaQFS6HjVbIdyEAoBkLnuNxIkiBM'
    
    try:
        upload_large_file(file_path, dest, ACCESS_TOKEN)
        print("File upload complete!")
    except AuthError:
        print("Invalid Dropbox access token.")
    except Exception as e:
        print("An error occurred:", e)