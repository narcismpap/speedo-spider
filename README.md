# Speedo
Hello World, meet Speedo! The world's least sophsisticated non-recursive gevent-based Python crawler.

## Usage
```
docker run --rm -v $(pwd)/crawler:/speedo/code speedo:latest "http://news.ycombinator.com"
```

## Purpose
This was a fun coding challenge with a four hour deadline.

## Requirements
Web Crawler using python that crawls a single user-provided domain. After crawling, it should print links between pages.


## Commands
```
# run demo application against Hacker News
make run

# rebuild docker container and tag image
make build

# run unit tests
make test

# run flake8
make lint
```

# Todo

* [ ] fix unit testing fixtures, looks like double monkey patching by gevent and mocket has undefined behavior
* [ ] exponential backoff capabilities

# Example Output

```
[I] Crawling http://news.ycombinator.com
[+] Fetching robots.txt
[I] robots.txt processed
[I] Worker:1 processing L1 http://news.ycombinator.com
[I] Worker #2 Tasks completed
[I] Worker #3 Tasks completed
[I] Controller Tasks completed
[I] Worker #1 Tasks completed


[SUMMARY]
Crawled:     1 pages
Discovered:  129 links
Responses:   1 requests
Errors:      0 requests


[HIERARCHY]
| http://news.ycombinator.com
| --> http://news.ycombinator.com/vote?id=26395361&how=up&goto=news
| --> http://news.ycombinator.com/hide?id=26387100&goto=news
| --> http://news.ycombinator.com/vote?id=26395138&how=up&goto=news
| --> http://news.ycombinator.com/user?id=dimtion
| --> http://news.ycombinator.com/newcomments
| --> http://news.ycombinator.com/hide?id=26398960&goto=news
| --> http://news.ycombinator.com/hide?id=26400053&goto=news
| --> http://news.ycombinator.com/item?id=26394564
| --> http://news.ycombinator.com/from?site=github.com/evanw
| --> http://news.ycombinator.com/lists
| --> http://news.ycombinator.com/from?site=realtimerendering.com
| --> http://news.ycombinator.com/from?site=findka.com
| --> http://news.ycombinator.com/news?p=2
| --> http://news.ycombinator.com/item?id=26399377
| --> http://news.ycombinator.com/item?id=26399672
| --> http://news.ycombinator.com/from?site=bloomberg.com
| --> http://news.ycombinator.com/from?site=vaex.io
| --> http://news.ycombinator.com/from?site=github.blog
| --> http://news.ycombinator.com/from?site=modernmechanix.com
| --> http://news.ycombinator.com/from?site=plover.com
| --> http://news.ycombinator.com/from?site=bbc.co.uk
| --> http://news.ycombinator.com/front
| --> http://news.ycombinator.com/from?site=quantamagazine.org
| --> http://news.ycombinator.com/from?site=lever.co
| --> http://news.ycombinator.com/vote?id=26399733&how=up&goto=news
| --> http://news.ycombinator.com/hide?id=26399672&goto=news
| --> http://news.ycombinator.com/from?site=washingtonpost.com
| --> http://news.ycombinator.com/item?id=26398767
| --> http://news.ycombinator.com/vote?id=26394564&how=up&goto=news
| --> http://news.ycombinator.com/vote?id=26387100&how=up&goto=news
| --> http://news.ycombinator.com/item?id=26397924
| --> http://news.ycombinator.com/hide?id=26398003&goto=news
| --> http://news.ycombinator.com/item?id=26387100
| --> http://news.ycombinator.com/from?site=schneier.com
| --> http://news.ycombinator.com/show
| --> http://news.ycombinator.com/from?site=toastytech.com
| --> http://news.ycombinator.com/item?id=26400053
| --> http://news.ycombinator.com/hide?id=26396978&goto=news
| --> http://news.ycombinator.com/vote?id=26398767&how=up&goto=news
| --> http://news.ycombinator.com/hide?id=26399377&goto=news
| --> http://news.ycombinator.com/from?site=terraaeon.com
| --> http://news.ycombinator.com/user?id=Tomte
| --> http://news.ycombinator.com/user?id=Fiveplus
| --> http://news.ycombinator.com/vote?id=26398197&how=up&goto=news
| --> http://news.ycombinator.com/hide?id=26398197&goto=news
| --> http://news.ycombinator.com/item?id=26393824
| --> http://news.ycombinator.com/hide?id=26395361&goto=news
| --> http://news.ycombinator.com/vote?id=26398870&how=up&goto=news
| --> http://news.ycombinator.com/vote?id=26399377&how=up&goto=news
| --> http://news.ycombinator.com/vote?id=26400280&how=up&goto=news
| --> http://news.ycombinator.com/newsguidelines.html
| --> http://news.ycombinator.com/hide?id=26399758&goto=news
| --> http://news.ycombinator.com/item?id=26381829
| --> http://news.ycombinator.com/item?id=26396671
| --> http://news.ycombinator.com/item?id=26400280
| --> http://news.ycombinator.com/hide?id=26393795&goto=news
| --> http://news.ycombinator.com/vote?id=26398518&how=up&goto=news
| --> http://news.ycombinator.com/hide?id=26400089&goto=news
| --> http://news.ycombinator.com/from?site=hanami.run
| --> http://news.ycombinator.com/from?site=nytimes.com
| --> http://news.ycombinator.com/item?id=26395138
| --> http://news.ycombinator.com/vote?id=26396978&how=up&goto=news
| --> http://news.ycombinator.com/from?site=ledru.info
| --> http://news.ycombinator.com/item?id=26381768
| --> http://news.ycombinator.com/item?id=26399733
| --> http://news.ycombinator.com/hide?id=26398518&goto=news
| --> http://news.ycombinator.com/user?id=LinuxBender
| --> http://news.ycombinator.com/login?goto=news
| --> http://news.ycombinator.com/hide?id=26396798&goto=news
| --> http://news.ycombinator.com/item?id=26375307
| --> http://news.ycombinator.com/hide?id=26396142&goto=news
| --> http://news.ycombinator.com/user?id=dcu
| --> http://news.ycombinator.com/user?id=ddtaylor
| --> http://news.ycombinator.com/hide?id=26381768&goto=news
| --> http://news.ycombinator.com/user?id=bezelbuttons
| --> http://news.ycombinator.com/hide?id=26381829&goto=news
| --> http://news.ycombinator.com/user?id=jacobobryant
| --> http://news.ycombinator.com/user?id=ot
| --> http://news.ycombinator.com/item?id=26399758
| --> http://news.ycombinator.com/vote?id=26396671&how=up&goto=news
| --> http://news.ycombinator.com/from?site=restofworld.org
| --> http://news.ycombinator.com/item?id=26393795
| --> http://news.ycombinator.com/user?id=grecy
| --> http://news.ycombinator.com/ask
| --> http://news.ycombinator.com/user?id=WuTangCFO
| --> http://news.ycombinator.com/user?id=luu
| --> http://news.ycombinator.com/hide?id=26398870&goto=news
| --> http://news.ycombinator.com/security.html
| --> http://news.ycombinator.com/from?site=catern.com
| --> http://news.ycombinator.com/user?id=tosh
| --> http://news.ycombinator.com/hide?id=26395138&goto=news
| --> http://news.ycombinator.com/submit
| --> http://news.ycombinator.com/hide?id=26400280&goto=news
| --> http://news.ycombinator.com/user?id=maartenbreddels
| --> http://news.ycombinator.com/item?id=26398003
| --> http://news.ycombinator.com/vote?id=26399224&how=up&goto=news
| --> http://news.ycombinator.com/hide?id=26396671&goto=news
| --> http://news.ycombinator.com/newsfaq.html
| --> http://news.ycombinator.com/user?id=prostoalex
| --> http://news.ycombinator.com/jobs
| --> http://news.ycombinator.com/user?id=leoschwartz
| --> http://news.ycombinator.com/item?id=26399224
| --> http://news.ycombinator.com/from?site=youtube.com
| --> http://news.ycombinator.com/vote?id=26399746&how=up&goto=news
| --> http://news.ycombinator.com/item?id=26396594
| --> http://news.ycombinator.com/vote?id=26396798&how=up&goto=news
| --> http://news.ycombinator.com/user?id=JimWestergren
| --> http://news.ycombinator.com/hide?id=26396594&goto=news
| --> http://news.ycombinator.com/item?id=26399746
| --> http://news.ycombinator.com/from?site=twitter.com/isostandards
| --> http://news.ycombinator.com/vote?id=26400089&how=up&goto=news
| --> http://news.ycombinator.com/from?site=lostartpress.com
| --> http://news.ycombinator.com/from?site=github.com/torvalds
| --> http://news.ycombinator.com/vote?id=26381829&how=up&goto=news
| --> http://news.ycombinator.com/hide?id=26397924&goto=news
| --> http://news.ycombinator.com/item?id=26395361
| --> http://news.ycombinator.com/hide?id=26399224&goto=news
| --> http://news.ycombinator.com/news
| --> http://news.ycombinator.com/vote?id=26397924&how=up&goto=news
| --> http://news.ycombinator.com/user?id=mknippen
| --> http://news.ycombinator.com/vote?id=26393795&how=up&goto=news
| --> http://news.ycombinator.com/vote?id=26393824&how=up&goto=news
| --> http://news.ycombinator.com/user?id=catern
| --> http://news.ycombinator.com/hide?id=26399733&goto=news
| --> http://news.ycombinator.com/user?id=tasn
| --> http://news.ycombinator.com/item?id=26396142
| --> http://news.ycombinator.com/item?id=26398518
| --> http://news.ycombinator.com/from?site=abhijitbhaduri.com
| --> http://news.ycombinator.com/hide?id=26394564&goto=news
| --> http://news.ycombinator.com/user?id=swyx
| --> http://news.ycombinator.com/hide?id=26398767&goto=news
| --> https://news.ycombinator.com
| --> http://news.ycombinator.com/vote?id=26398960&how=up&goto=news
| --> http://news.ycombinator.com/vote?id=26381768&how=up&goto=news
| --> http://news.ycombinator.com/vote?id=26399758&how=up&goto=news
| --> http://news.ycombinator.com/vote?id=26396142&how=up&goto=news
| --> http://news.ycombinator.com/item?id=26396978
| --> http://news.ycombinator.com/from?site=diahook.com
| --> http://news.ycombinator.com/user?id=diodorus
| --> http://news.ycombinator.com/user?id=blinding-streak
| --> http://news.ycombinator.com/hide?id=26375307&goto=news
| --> http://news.ycombinator.com/user?id=bertdb
| --> http://news.ycombinator.com/item?id=26398197
| --> http://news.ycombinator.com/item?id=26396798
| --> http://news.ycombinator.com/item?id=26398870
| --> http://news.ycombinator.com/from?site=theroadchoseme.com
| --> http://news.ycombinator.com/vote?id=26400053&how=up&goto=news
| --> http://news.ycombinator.com/item?id=26398960
| --> http://news.ycombinator.com/item?id=26400089
| --> http://news.ycombinator.com/newest
| --> http://news.ycombinator.com/user?id=BlackVanilla
| --> http://news.ycombinator.com/vote?id=26399672&how=up&goto=news
| --> http://news.ycombinator.com/vote?id=26396594&how=up&goto=news
| --> http://news.ycombinator.com/hide?id=26399746&goto=news
| --> http://news.ycombinator.com/vote?id=26375307&how=up&goto=news
| --> http://news.ycombinator.com/hide?id=26393824&goto=news
| --> http://news.ycombinator.com/from?site=dougallj.github.io
| --> http://news.ycombinator.com/user?id=todsacerdoti
[DONE]
```

2021, London.