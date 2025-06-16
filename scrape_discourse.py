import requests
import json

BASE_URL = "https://discourse.onlinedegree.iitm.ac.in"
CATEGORY_SLUG = "c/courses/tds-kb"  # The category path
OUTPUT_FILE = "discourse_topics.json"

def fetch_topics(page=0):
    url = f"{BASE_URL}/{CATEGORY_SLUG}.json?page={page}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def save_topics(topics, filename=OUTPUT_FILE):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(topics, f, indent=2, ensure_ascii=False)

def main():
    all_topics = []
    page = 0
    while True:
        data = fetch_topics(page=page)
        if not data or not data.get('topic_list', {}).get('topics'):
            print("No more topics found, stopping.")
            break
        topics = data['topic_list']['topics']
        all_topics.extend(topics)
        print(f"Fetched page {page}, got {len(topics)} topics")
        page += 1

    save_topics(all_topics)
    print(f"Saved total {len(all_topics)} topics to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
