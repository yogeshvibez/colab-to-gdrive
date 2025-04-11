# Install required packages
!pip install ipyfilechooser

import ipywidgets as widgets
from IPython.display import display
from ipyfilechooser import FileChooser
from google.colab import drive
import shutil
import os

# Mount Google Drive
drive.mount('/content/drive')

# Create file chooser for selecting files
file_chooser = FileChooser('/content')

# Function to upload the selected file to Google Drive
def upload_to_drive(b):
    selected_file = file_chooser.selected
    if selected_file:
        dest_path = f'/content/drive/MyDrive/{selected_file.split("/")[-1]}'
        shutil.copy(selected_file, dest_path)
        print(f"File uploaded to Google Drive: {dest_path}")
    else:
        print("No file selected.")

# Function to cancel the upload process
def cancel_upload(b):
    print("Upload cancelled.")

# Create Upload and Cancel buttons
upload_button = widgets.Button(description="Upload to Google Drive", button_style='primary')
upload_button.on_click(upload_to_drive)

cancel_button = widgets.Button(description="Cancel", button_style='danger')
cancel_button.on_click(cancel_upload)

# Create a file manager similar to Windows
file_manager = widgets.Accordion(children=[file_chooser])
file_manager.set_title(0, 'File Manager')

# Display the file manager, upload button, and cancel button
display(file_manager)
display(upload_button)
display(cancel_button)
