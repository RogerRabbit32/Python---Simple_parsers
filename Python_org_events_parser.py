import requests
from bs4 import BeautifulSoup as Bs

python_main_page = requests.get('https://www.python.org/')
page_html = Bs(python_main_page.content, 'html.parser')

print()

for event in page_html.select('.medium-widget.event-widget.last > .shrubbery > .menu > li'):
    event_name = event.select('a')
    event_date = event.select('time')
    print(event_date[0].text, event_name[0].text, 'https://www.python.org' + event.find('a').get('href'))
