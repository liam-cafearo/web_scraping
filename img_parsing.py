from bs4 import BeautifulSoup
from urllib2 import urlopen

my_address = "http://www.irishtimes.com/"
html_page = urlopen(my_address)
html_text = html_page.read()
soup = BeautifulSoup(html_text, "html.parser")

# Put all image elements in a list, each 'img tag gets stored
# as a dictionary.
images = soup.find_all("img")

# Iterate over 'images' list and
# print the 'src' of each image
for img in images:
    # The list stores each img found as a dictionary therefore
    # you can select the key 'src'
    print img['src']