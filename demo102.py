import urllib.request
import xml.dom.minidom
URL1 = "https://www.reddit.com/.rss"
file1 = urllib.request.urlopen(URL1)
DOMTree =xml.dom.minidom.parse(file1)
file1.close()
DOMTree
root = DOMTree.documentElement
if root.hasAttribute('xmlns'):
    print("xmlns={}".format(root.getAttribute("xmlns")))
    print("xmlns media={}".format(root.getAttribute("xmlns:media")))
    print("root element tag={}".format(root.tagName))
for c in root.childNodes:
    #print(c.toxml())
    print(c.tagName)
entries = root.getElementsByTagName("entry")
for e in entries:
    print(e.tagName)
    for se in e.childNodes:
        print("..{}".format(se.tagName))
for e in entries:
    title = e.getElementsByTagName("title")[0]
    print("title={}".format(title.childNodes[0].data))
    updated = e.getElementsByTagName("updated")[0]
    print("last update={}".format(updated.childNodes[0].data))
    link = e.getElementsByTagName("link")[0]
    print("link to ={}".format(link.getAttribute('href')))
    author = e.getElementsByTagName("author")[0]
    name = author.getElementsByTagName("name")[0]
    print(f"{author.tagName} has tag {name.tagName} with value {name.childNodes[0].data}")
    print()
    print("-------------------")
    content = e.getElementsByTagName("content")[0]
    print("type = {}".format(content.getAttribute("type")))
    print(content.childNodes[0].data)
    print("-------------------")