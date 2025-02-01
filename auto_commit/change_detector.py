import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from .commit_message_generator import CommitMessageGenerator
from .git_manager import GitManager
class ChangeDetector(FileSystemEventHandler):
    def __init__(self, repo, api_key):
        self.changes = []
        self.repo = repo
        self.commit_message_generator = CommitMessageGenerator(api_key)

    def on_modified(self, event):
        if not event.is_directory:
            self.changes.append(("modified", event.src_path))
            self.handle_changes()

    def on_created(self, event):
        if not event.is_directory:
            self.changes.append(("created", event.src_path))
            self.handle_changes()

    def on_deleted(self, event):
        if not event.is_directory:
            self.changes.append(("deleted", event.src_path))
            self.handle_changes()
    def handle_changes(self):
        """
        Handle detected changes by staging, generating a commit message, and committing.
        """
        diff = GitManager.get_diff(self.repo)
        if diff:
            # Stage changes
            GitManager.stage_changes(self.repo)

            # Generate commit message
            commit_message = self.commit_message_generator.generate_commit_message(diff)
            print(f"Generated commit message: {commit_message}")

            # Commit changes
            GitManager.commit_changes(self.repo, commit_message)
        else:
            print("No changes to commit.")
    def get_changes(self):
        changes = self.changes
        self.changes = []  # Clear the changes after retrieving them
        return changes

def start_monitoring(directory, repo, api_key):
    """
    Start monitoring the directory for changes.
    """
    event_handler = ChangeDetector(repo=repo, api_key=api_key)
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