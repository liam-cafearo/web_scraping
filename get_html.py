# Import the urlopen function. We need this to read in the HTML
from urllib2 import urlopen

# Set a URL that we'll try to grab some HTML from.
url = "https://en.wikipedia.org/wiki/Web_scraping"

# Open the URL and read the HTML content into a string variable.
html_page = urlopen(url)
html_text = html_page.read()

# Set the range that we want filter on.
# In this instance everything between the <title></title> tags
start_tag = "<title>"
end_tag = "</title>"

"""
Search for the tags.

The html_text.find() function will give us the index of the very
first '<' character that matches the string that we pass through.
We want to search for everything from the end of the tag -
i.e. ">This text"
To achieve this we'll add the length of the 'start_tag' to the index of '<'
character.

This won't be necessary for the end tag. We just need the index for the '<'
character.
"""
# By adding the length of the start_tag it means the index starts
# after the start tag so that it doesn't include 
# the opening <title> tag.
start_index = html_text.find(start_tag) + len(start_tag)
end_index = html_text.find(end_tag)

# Print everything between the two indexes in html_text
print html_text[start_index:end_index]