import requests
import sys

def get_top_posts(subreddit, time_filter, sort_method):
    url = f'https://www.reddit.com/r/{subreddit}/{sort_method}.json?t={time_filter}&limit=10'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        top_posts = data['data']['children']

        for post in top_posts:
            title = post['data']['title']
            permalink = post['data']['permalink']
            post_url = f'https://www.reddit.com{permalink}'
            print(f"Title: {title}")
            print(f"URL: {post_url}")
            print()
    else:
        print(f"Error: {response.status_code} - {response.reason}")

if len(sys.argv) == 4:
    subreddit_name = sys.argv[1]
    time_filter = sys.argv[2]
    sort_method = sys.argv[3]
    get_top_posts(subreddit_name, time_filter, sort_method)
else:
    print("Usage: python reddit.py <subreddit> <time_filter> <sort_method>")
