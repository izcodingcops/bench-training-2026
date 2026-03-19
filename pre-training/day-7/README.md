# Reddit Technology Analyzer

Fetches the top 50 posts from r/technology, counts word frequency across titles, and saves a summary report to JSON.

## Project Structure

```
day-7/
├── reddit_analyzer.py
├── constants.py
└── report.json
```

## Run

```bash
python reddit_analyzer.py
```

Expected output:

```
Fetched 50 posts.
Report saved to report.json
```

## Output

`report.json` contains:

| Field               | Description                                  |
|---------------------|----------------------------------------------|
| `total_posts`       | Number of posts fetched                      |
| `most_upvoted_post` | Title, upvotes, author, URL of the top post  |
| `avg_upvotes`       | Average upvotes across all 50 posts          |
| `today_posts`       | Titles of posts created today (UTC)          |
| `older_posts`       | Titles of posts created before today         |
| `top_words`         | Top 20 words from titles, stopwords excluded |
