import os
from bs4 import BeautifulSoup # BeautifulSoup4 package
from urllib2 import urlopen

# Grab the HTML from a web page just like we did
# in the first example
my_address = "https://docs.python.org/2/whatsnew/2.7.html"
html_page = urlopen(my_address)
html_text = html_page.read()

# Pass the HTML to the BeautifulSoup constructor.
# The second argument tells beautifulsoup which parser to use.
soup = BeautifulSoup(html_text, "lxml")

# get_text() from beautifulsoup, extracts the text removing any HTML
# tags automatically
print soup.get_text().encode("utf-8")

# There are a lot of extra balnk lines left, but these can be taken out.
# one way of doing this is below (we import "os" module above)
result = soup.get_text().encode("utf-8")
text = os.linesep.join([s for s in result.splitlines() if s])
print text