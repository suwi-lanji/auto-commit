import google.generativeai as genai

class CommitMessageGenerator:
    def __init__(self, api_key):
        """
        Initialize the Gemini API client.
        """
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')  # Use the appropriate model

    def generate_commit_message(self, diff):
        """
        Generate a commit message using the Gemini API.
        """
        prompt = f"Generate a concise and meaningful Git commit message for the following changes:\n\n{diff}"
        response = self.model.generate_content(prompt)
        return response.text.strip()