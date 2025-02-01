import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ChangeDetector(FileSystemEventHandler):
    def __init__(self):
        self.changes = []

    def on_modified(self, event):
        if not event.is_directory:
            self.changes.append(("modified", event.src_path))
            print(f"Modified: {event.src_path}")

    def on_created(self, event):
        if not event.is_directory:
            self.changes.append(("created", event.src_path))
            print(f"Created: {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory:
            self.changes.append(("deleted", event.src_path))
            print(f"Deleted: {event.src_path}")

    def get_changes(self):
        changes = self.changes
        self.changes = []  # Clear the changes after retrieving them
        return changes

def start_monitoring(directory):
    """
    Start monitoring the directory for changes.
    """
    event_handler = ChangeDetector()
    observer = Observer()
    observer.schedule(event_handler, path=directory, recursive=True)
    observer.start()
    print(f"Monitoring directory: {directory}")

    try:
        while True:
            time.sleep(1)  # Keep the script running
            changes = event_handler.get_changes()
            if changes:
                print("Detected changes:", changes)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()