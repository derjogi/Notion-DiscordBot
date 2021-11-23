import requests
import json
import os
import conf

url = "https://api.notion.com/v1/databases/" + str(conf.DATABASE) + "/query"

def doesEntryExist(link):

  headers = {
    'Authorization': conf.NOTION_AUTH,
    'Notion-Version': '2021-05-13',
    'Content-Type': 'application/json'
  }
  response = requests.post(url, headers=headers)
  response.raise_for_status()   # just in case we have 404 or so
  result = response.json()["results"]
  if(len(result) == 0):
    return False
  return True

def amIThere(file):
    filesUploaded = []
    with open("./Bot/dataUploaded.txt") as log:
        filesUploaded = [line.strip() for line in log]
    print(filesUploaded)

    if file in filesUploaded:
        return True
    return False
