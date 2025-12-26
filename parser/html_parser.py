from bs4 import BeautifulSoup

def extract_main_content(html):
    soup = BeautifulSoup(html, "lxml")

    for tag in soup(["nav", "footer", "header", "aside", "script", "style"]):
        tag.decompose()

    return soup.get_text(separator="\n")
