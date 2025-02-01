from setuptools import setup, find_packages

setup(
    name="auto_commit",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "watchdog",
        "GitPython",
        "google-generativeai",
    ],
    entry_points={
        "console_scripts": [
            "auto-commit=auto_commit.cli:main",
        ],
    },
)