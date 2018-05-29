import re

"""
Using * asterisk - multiple occurrences of the character 
preceding it. Below the first arguement is our regular expression,
the second argument is the string to test. So it matches any part
of the string that starts with "a", ends with a "c" and has
"*" zero or more of "b" in between the two.
"""

print re.findall("ab*c", "ac")      # ['ac']
print re.findall("ab*c", "abcd")    # ['abc']
print re.findall("ab*c", "acc")     # ['ac']
print re.findall("ab*c", "abcac")   # ['abc', 'ac']
print re.findall("ab*c", "abdc")    # []
print re.findall("ab*c", "ABC")     # [] case sensitive

# Using re.IGNORECASE to ignore upper-case and lower-case as regular
# expressions are case-sensitive.
print re.findall("ab*c", "ABC", re.IGNORECASE) # ['ABC]

"""
We can use a period "." to stand for any single character in a 
regular expression. For instance, we could find all the strings 
that contains the letters “a” and “c” separated by a single 
character.
"""

# Using . period - any single occurence
print re.findall("a.c", "abc")      # ['abc']
print re.findall("a.c", "abbc")     # []
print re.findall("a.c", "ac")       # []
print re.findall("a.c", "acc")      # ['acc']

"""
Therefore, putting the term .* inside of a regular expression 
stands for any character being repeated any number of times.
"""

# Combining "." with "*"
print re.findall("a.*c", "abc")     # ['abc']
print re.findall("a.*c", "abbc")    # ['abbc']
print re.findall("a.*c", "ac")      # ['ac']

"""
Usually we will want to use the re.search() function to search 
for a particular pattern inside a string. Calling the group() 
method on a MatchObject will return the first and most inclusive 
result.
"""

# Using re.search()
results = re.search("ab*c", "ABC", re.IGNORECASE)
print results.group()

"""
There is another re function that will come in handy when parsing 
out text: the sub() function. This is short for “substitute” and 
allows us to replace text in a string that matches a regular 
expression with new text (much like the string replace() method). 
The arguments passed to re.sub() are the regular expression, 
followed by the replacement text, then followed by the string.
"""

# example:
a_string = "Everything we do is <replaced> if it is indeed inside <tags>."

# Substitute the tags with 'coming up roses' using the re.sub() method
a_string = re.sub("<.*>", "coming up roses", a_string)
print a_string

"""
Unfortunately this only replaces everything between the first 
occurrence of < and the last occurrence of >. 
Let’s take a look at how to substitute all occurrences of the tags:
"""

another_string = "Everything we do is <replaced> if it is indeed inside <tags>"

# Make sure that both tags are replaced by using the ? to tell
# re.sub() to stop after the first match of '>'
another_string = re.sub("<.*?>", "coming up roses", another_string)
print another_string

"""
"?" means zero or one repititions
Why does adding a ‘?’ to the regular expression make such a big 
difference? The first expression <.*> matches the literal value <, 
followed by zero or more characters, followed by the 
literal value >. It is what’s known as a greedy expression. 
It finds the first < and the last > and matches on all of that, 
even if there are other < and > characters in between.
The second expression <.?> matches the literal value <, 
followed by zero or more characters, followed by the 
literal value >. However, the ? makes the expression operate in 
what’s known as lazy mode. This means that < and > characters 
between the outer pair are matched on, raising the possibility of 
finding multiple pairs of < and >.
"""