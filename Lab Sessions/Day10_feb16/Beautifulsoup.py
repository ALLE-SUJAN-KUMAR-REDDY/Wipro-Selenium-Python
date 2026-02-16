# 1. Parse HTML – Extract <title> and <h1>

from bs4 import BeautifulSoup
import requests

html = """
<html>
<head>
    <title>Sample Website</title>
</head>
<body>

<h1>Main Heading</h1>
<h2>Sub Heading</h2>
<h3>Section Heading</h3>

<p>This is <b>important</b> paragraph one.</p>
<p>This is paragraph two.</p>

<a href="https://google.com">Google</a>
<a href="https://openai.com">OpenAI</a>

<img src="logo.png" />
<img src="banner.jpg" />

<table border="1">
<tr>
    <th>Name</th>
    <th>Age</th>
</tr>
<tr>
    <td>Alice</td>
    <td>25</td>
</tr>
<tr>
    <td>Bob</td>
    <td>30</td>
</tr>
</table>

</body>
</html>
"""


soup = BeautifulSoup(html, "html.parser")

print("Title:", soup.title.text)
print("H1:", soup.h1.text)


# 2.Extract All Paragraphs

paragraphs = soup.find_all("p")
for p in paragraphs:
    print(p.text)


# 3.Extract All Links and Count

html = '''
<a href="https://google.com">Google</a>
<a href="https://openai.com">OpenAI</a>
'''

soup = BeautifulSoup(html, "html.parser")
links = soup.find_all("a")

print("Total links:", len(links))
for link in links:
    print(link.text, "->", link["href"])


# 4.Extract Attributes

tag = soup.find("a")
print(tag.get("href"))


# 5. Extract First <h2>

html = "<h2>First</h2><h2>Second</h2>"
soup = BeautifulSoup(html, "html.parser")

print(soup.find("h2").text)

# 6. Extract Bold Text

html = "<p>This is <b>bold</b> text</p>"
soup = BeautifulSoup(html, "html.parser")

bold = soup.find("b")
print(bold.text)


# 7. Extract All href Values

html = '''
<a href="link1.com">One</a>
<a href="link2.com">Two</a>
'''

soup = BeautifulSoup(html, "html.parser")

hrefs = [a["href"] for a in soup.find_all("a")]
print(hrefs)

# 8. Get All Text Without Tags

print(soup.get_text(strip=True))

# 9. Extract Title from Website (Live URL)

url = "https://example.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
print("Website title:", soup.title.text)

# 10. Extract All Headings (h1 to h6)

headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

for h in headings:
    print(h.name, ":", h.text)

# 11. Extract Table Data

html = '''
<table>
<tr><th>Name</th><th>Age</th></tr>
<tr><td>Alice</td><td>25</td></tr>
<tr><td>Bob</td><td>30</td></tr>
</table>
'''

soup = BeautifulSoup(html, "html.parser")

rows = soup.find_all("tr")
for row in rows:
    cols = [col.text for col in row.find_all(["td", "th"])]
    print(cols)

# 12. Extract Images

html = '''
<img src="img1.png">
<img src="img2.jpg">
'''

soup = BeautifulSoup(html, "html.parser")

images = soup.find_all("img")
for img in images:
    print(img.get("src"))
