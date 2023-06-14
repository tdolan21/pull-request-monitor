import os
import requests

class JenkinsConnector:
    def __init__(self, url: str) -> None:
        self.url = url
        self.username = os.getenv('JENKINS_USERNAME')
        self.password = os.getenv('JENKINS_PASSWORD')

    def trigger_build(self, job_name: str, parameters: dict = None) -> None:
        # Construct the API URL for triggering a build
        api_url = f"{self.url}/job/{job_name}/build"

        try:
            if parameters:
                # If parameters are provided, trigger a parameterized build
                api_url += "WithParameters"
                response = requests.post(
                    api_url,
                    headers={"Content-Type": "application/x-www-form-urlencoded"},
                    params=parameters,
                    auth=(self.username, self.password),
                )
            else:
                # Otherwise, trigger a regular build
                response = requests.post(
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
            print(f"Successfully triggered build for job {job_name}")
