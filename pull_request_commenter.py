import requests
import json

class PullRequestCommenter:
    def __init__(self, github_connector: GitHubConnector) -> None:
        self.github_connector = github_connector

    def post_comment(self, pull_request_url: str, comment: str) -> None:
        # Extract the pull request number from the URL
        pull_request_number = pull_request_url.split('/')[-1]

        # Construct the API URL for posting a comment
        api_url = f"https://api.github.com/repos/{self.github_connector.repo_owner}/{self.github_connector.repo_name}/issues/{pull_request_number}/comments"

        # Create the JSON payload
        payload = {"body": comment}

        # Post the comment
        response = requests.post(
            api_url,
            headers={
                "Authorization": f"token {self.github_connector.token}",
                "Accept": "application/vnd.github.v3+json",
            },
            json=payload,
        )

        # Check for errors
        response.raise_for_status()

    def fetch_comments(self, pull_request_url: str) -> None:
        # Extract the pull request number from the URL
        pull_request_number = pull_request_url.split('/')[-1]

        # Construct the API URL for fetching comments
        api_url = f"https://api.github.com/repos/{self.github_connector.repo_owner}/{self.github_connector.repo_name}/issues/{pull_request_number}/comments"

        # Fetch the comments
        response = requests.get(
            api_url,
            headers={
                "Authorization": f"token {self.github_connector.token}",
                "Accept": "application/vnd.github.v3+json",
            },
        )

        # Check for errors
        response.raise_for_status()

        # Parse the JSON response
        comments = json.loads(response.text)

        # Print each comment
        for comment in comments:
            print(f"{comment['user']['login']}: {comment['body']}\n")
