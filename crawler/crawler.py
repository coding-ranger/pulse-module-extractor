from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from crawler.fetcher import fetch_url

def crawl(base_url, max_pages=50):
    visited = set()
    to_visit = [base_url]
    pages = {}

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)
        if url in visited:
            continue

        html = fetch_url(url)
        if not html:
            continue

        visited.add(url)
        pages[url] = html

        soup = BeautifulSoup(html, "lxml")
        for link in soup.find_all("a", href=True):
            full = urljoin(base_url, link["href"])
            if base_url in full and full not in visited:
                to_visit.append(full)

    return pages
