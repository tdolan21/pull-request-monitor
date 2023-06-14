import os
import requests

class GitHubConnector:
    def __init__(self, repository: str) -> None:
        self.username = os.getenv('GITHUB_USERNAME')
        self.password = os.getenv('GITHUB_PASSWORD')
        self.repository = repository

    def connect(self) -> None:
        # Construct the API URL for the repository
        api_url = f"https://api.github.com/repos/{self.repository}"

        try:
            # Send a GET request to the API URL
            response = requests.get(
                api_url,
                auth=(self.username, self.password),
            )

            # Check for errors
            response.raise_for_status()

        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("Something went wrong with the request:",err)

        else:
            # If the request was successful, print a success message
            print(f"Successfully connected to the repository {self.repository}")
