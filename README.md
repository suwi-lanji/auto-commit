# Auto-Commit Bot

![GitHub](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.7%2B-green)

The **Auto-Commit Bot** is a Python-based tool that automatically monitors a directory for changes, generates meaningful commit messages using the **Google Gemini API**, and commits the changes to a Git repository. It’s perfect for automating repetitive Git tasks and ensuring consistent commit messages.

---

## Features

- **Real-Time File Monitoring**: Watches a directory for changes (created, modified, or deleted files).
- **Auto-Commit**: Automatically stages and commits changes with a generated commit message.
- **AI-Powered Commit Messages**: Uses the **Google Gemini API** to generate concise and meaningful commit messages based on `git diff`.
- **Git Repository Management**: Initializes a Git repository if one doesn’t exist in the directory.
- **Customizable**: Easily extendable to include additional features like auto-pushing to a remote repository.

---

## Installation

### Prerequisites

- Python 3.7 or higher
- A **Google Gemini API key** (sign up [here](https://ai.google.dev/))

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/suwi-lanji/auto-commit.git
   cd auto-commit
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set your Google Gemini API key as an environment variable:

   ```bash
   export GEMINI_API_KEY="your-api-key"
   ```

4. Install the package locally:
   ```bash
   pip install .
   ```

---

## Usage

Run the Auto-Commit Bot on a directory:

```bash
auto-commit /path/to/your/directory
```

### What Happens?

1. **Repository Initialization**:

   - If the directory is not a Git repository, the bot initializes one.

2. **File Monitoring**:

   - The bot monitors the directory for changes (created, modified, or deleted files).

3. **Auto-Commit**:

   - When changes are detected:
     - The bot stages all changes.
     - Generates a commit message using the Google Gemini API.
     - Commits the changes with the generated message.

4. **Logging**:
   - All actions (e.g., detected changes, generated commit messages, commits) are logged to the console.

---

## Example

### Directory Structure

```
/my-project/
├── file1.txt
├── file2.txt
```

### Running the Bot

```bash
auto-commit /my-project
```

### Making Changes

1. Modify `file1.txt`:

   ```bash
   echo "New content" >> /my-project/file1.txt
   ```

2. The bot detects the change and outputs:

   ```
   Modified: /my-project/file1.txt
   Staged all changes.
   Generated commit message: Updated file1.txt with new content.
   Committed changes with message: Updated file1.txt with new content.
   ```

3. Check the Git log:
   ```bash
   git -C /my-project log --oneline
   ```
   Output:
   ```
   abc1234 Updated file1.txt with new content.
   ```

---

## Configuration

### Environment Variables

- `GEMINI_API_KEY`: Your Google Gemini API key.

### Command-Line Arguments

- `directory`: The directory to monitor (required).
- `--api-key`: The Google Gemini API key (optional if set as an environment variable).

---

## Contributing

Contributions are welcome! Here’s how you can contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Google Gemini API**: For providing the AI model to generate commit messages.
- **GitPython**: For simplifying Git operations in Python.
- **Watchdog**: For monitoring file system changes.

---

## Questions?

If you have any questions or need further assistance, feel free to open an issue on the [GitHub repository](https://github.com/suwi-lanji/auto-commit).
