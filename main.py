#!/usr/bin/env python3

import yaml
import feedparser
import time
from datetime import datetime, timedelta
import html2text

feedURLs = []
weightedKeywords = {}
scoreThreshold = 1
dateThreshold = datetime.now() - timedelta(days=7)

with open('feeds.txt') as f:
    feedURLs = f.readlines()

with open('keywords.yml') as f:
    weightedKeywords = yaml.load(f, Loader=yaml.FullLoader)

results = []

for url in feedURLs:
    feed = feedparser.parse(url)
    for entry in feed.entries:
        if not hasattr(entry, 'published_parsed'):
            continue
            
        date = datetime.fromtimestamp(time.mktime(entry.published_parsed))
        if date > dateThreshold:
            continue

        desc = html2text.html2text(entry.title + ' ' +entry.description).lower()
        keywords = list(dict.fromkeys(desc.split(' ')))
        score = 0
        for k in keywords:
            if k in weightedKeywords:
                score += weightedKeywords[k]
        if score >= scoreThreshold:
            entry.score = score
            results.append(entry)

for result in results:
    print("%d: %s\n\tPublished: %s\n\tURL: %s" % (result.score, result.title, result.published, result.link))
