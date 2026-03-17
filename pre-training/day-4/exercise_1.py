import requests
import sys


def fetch_profile(name):
    try:
        profile = requests.get(f"https://api.github.com/users/{name}")

        if profile.status_code == 404:
            print("User not found")
            return
        elif profile.status_code == 403:
            print("Rate limit hit. Try again in a few minutes.")
            return
        elif profile.status_code == 200:
            profile = profile.json()

            print("------------------------------------- USER DETAILS -------------------------------------\n")
            print(f"Username: {profile.get('login')}")
            print(f"Bio: {profile.get('bio')}")
            print(f"Repos: {profile.get('public_repos')}")
            print(f"Followers : {profile.get('followers')}")

            repos = requests.get(f"https://api.github.com/users/{profile.get('login')}/repos?per_page=100").json()
            top5 = sorted(repos, key=lambda r: r["stargazers_count"], reverse=True)[:5]

            print(
                "\n------------------------------------- Top 5 repos by stars -------------------------------------\n")
            print(f" {'Repo':35} {'Stars':6}  {'Language'}")
            print("-" * 50)
            for repo in top5:
                print(f"{repo['name']:35} {repo['stargazers_count']:6}  {repo['language'] or 'N/A'}")
            return

    except requests.exceptions.ConnectionError:
        print("Something went wrong")


def main():
    if len(sys.argv) < 2:
        print("Usage: python exercise_1.py <username>")
        return
    fetch_profile(sys.argv[1])


if __name__ == "__main__":
    main()
