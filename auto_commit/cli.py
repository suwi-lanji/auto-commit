import argparse
from .git_manager import GitManager
from .change_detector import start_monitoring

def main():
    parser = argparse.ArgumentParser(description="Git Auto-Commit Bot")
    parser.add_argument("directory", type=str, help="Directory to monitor")
    args = parser.parse_args()

    # Ensure a Git repository exists
    GitManager.ensure_repo(args.directory)

    # Start monitoring the directory
    start_monitoring(args.directory)

if __name__ == "__main__":
    main()