import os
from pydrive2.drive import GoogleDrive
from pydrive2.auth import GoogleAuth

gauth = GoogleAuth()

gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

# Enter the absolute path to the file
file_path = r""

file_title = os.path.basename(file_path)
f = drive.CreateFile({'title' : file_title})

f.SetContentFile(file_path)
f.Upload()
print(f"{file_title} was uploaded successfully!!")
f = None