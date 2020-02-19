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

    for n in range(len(repo_list)):
        get_commits = requests.get(f"https://api.github.com/repos/{github_id}/{repo_list[n]}/commits")
        re = get_commits.json()
        print(f"AccountID : {github_id} Repo : {repo_list[n]} Number of commits : {len(re)}")

    return repo_list

class TextFunction(unittest.TestCase):

    def test_GitHub567(self):

        self.assertEqual(GitHub567("JWSolo"), ['GithubApi567', 'SSW567', 'Triangle567', 'University-HW10'])

if __name__ == "__main__":
    unittest.main()

