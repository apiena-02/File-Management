#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 13:10:24 2024

@author: apienaselvarajah
"""

import os
import sys
import logging
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source = "/Users/apienaselvarajah/Downloads"
destination = "/Users/apienaselvarajah/Desktop/test"

class manageDownloads(FileSystemEventHandler):
    def on_modified(self, event):
        entries = os.listdir(source)

        for entry in entries:
            source_path = os.path.join(source, entry)
            destination_path = os.path.join(destination, entry)
            
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