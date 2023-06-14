from github_connector import GitHubConnector
from pull_request_monitor import PullRequestMonitor
from jenkins_connector import JenkinsConnector
from build_analyzer import BuildAnalyzer
from pull_request_commenter import PullRequestCommenter

# User-provided credentials
github_repository = "your_github_repository"
jenkins_url = "your_jenkins_url"

# Create instances of the necessary classes
github_connector = GitHubConnector(github_repository)
jenkins_connector = JenkinsConnector(jenkins_url)
build_analyzer = BuildAnalyzer()
pull_request_commenter = PullRequestCommenter(github_connector)

# Create an instance of PullRequestMonitor and start monitoring
pull_request_monitor = PullRequestMonitor(github_connector, jenkins_connector, build_analyzer, pull_request_commenter)

# Start monitoring for new pull requests
pull_request_monitor.start_monitoring()

# Fetch and display all open pull requests
pull_request_monitor.fetch_open_pull_requests()
