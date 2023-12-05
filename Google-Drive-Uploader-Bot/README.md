# Google Drive File Upload with PyDrive2

This repository contains a Python script that allows you to upload files to your Google Drive using the PyDrive library. You can use this script to easily upload individual files to your Google Drive account.

## Prerequisites

Before using the script, make sure you have the following prerequisites installed:

- Python 3. x
- PyDrive library (`pydrive2`)

You can install the `pydrive2` library using pip:

```bash
pip install -r requirements.txt
```

## Set up Google Drive API

1. Go to the [Google API Console](https://console.developers.google.com/).

2. Create a new project.

3. Enable the "Google Drive API" for the project.

4. Create credentials for the API and download the JSON file containing the client ID and client secret.

5. Rename the downloaded JSON file to `client_secrets.json` and place it in the same directory as your Python script.


## Usage

Follow these steps to use the script:

1. Clone this repository or download the Python script to your local machine.

2. Open the Python script in a text editor or IDE of your choice.

3. Replace the empty string (`file_path`) with the absolute path to the file you want to upload. For example:

   ```python
   file_path = r"/path/to/your/file.txt"
   ```

4. Save the changes
5. Run the script using:
   ```
   python main.py
   ```

6. On successful compilation of the code, the script will prompt you into your Google account which was used to create the Google Drive API.
7. After the successfulf authentication, the file will be uploaded to your Google Drive and you will the following confirmation message.
   ```
   The authentication flow has completed.
   ```
