"""
Author: Apiena Selvarajah
Date: July 23, 2024
Description: Monitors the Downloads folder and automatically organizes files into specific subfolders based on their types 
(videos, PDFs, documents, images, presentations, and other)
"""

import os
import logging
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Paths for organizing files
source = "/Users/apienaselvarajah/Downloads"
destination_videos = "/Users/apienaselvarajah/Downloads/Videos"
destination_pdf = "/Users/apienaselvarajah/Downloads/PDFs"
destination_docs = "/Users/apienaselvarajah/Downloads/WordDocs"
destination_images = "/Users/apienaselvarajah/Downloads/Images"
destination_powerpoints = "/Users/apienaselvarajah/Downloads/PowerPoints"
destination_other = "/Users/apienaselvarajah/Downloads/Other"

class manageDownloads(FileSystemEventHandler):
    """
    Handles file system events to organize files in the Downloads folder
    into specific subfolders based on their types.
    """
    def on_modified(self, event):
        entries = os.listdir(source)

        for entry in entries:
            source_path = os.path.join(source, entry)

            # Determine the destination path based on file type
            if (entry.endswith('.MOV') or entry.endswith('.mp4') or entry.endswith('.mpg')):
                destination_path = os.path.join(destination_videos, entry)
            
            elif (entry.endswith('.pdf')):
                destination_path = os.path.join(destination_pdf, entry)
            
            elif (entry.endswith('.docx') or entry.endswith('.doc')):
                destination_path = os.path.join(destination_docs, entry)

            elif (entry.endswith('.png') or entry.endswith('.jpg')):
                destination_path = os.path.join(destination_images, entry)
            
            elif (entry.endswith('.pptx') or entry.endswith('.ppsx') or entry.endswith('.ppt')):
                destination_path = os.path.join(destination_powerpoints, entry)
            
            else:
                destination_path = os.path.join(destination_other, entry)
            
            # Check if the entry is a file before moving
            if os.path.isfile(source_path):
                shutil.move(source_path, destination_path)
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    path = source
    event_handler = manageDownloads()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while observer.is_alive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()