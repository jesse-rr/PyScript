import os

class FileSystemCrawler:
    def __init__(self, search_term, start_path):
        self.search_term = search_term
        self.start_path = start_path
        self.matches = []

    def recursive_travel(self, path):
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                self.recursive_travel(full_path)
            elif self.search_term in item:
                self.matches.append(full_path)

    def run(self):
        print(f"Running {self.__class__.__name__} with search term {self.search_term}")
        self.recursive_travel(self.start_path)
        print(f"Found {len(self.matches)} file(s):")
        for match in self.matches:
            print(f" - {match}")