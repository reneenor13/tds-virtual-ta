import requests
import json

# Base URL for Discourse API of the TDS forum
BASE_URL = "https://discourse.onlinedegree.iitm.ac.in"

def fetch_posts(category_id=34, page=0):
    url = f"{BASE_URL}/c/courses/tds-kb/{category_id}.json?page={page}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def save_posts(posts, filename="discourse_posts.json"):
    with open(filename, "w") as f:
        json.dump(posts, f, indent=2)

def main():
    all_posts = []
    page = 0
    while True:
        data = fetch_posts(page=page)
        if not data or not data.get('topic_list', {}).get('topics'):
            break
        topics = data['topic_list']['topics']
        all_posts.extend(topics)
        print(f"Fetched page {page}, got {len(topics)} topics")
        page += 1

    save_posts(all_posts)

if __name__ == "__main__":
    main()
