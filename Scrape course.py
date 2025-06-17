import requests
from bs4 import BeautifulSoup

BASE_URL = "https://tds.s-anand.net/#/2025-01/"
RAW_URL = "https://tds.s-anand.net/2025-01/"

def scrape_course_content():
    """
    Scrapes the course content from the TDS lecture pages.
    Returns a dictionary where keys are lecture titles and values are cleaned text content.
    """
    response = requests.get(RAW_URL + "toc.json")  # loads the table of contents
    if response.status_code != 200:
        raise Exception("Failed to fetch course table of contents")
    
    toc = response.json()
    course_data = {}

    for lecture in toc:
        slug = lecture.get("slug")
        title = lecture.get("title")
        url = f"{RAW_URL}{slug}.html"

        lecture_resp = requests.get(url)
        if lecture_resp.status_code != 200:
            print(f"Could not fetch {url}")
            continue

        soup = BeautifulSoup(lecture_resp.text, "html.parser")
        content_div = soup.find("div", class_="markdown-body")

        if content_div:
            content_text = content_div.get_text(separator="\n").strip()
            course_data[title] = content_text

    return course_data


if __name__ == "__main__":
    data = scrape_course_content()
    for title, text in data.items():
        print(f"=== {title} ===\n{text[:500]}...\n")
