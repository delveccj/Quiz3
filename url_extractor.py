# url_extractor.py
from bs4 import BeautifulSoup

def extract_urls_from_html(file_path):
    urls = []
    with open(file_path, 'r') as file:
        content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        for link in soup.find_all('a'):
            urls.append(link.get('href'))
    return urls

if __name__ == "__main__":
    html_file = "example.html"
    urls = extract_urls_from_html(html_file)
    print(urls)
