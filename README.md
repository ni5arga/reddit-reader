# Reddit Reader SCript
This script retrieves the top posts from a specified subreddit using the Reddit JSON API. It allows you to specify the subreddit, time filter, and sort method (hot, top, new, rising) as command-line arguments.

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. Clone the repository or download the `reddit.py` file.
2. Install the `requests` library by running the following command: `pip install requests`

## Usage

Run the script using the following command:
`python reddit.py <subreddit> <time_filter> <sort_method>`

Replace `<subreddit>`, `<time_filter>`, and `<sort_method>` with the desired values:

- `<subreddit>`: The name of the subreddit you want to retrieve top posts from.
- `<time_filter>`: The time filter for the top posts. Valid options are `day`, `week`, `month`, `year`, or `all`.
- `<sort_method>`: The sorting method for the top posts. Valid options are `hot`, `top`, `new`, or `rising`.

Example: `python reddit.py science day top`
