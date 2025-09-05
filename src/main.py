import argparse
from crawler.filesystemcrawler import FileSystemCrawler

CRAWLERS = {
    'fs': FileSystemCrawler
}

class Main:
    def __init__(self, crawler_name, search_term, start_path):
        if crawler_name not in CRAWLERS:
            raise ValueError("Unknown crawler")

        crawler_class = CRAWLERS[crawler_name]
        self.crawler = crawler_class(search_term, start_path)

    def run(self):
        self.crawler.run()

def main():
    parser = argparse.ArgumentParser(description="Choose a crawler and pass a search term and start path.")
    parser.add_argument('crawler', choices=CRAWLERS.keys(), help='Which crawler to run')
    parser.add_argument('search_term', help='Search term to pass to the crawler')
    parser.add_argument('start_path', help='Start path for the crawler')

    args = parser.parse_args()

    app = Main(args.crawler, args.search_term, args.start_path)
    app.run()

if __name__ == "__main__":
    main()
