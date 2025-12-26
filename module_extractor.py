import argparse
from crawler.crawler import crawl
from parser.structure import extract_sections
from inference.module_infer import infer_modules
from inference.description_gen import summarize

def run(urls):
    result = []

    for url in urls:
        pages = crawl(url)
        all_sections = []
        for html in pages.values():
            all_sections.extend(extract_sections(html))

        modules = infer_modules(all_sections)

        for mod, subs in modules.items():
            module_desc = summarize(" ".join(s["content"] for s in subs))
            submods = {
                s["title"]: summarize(s["content"])
                for s in subs
            }

            result.append({
                "module": mod,
                "Description": module_desc,
                "Submodules": submods
            })

    return result
