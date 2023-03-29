import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/drish/Downloads"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"{event.src_path} created")
    
    def on_deleted(self, event):
        print(f"{event.src_path} deleted")
    
    def on_modified(self, event):
        print(f"{event.src_path} modified")
    
    def on_moved(self, event):
        print(f"{event.src_path} moved to {event.dst_path}")



#init event handler class
event_handler = FileEventHandler()

#init observer
observer = Observer()

# shedule the observer
observer.schedule(event_handler,from_dir,recursive=True)

observer.start()

try :
    while True:
        time.sleep(1)
        print("runing ............")
    
except KeyboardInterrupt:
    print("stop")
    observer.stop()

