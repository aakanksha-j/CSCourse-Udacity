def crawl_web(seed):
    toCrawl=[seed]
    crawled=[]
    index=[]
    while toCrawl:
        page=toCrawl.pop()
        if page not in crawled:
            content=get_page(page)
            add_page_to_index(index,page,content)
            union(toCrawl, get_all_links(content))
            crawled.append(page)
    print index
    return index

def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword, [url]])

def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

def get_page(url):
    if url=="https://udacity.github.io/cs101x/index.html":
        return """<html>
<body>
This is a test page for learning to crawl!
<p>
It is a good idea to
<a href="https://udacity.github.io/cs101x/crawling.html">learn to crawl</a>
before you try to
<a href="https://udacity.github.io/cs101x/walking.html">walk</a> or
<a href="https://udacity.github.io/cs101x/flying.html">fly</a>.
</p>
</body>
</html>"""
    elif url=="https://udacity.github.io/cs101x/crawling.html":
        return """
<html>
<body>
I have not learned to crawl yet, but I am quite good at
<a href="https://udacity.github.io/cs101x/kicking.html">kicking</a>.
</body>
</html>
               """
    elif url=="https://udacity.github.io/cs101x/walking.html":
        return """
<html>
<body>
I can't get enough
<a href="https://udacity.github.io/cs101x/index.html">crawling</a>!
</body>
</html>
               """
    elif url=="https://udacity.github.io/cs101x/flying.html":
        return """
<html>
<body>
The magic words are Squeamish Ossifrage!
</body>
</html>
               """
    elif url=="https://udacity.github.io/cs101x/kicking.html":
        return """
<html>
<body>
<b>Kick! Kick! Kick!</b>
</body>
</html>
               """
    return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def lookup(index,keyword):

    for entry in index:
        if entry[0]==keyword:
            return entry[1]
    return []

index=crawl_web("https://udacity.github.io/cs101x/index.html")
print lookup(index,'are')
