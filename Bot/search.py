import os
import json
import requests

from Bot import conf


class SearchObject:
    # Class for Search Results
    title = ""
    url = ""
    id=""

    def __init__(self, url, title, id):
        self.url = url
        self.title = title
        self.id = id


def searchTag(args):
    # Search for a tag
    url = "https://api.notion.com/v1/databases/" + \
        conf.DATABASE + "/query"
    payload = json.dumps({
        "filter": {
            "and": args
        }
    })
    headers = {
        'Authorization': conf.NOTION_AUTH,
        'Notion-Version': '2021-05-13',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)

    query_results = response.json()["results"]
    no_of_results = len(query_results)

    search_results = []
    if no_of_results == 0:
        # No results found
        return(search_results)
    for result in query_results:
        # Create Search Object for each result
        search_object = SearchObject(
            result["properties"]["URL"]["url"], result["properties"]["Title"]["rich_text"][0]["plain_text"], result["id"])
        search_results.append(search_object)
    return(search_results)