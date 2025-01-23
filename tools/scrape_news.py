import argparse
import asyncio
import json
import re
import requests

from bs4 import BeautifulSoup
from pathlib import Path
from typing import Optional

class Article:
    def __init__(self, title: str, content: str, category: str):
        self.title = title
        self.content = content
        self.category = category
        
    @staticmethod
    def from_dict(obj: dict[str, str]) -> "Article":
        return Article(
            obj["title"],
            obj["content"],
            obj["category"]
        )


class ArticleEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Article):
            return obj.__dict__
        return super().default(obj)


class BBCNewsScraper:
    def __init__(
        self, category_links: dict[str, str], 
        article_link_pattern: str = "https:\/\/www\.bbc\.com\/amharic\/articles\/([a-zA-Z0-9]+)"
        ):
        self.category_links = category_links
        self.article_link_pattern = article_link_pattern
    
    async def __get_soup(self, url: str) -> BeautifulSoup:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
        }
        html = await asyncio.to_thread(requests.get, url, headers=headers)
        htmlText = html.text.encode(html.encoding).decode("utf-8")
        soup = BeautifulSoup(htmlText, "html.parser")

        return soup
    
    def __get_num_pages(self, soup: BeautifulSoup) -> int:
        items = soup.find_all("nav")[-1].find_all("li")
        max_page = max(int(item.string) for item in items if item.string and item.string.isnumeric())
        return max_page
    
    def __get_page_links(self, category_link: str, num_pages: int) -> list[str]:
        return [f"{category_link}?page={page}" for page in range(1, num_pages + 1)]
    
    async def __get_article_links(self, page_link: str) -> list[str]:
        soup = await self.__get_soup(page_link)
        all_links = [item["href"] for item in soup.find_all("a") if item["href"]]
        def matcher(link):
            if re.search(self.article_link_pattern, link):
                return True
            return False
        return [str(link) for link in all_links if matcher(link)]
    
    async def get_article(self, article_link: str, category: str = "other") -> Article:
        soup = await self.__get_soup(article_link)
        title = str(soup.find("h1").string)
        main = soup.find("main")
        paragraphs = main.find_all("p")
        texts = [p.string for p in paragraphs if p.string]
        content = "\n".join(texts)
        
        return Article(title, content, category)
    
    async def scrape_page(self, page_link: str, category: str = "other") -> list[Article]:
        article_links = await self.__get_article_links(page_link)
        tasks = [self.get_article(link, category) for link in article_links]
        articles = await asyncio.gather(*tasks)
            
        return articles
    
    async def __scrape_category(self, category: str, save_dir: Optional[str] = None) -> list[Article]:
        if category not in self.category_links:
            raise Exception("category must be present in predefined categories")
        link = self.category_links[category]
        soup = await self.__get_soup(link)
        num_pages = self.__get_num_pages(soup)
        articles = []
        for page_link in self.__get_page_links(link, num_pages):
            articles.extend(await self.scrape_page(page_link, category))
            
        if save_dir:
            self.__save_json(f"{save_dir}/{category}.json", articles)
        
        print(f"Scraped category '{category}'")
        return articles

    def __save_json(self, path: str, obj: any):
        with open(path, "w") as f:
            json.dump(obj, f, cls=ArticleEncoder)
        
    async def scrape(self, save_json: bool, save_dir: str = "./") -> dict[str, list[Article]]:
        res = {}
        try:
            for category in self.category_links:
                res[category] = await self.__scrape_category(category, save_dir)
        except Exception as e:
            print("error", e)
            
        if save_json:
            self.__save_json(f"{save_dir}/bbc_news.json", res)

        return res
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--save-dir", type=Path, required=False, default="scraped_data")
    
    args = parser.parse_args()
    save_dir = args.save_dir
    
    scraper = BBCNewsScraper({
        "Politics": "https://www.bbc.com/amharic/topics/cg7265pj1jvt",
        "Sports": "https://www.bbc.com/amharic/topics/cdr56g2x71dt",
        "Business": "https://www.bbc.com/amharic/topics/cnq6815jj3xt",
        "Technology": "https://www.bbc.com/amharic/topics/c06gq8wx467t"
    })
    
    asyncio.run(scraper.scrape(save_json=True, save_dir=save_dir))
