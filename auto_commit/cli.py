import argparse
import os
from .git_manager import GitManager
from .change_detector import start_monitoring

def main():
    parser = argparse.ArgumentParser(description="Git Auto-Commit Bot")
    parser.add_argument("directory", type=str, help="Directory to monitor")
    parser.add_argument("--api-key", type=str, help="Gemini API key", default=os.getenv("GEMINI_API_KEY"))
    args = parser.parse_args()

    if not args.api_key:
        raise ValueError("Gemini API key is required. Pass it via --api-key or set the GEMINI_API_KEY environment variable.")

    # Ensure a Git repository exists
    repo = GitManager.ensure_repo(args.directory)

    # Start monitoring the directory
    start_monitoring(args.directory, repo, args.api_key)
if __name__ == "__main__":
    main()