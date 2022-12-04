import sys
from bs4 import BeautifulSoup

# Read the HTML file
html_file = sys.argv[1]
with open(html_file, "r") as f:
    html = f.read()

# Parse the HTML file using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# 1. Extract out a div tag with a class that starts with the string "ThreadLayout__NodeWrapper-". 
# Lets call this the main tag.
main = soup.find("div", class_=lambda c: c and c.startswith("ThreadLayout__NodeWrapper-"))

# 2. Inside the "main" tag, delete the divs that have a class that starts with one of the following strings:
# "Pagination__PaginationWrapper-", "ConversationItem__ActionButtons-", "CodeSnippet__ActionBar-" or "Thread__PositionForm-".
for div in main.find_all("div", class_=lambda c: c and c.startswith(("Pagination__PaginationWrapper-",
                                                                     "ConversationItem__ActionButtons-",
                                                                     "CodeSnippet__ActionBar-",
                                                                     "Thread__PositionForm-"))):
    div.decompose()

# 3. For any div with a class starting with the string "Avatar-", remove the style attribute if one exists.
for div in main.find_all("div", class_=lambda c: c and c.startswith("Avatar-")):
    div.attrs.pop("style", None)

# 4. For any "p" tags in the document, apply the style attribute with the value "white-space: pre-wrap;" and 
# strip leading whitespaces in the text found in any child nodes (recursive), if they have any text.
for p in soup.find_all("p"):
    p.attrs["style"] = "white-space: pre-wrap;"
    for text in p.find_all(text=True):
        text.replace_with(text.strip())

# 5. Wrap the main tag in a standard HTML5 document. Include a link at the top (before the main tag), 
# with the text "< Back" linking to the URL "/chatgpt"
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>ChatGPT Transcript</title>
</head>
<body>
    <a href="/chatgpt">&lt; Back</a>
    {}
</body>
</html>
"""

# 6. Output the HTML document to stdout without prettifying it.
print(html_template.format(main))
