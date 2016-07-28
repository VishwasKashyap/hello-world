from bs4 import BeautifulSoup
import requests

url = 'http://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
Soup = BeautifulSoup(r.text)
for story_heading in Soup.find_all(class_ = 'story-heading'):
    if story_heading.a:
        print(story_heading.a.text.replace("\n"," ").strip())
    else:
        print(story_heading.contents[0].strip())
