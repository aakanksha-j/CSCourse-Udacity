def crawl_web(seed):
    toCrawl=[seed]
    crawled=[]
    #print "seedpage: "+seed
    #print "toCrawl in beginning:",toCrawl
    while toCrawl!=[]:
        page = toCrawl.pop()
        #print "3",page
        #print "4",toCrawl
        if page not in crawled:
            toCrawl=union(toCrawl,get_all_links(get_page(page)))
            #print "5",toCrawl
            #print "10", page
            #print "11", crawled
            crawled.append(page)
            #print "6",crawled
    return crawled

def get_page(url):
    if url== "https://udacity.github.io/cs101x/index.html":
        return '<html><head></head><body>This is a test page for learning to crawl!<p>It is a good idea to<a href="https://udacity.github.io/cs101x/crawling.html">learn to crawl</a>before you try to<a href="https://udacity.github.io/cs101x/walking.html">walk</a> or<a href="https://udacity.github.io/cs101x/flying.html">fly</a>.</p></body></html>'
    if url== "https://udacity.github.io/cs101x/crawling.html":
        return '<html><body>I have not learned to crawl yet, but I am quite good at <a href="https://udacity.github.io/cs101x/kicking.html">kicking</a>.</body></html>'
    if url== "https://udacity.github.io/cs101x/walking.html":
        return '<html><body>I can\'t get enough <a href="https://udacity.github.io/cs101x/index.html">crawling</a>!</body></html>'
    if url== "https://udacity.github.io/cs101x/flying.html":
        return '<html><body>The magic words are Squeamish Ossifrage!</body></html>'
    if url== "https://udacity.github.io/cs101x/kicking.html":
        return '<html><body><b>Kick! Kick! Kick!</b></body></html>'

def get_next_target(page):
    #print "inside get_next_target"
    start_link=page.find('<a href=')
    #print start_link
    if start_link==-1:
        return None,0
    start_quote=page.find('"', start_link)
    #print start_quote
    end_quote=page.find('"', start_quote+1)
    #print end_quote
    url=page[start_quote+1:end_quote]
    #print "9",url
    return url, end_quote

def get_all_links(page):
    linksFromOnePage=[]
    while True:
        url,endpos=get_next_target(page)
        if url:
            linksFromOnePage.append(url)
            page=page[endpos:]
            #print "7",linksFromOnePage
        else:
            break
    return linksFromOnePage

def union(p,q):
    for e in q:
        if e not in p:
            #print "8",e
            p.append(e)
    return p

crawledLinks= crawl_web("https://udacity.github.io/cs101x/index.html")
for i in crawledLinks:
    print i
