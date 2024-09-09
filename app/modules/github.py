from service.github import get_repos, get_followers, commit_count
from type.github_service import MetricsDTO


def get_github_metrics(user: str) -> MetricsDTO:
    repos_values = get_repos(user)

    metrics: MetricsDTO = {"all_repos": len(repos_values)}
    metrics["all_followers"] = get_followers(user)

    for repo in repos_values:
        metrics["all_stars"] += repo["stars"]
        metrics["all_commits"] += commit_count(user, repo["name"])

    return metrics
