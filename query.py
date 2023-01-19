#search for lyricist
def composerSearch(query):
    resQue = {
        "query": {
            "match": {
                "Composer": {
                    "query": query
                }
            }
        }
    }
    return resQue
#search for lyricist
def lyricistSearch(query):
    resQue = {
        "query": {
            "match": {
                "lyricist ": {
                    "query": query
                }
            }
        }
    }
    return resQue
#search for the hero
def heroSearch(query):
    resQue = {
        "query": {
            "match": {
                "Star": {
                    "query": query
                }
            }
        }
    }
    return resQue
def standardAnalyzer(query):

    resQue = {
        "analyzer": "standard",
        "text": query
    }
    return resQue
#query for the basic search
def basicSearch(searchword):
    resQue = {
        "query": {
            "query_string": {
                "query": searchword
            }
        }
    }
    return resQue

def year_range_search(query):
    q={
        "query": {
    "range": {
      "Year": {
        "gte": 2000,
        "lte": 2010,
        "boost": 2.0
      }
    }
  }
}
