import json
from tools.scrape_news import Article, ArticleEncoder

def load_scraped(path: str) -> list[Article]:
    categories = {}
    with open(path, "r") as f:
        categories = json.load(f)
    
    articles = []
    for category in categories:
        a = map(Article.from_dict, categories[category])
        articles.extend(a)
        
    return articles
