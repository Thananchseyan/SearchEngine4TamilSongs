import json
from elasticsearch import Elasticsearch
from query import basicSearch, standardAnalyzer

#index of the csv
INDEX = 'metaphor'
#user name and pw for the elastic search
client = Elasticsearch("https://localhost:9200", verify_certs=False,
                   http_auth=['elastic', 'aX3KZ=b5kZca3CxGrlVH'],)

#do the wildcardSearch
def search_advanced_query(query):
    hits = {
       "query": {
            "wildcard": {
            "Metaphor": {
                "value": "*"+query
            }
            }
        }
    }
    response = client.search(index=INDEX, body=hits)
    return response

def basicSearch(query):
    query_body = basicSearch(query)
    response = client.search(index=INDEX, body=query_body)
    return response

#autogrenerating the queries
def basic_search_with_fields(fields):

    hit = {}
    hit["query"] = {}
    hit["query"]["bool"] = {}
    hit["query"]["bool"]["must"] = []
    
    for field in fields:
        if field == 'Year':
            hit["query"]["bool"]["must"].append({"range":{field:fields[field]}})
        else:

            hit["query"]["bool"]["must"].append({"term":{field:fields[field]}})

    response = client.search(index=INDEX, body=hit)
    return response


def multiMatchSearch(query, fields=['title', 'song_lyrics'], operator='or'):
    hit = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": fields,
                "operator": operator,
                "type": "best_fields"
            }
        }
    }
    return hit


def aggregatedMultiMatchSearch(query, fields=['title', 'song_lyrics'], operator='or'):
    hit = {
        "size": 500,
        "explain": True,
        "query": {
            "multi_match": {
                "query": query,
                "fields": fields,
                "operator": operator,
                "type": "best_fields"
            }
        },
        "aggs": {
            "Genre Filter": {
                "terms": {
                    "field": "genre.keyword",
                    "size": 10
                }
            },
            "Music Filter": {
                "terms": {
                    "field": "music.keyword",
                    "size": 10
                }
            },
            "Artist Filter": {
                "terms": {
                    "field": "artist.keyword",
                    "size": 10
                }
            },
            "Lyrics Filter": {
                "terms": {
                    "field": "lyrics.keyword",
                    "size": 10
                }
            }
        }
    }

    hit = json.dumps(hit)
    return hit


def aggregatedSearch():
    hit = {
        "size": 0,
        "aggs": {
            "Category Filter": {
                "terms": {
                    "field": "genre",
                    "size": 10
                }
            }
        }
    }
    return hit

def aggregatedMultimatchSortingSearch(query, fields, operator='or', pagi=10):

    hit = {
        "size": pagi,
        "sort": [
            {"views": {"order": "desc"}},
        ],
        "query": {
            "multi_match": {
                "query": query,
                "fields": fields,
                "operator": operator,
                "type": "best_fields"
            }
        },
        "aggs": {
            "Genre Filter": {
                "terms": {
                    "field": "வகை.keyword",
                    "size": 10
                }
            },
            "Music Filter": {
                "terms": {
                    "field": "இசையமைப்பாளர்.keyword",
                    "size": 10
                }
            },
            "Artist Filter": {
                "terms": {
                    "field": "பாடியவர்கள்.keyword",
                    "size": 10
                }
            },
            "Lyrics Filter": {
                "terms": {
                    "field": "பாடல்வரிகள்.keyword",
                    "size": 10
                }
            }
        }
    }
    hit = json.dumps(hit)
    return hit