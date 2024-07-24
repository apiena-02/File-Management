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
from watchdog.events import LoggingEventHandler

source = "/Users/apienaselvarajah/Downloads"

class manageDownloads():
    entries = os.listdir(source)

    for entry in entries:
        print(entry)
    
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