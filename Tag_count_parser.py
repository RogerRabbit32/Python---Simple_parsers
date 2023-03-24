import requests
from bs4 import BeautifulSoup

# Make a request to the website and get the HTML content
url = 'https://jetlend.ru/'
response = requests.get(url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Count the number of tags and their attributes
tags = {}
attributes = {}
for tag in soup.find_all():
    tag_name = tag.name
    if tag_name in tags:
        tags[tag_name] += 1
    else:
        tags[tag_name] = 1
    for attr in tag.attrs:
        if tag_name not in attributes:
            attributes[tag_name] = {}
        attr_name = attr
        if attr_name in attributes[tag_name]:
            attributes[tag_name][attr_name] += 1
        else:
            attributes[tag_name][attr_name] = 1

# Print the results
print("Tag Counts:")
for tag_name, count in tags.items():
    print(f"{tag_name}: {count}")
total_tags = sum(tags.values())
print("\nTotal tags:", total_tags, "\n" * 3)

print("Attribute Counts:")
for tag_name, attrs in attributes.items():
    print(tag_name)
    for attr_name, count in attrs.items():
        print(f"\t{attr_name}: {count}")
    print(f"\tTotal: {sum(attrs.values())}")
total_attributes = sum([sum(attrs.values()) for attrs in attributes.values()])
print("\nTotal attributes:", total_attributes)
