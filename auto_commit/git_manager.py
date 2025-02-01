import os
from git import Repo, InvalidGitRepositoryError

class GitManager:
    @staticmethod
    def ensure_repo(directory):
        """
        Ensure a Git repository exists in the directory.
        If not, initialize one.
        """
        try:
            return Repo(directory)
            print(f"Git repository already exists in {directory}")
        except InvalidGitRepositoryError:
            print(f"Initializing new Git repository in {directory}")
            return Repo.init(directory)
    @staticmethod
    def get_diff(repo):
        """
        Get the `git diff` output for the repository.
        """
        return repo.git.diff()
    @staticmethod
    def stage_changes(repo):
        """
        Stage all changes in the repository.
        """
        repo.git.add(A=True)  # Stage all changes (new, modified, and deleted files)
        print("Staged all changes.")

    @staticmethod
    def commit_changes(repo, commit_message):
        """
        Commit the staged changes with the given commit message.
        """
        repo.git.commit(m=commit_message)
        print(f"Committed changes with message: {commit_message}")