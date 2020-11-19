# Search engine

## Goal

Develop a search engine with auto complete/suggest

## Tools

### Docker

[Install Docker](https://docs.docker.com/get-docker/)

### ElasticSearch

* Pull the Docker image

```sh
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.10.0
```

* Start a single node cluster

```sh
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.10.0
```

* Create Index for auto-suggest functionality
  * *Edge n-gram Tokenizer*: To match partial/full keywords. (We are using this here)
  * *Completion Suggester*: Basic autocomplete without spell check; Good performance.
