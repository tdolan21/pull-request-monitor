# Automated Pull Request Monitor

This tool automates the process of monitoring a GitHub repository for new pull requests, triggering a build process in a Jenkins server, analyzing the build results, and posting a comment on the pull request with a summary of the build analysis.

## Prerequisites

- Python 3.6 or higher
- Access to a GitHub repository
- Access to a Jenkins server

## Installation

1. Clone this repository to your local machine.
2. Navigate to the directory containing the repository.
3. Install the required Python packages by running `pip install -r requirements.txt`.

## Configuration

Before running the tool, you need to set the following environment variables:

- `GITHUB_USERNAME`: Your GitHub username.
- `GITHUB_PASSWORD`: Your GitHub password.
- `JENKINS_USERNAME`: Your Jenkins username.
- `JENKINS_PASSWORD`: Your Jenkins password.

You can set these environment variables in your operating system's settings, or you can set them in your shell before running the tool. For example, in a Unix-based system, you can set an environment variable in the shell like this:

```bash
```export GITHUB_USERNAME=your_github_username

## Usage

To run the tool, navigate to the directory containing the repository and run the main.py script:

``` 
python main.py
```
The tool will start monitoring the specified GitHub repository for new pull requests. When a new pull request is detected, it will trigger a build process in the Jenkins server, analyze the build results, and post a comment on the pull request with a summary of the build analysis.

You can also fetch and display all open pull requests by calling the fetch_open_pull_requests method of the PullRequestMonitor class.

This README provides a basic overview of what the tool does, how to install it, how to configure it, and how to use it. You can customize it to suit your needs.
