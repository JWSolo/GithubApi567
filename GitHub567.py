import requests
import unittest


def GitHub567(github_id):
    """
    a function that will take as input a GitHub user ID. The output from the function will be a list of the names of
    the repositories that the user has, along with the number of commits that are in each of the listed repositories.
    """
    get_repo_name = requests.get(f"https://api.github.com/users/{github_id}/repos")
    r = get_repo_name.json()
    repo_list = []

    for i in range(len(r)):
        repo_list.append(r[i]["name"])

    commit_dict = {}
    for n in range(len(repo_list)):
        get_commits = requests.get(f"https://api.github.com/repos/{github_id}/{repo_list[n]}/commits")
        re = get_commits.json()
        commit_dict[repo_list[n]] = len(re)
        print(f"AccountID : {github_id} Repo : {repo_list[n]} Number of commits : {len(re)}")

    return commit_dict


if __name__ == "__main__":
    print(GitHub567("JWSolo"))
