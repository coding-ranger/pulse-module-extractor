from collections import defaultdict

def infer_modules(sections):
    modules = defaultdict(list)

    current_module = None
    for sec in sections:
        if sec["level"] == "h1":
            current_module = sec["title"]
        elif sec["level"] in ["h2", "h3"] and current_module:
            modules[current_module].append(sec)

    return modules
