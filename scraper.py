import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Greece"

def retrieve_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    paragraphs = soup.find_all("p")

    citations_paragraphs = []

    for paragraph in paragraphs:
        if paragraph.select("sup i a span"):
            citations_paragraphs.append(paragraph)

    return tuple(citations_paragraphs)

def retrieve_citations(paragraphs):
    citations = []
    for paragraph in paragraphs:
        if "citation needed" in paragraph.text:
            citations.append(paragraph.select("sup i a span"))

    return tuple(citations)

def get_citations_needed_count(url):
    soup = retrieve_soup(url)
    citations = retrieve_citations(list(soup))
    return len(citations)

def get_citations_needed_report(url):
    report = ''

    soup = retrieve_soup(url)
    for item in soup:
        if "citation" in item.text:
            report += item.text
            report += '\n'

    return report

print(get_citations_needed_count(url))
print(get_citations_needed_report(url))