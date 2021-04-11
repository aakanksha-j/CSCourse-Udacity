# Here we modify the search engine data structure from a list to a dictionary.
# Mentioning all the functions where the change is needed.

# no change in get_all_links function
def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url) page = page[endpos:]
        else:
            break
    return links

# change in crawl_web
def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = {} # index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index

# no change in add_page_to_index function
def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

# change in add_to_index
def add_to_index(index, keyword, url):
    if keyword in index: # no for loop.
        index[keyword].append(url)
    else:
        # not found, add new keyword to index
        index[keyword]=[url] # dictionary assignment of new keyword

# change in lookup
def lookup(index, keyword):
    if keyword in index: # no for loop
        return index[keyword]
    else:
        return None
