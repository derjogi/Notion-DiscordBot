import requests
import json
from Bot import conf
from getTitle import giveTitle
import os
url = "https://api.notion.com/v1/pages"
database = conf.DATABASE

def createDatabaseScheme():
    # connect to notion, get the headers and types for this database.
    # Then check whether the given fields match somewhat into that scheme.
    pass



def addData(url, contributor, tag=[{"name": "misc", "color": "default"}]):
    data_to_be_written = {
        "parent": {
            "database_id": database
        },
        "properties": {
            "Tag": {
                "multi_select": tag
            },
            "Title": {
                "rich_text": [
                    {
                        "text": {
                            "content": giveTitle(url),
                        },
                        "annotations": {
                            "bold": True,
                            "italic": False,
                            "strikethrough": False,
                            "underline": False,
                            "code": False,
                            "color": "yellow"
                        }
                    },

                ]
            },
            "URL": {
                "url": url
            },
            "Contributor": {
                "title": [
                    {
                        "text": {
                            "content": contributor,
                        },
                    }
                ]
            }
        }
    }

    # Posting the dictionary on the database
    payload = json.dumps(data_to_be_written)
    sendData(payload)

def addPDF(url, contributor, title, tag=[{"name": "misc", "color": "default"}, {"name": "pdf", "color": "default"}]):
    data_to_be_written = {
        "parent": {
            "database_id": database
        },
        "properties": {
            "Tag": {
                "multi_select": tag
            },
            "Title": {
                "rich_text": [
                    {
                        "text": {
                            "content": title,
                        },
                        "annotations": {
                            "bold": True,
                            "italic": False,
                            "strikethrough": False,
                            "underline": False,
                            "code": False,
                            "color": "yellow"
                        }
                    },

                ]
            },
            "URL": {
                "url": url
            },
            "Contributor": {
                "title": [
                    {
                        "text": {
                            "content": contributor,
                        },
                    }
                ]
            }
        }
    }

    # Posting the dictionary on the database
    payload = json.dumps(data_to_be_written)
    sendData(payload)

def addGenericFile(url, contributor, title, tag=[{"name": "misc", "color": "default"}]):
    data_to_be_written = {
        "parent": {
            "database_id": database
        },
        "properties": {
            "Tag": {
                "multi_select": tag
            },
            "Title": {
                "rich_text": [
                    {
                        "text": {
                            "content": title,
                        },
                        "annotations": {
                            "bold": True,
                            "italic": False,
                            "strikethrough": False,
                            "underline": False,
                            "code": False,
                            "color": "yellow"
                        }
                    },

                ]
            },
            "URL": {
                "url": url
            },
            "Contributor": {
                "title": [
                    {
                        "text": {
                            "content": contributor,
                        },
                    }
                ]
            }
        }
    }

    # Posting the dictionary on the database
    payload = json.dumps(data_to_be_written)
    sendData(payload)

def sendData(payload):
    headers = {
        'Authorization': conf.NOTION_AUTH,
        'Notion-Version': '2021-05-13',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.status_code)
