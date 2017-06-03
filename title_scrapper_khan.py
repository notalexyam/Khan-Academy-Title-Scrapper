# Small Script that extracts Khan Academy Titles of the Lessons

import requests
from bs4 import BeautifulSoup

def make_soup(url):
    try:
        html = requests.get(url).content
    except:
        return None
    return BeautifulSoup(html,"html.parser")


def get_titles(base_url): # Get a list of all the text in <div> links 
    soup = make_soup(base_url)
    titles = []
    for title_element in soup.find_all('div', class_='nodeTitle_1lw7ui1'):
        titles.append(title_element.text)
    return titles

if __name__ == "__main__":
    #Math
    print("\n".join(get_titles("https://www.khanacademy.org/test-prep/sat/sat-math-practice")))
    #Newline
    print('\n')
    #English
    print("\n".join(get_titles("https://www.khanacademy.org/test-prep/sat/sat-reading-writing-practice")))