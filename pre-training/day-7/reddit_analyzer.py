import json
import requests
from datetime import datetime, timezone
from constants import *


class RedditAnalyzer:

    def __init__(self):
        self.posts = []
        self.most_upvoted_post = None
        self.avg_upvotes = None
        self.top_words = []
        self.today_posts = []
        self.older_posts = []

    def get_top50_posts(self):
        try:
            response = requests.get(
                REDDIT_POST_URL,
                headers={"User-Agent": "python:reddit.analyzer:v1.0 (by /u/irtazafayaz)"}
            )
            if response.status_code == 200:
                self.posts = response.json()["data"]["children"]
                print(f"Fetched {len(self.posts)} posts.")
                return True
            elif response.status_code == 404:
                print("Please confirm if the provided url is correct.")
            else:
                print(f"Error {response.status_code}: Unexpected response from reddit.")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {str(e)}")
        return False

    def count_words(self):
        word_count = {}
        for post in self.posts:
            for word in post["data"]["title"].lower().split():
                word = word.strip(PUNCTUATION_KEYS)
                if word and word not in STOPWORDS:
                    word_count[word] = word_count.get(word, 0) + 1

        self.top_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:20]
        return self.top_words

    def find_post_details(self):
        if not self.posts:
            print("No posts loaded. Run get_top50_posts() first.")
            return

        self.most_upvoted_post = sorted(self.posts, key=lambda post: post["data"]["ups"], reverse=True)[0]
        print(self.most_upvoted_post)
        total_ups = 0
        for post in self.posts:
            total_ups += post["data"]["ups"]
        self.avg_upvotes = total_ups / len(self.posts)

        today_ts = datetime.now(timezone.utc).replace(
            hour=0, minute=0, second=0, microsecond=0
        ).timestamp()
        self.today_posts = [p for p in self.posts if p["data"]["created_utc"] >= today_ts]
        self.older_posts = [p for p in self.posts if p["data"]["created_utc"] < today_ts]

    def _convert_to_json(self):
        most_upvoted = None
        if self.most_upvoted_post:
            data = self.most_upvoted_post["data"]
            most_upvoted = {
                "title": data["title"],
                "ups": data["ups"],
                "author": data["author"],
                "url": data["url"],
            }
        return {
            "total_posts": len(self.posts),
            "most_upvoted_post": most_upvoted,
            "avg_upvotes": self.avg_upvotes,
            "today_posts": [p["data"]["title"] for p in self.today_posts],
            "older_posts": [p["data"]["title"] for p in self.older_posts],
            "top_words": [w for w, c in self.top_words],
        }

    def save_to_json(self):
        data = self._convert_to_json()
        with open(REPORT_FILE, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Report saved to {REPORT_FILE}")


analyzer = RedditAnalyzer()
if analyzer.get_top50_posts():
    analyzer.count_words()
    analyzer.find_post_details()
    analyzer.save_to_json()
