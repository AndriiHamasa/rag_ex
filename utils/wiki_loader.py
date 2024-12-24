import wikipediaapi


wiki = wikipediaapi.Wikipedia(
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.89 Safari/537.36"
)

def load_wikipedia_article(title: str) -> str:
    print("title in func load_wikipedia_article: ", title)
    page = wiki.page(title)
    if page.exists():
        return page.text

    raise Exception(f"Wikipedia article with title: '{title}' was not found")

load_wikipedia_article("Wikipedia:Popular pages")