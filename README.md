# RSS Aggregator

## Configuration

`scoreThreshold` adjust to change minimum required score for a result to be included.

`dateThreshold` adjust to change the minimum date required to be included.

### feeds.txt

List of RSS feeds to query, one per line

### keywords.yml

List of keywords and associated scores, YAML formatted, negatives allowed.

## Dependencies

The following python packages are required:

* yaml
* feedparser
* html2text

## Usage

Set feeds, keywords, and config appropraitely. Then run:

```sh
./main.py
```