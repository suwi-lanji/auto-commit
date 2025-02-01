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
            Repo(directory)
            print(f"Git repository already exists in {directory}")
        except InvalidGitRepositoryError:
            print(f"Initializing new Git repository in {directory}")
            Repo.init(directory)