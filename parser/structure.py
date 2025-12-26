from bs4 import BeautifulSoup


def extract_sections(html):
    soup = BeautifulSoup(html, "lxml")
    sections = []

    for h in soup.find_all(["h1", "h2", "h3"]):
        sections.append({
            "title": h.get_text(strip=True),
            "level": h.name,
            "content": h.find_next_sibling("p").get_text(strip=True)
            if h.find_next_sibling("p") else ""
        })
    return sections
