from flask import render_template
from app import app
from elasticsearch import Elasticsearch, helpers
import json
from datetime import datetime
from time import sleep

@app.route('/')
@app.route('/index')
def index():
    #INSERT SHOULD BE DONE, LETS CHECK
    # get all of docs for the index
    client = Elasticsearch("localhost:9200")
    query_all = {
    'size' : 5,
    'query': {
    'match_all' : {}
    }
    }
    print ("\nSleeping for a few seconds to wait for indexing request to finish.")
    sleep(1)
    # pass the query_all dict to search() method
    resp = client.search(
    index = "elitemarket",
    body = query_all
    )

    print(type(resp))
    temp = json.dumps(resp)
    user = json.loads(temp)
    print(user['hits']['hits'][0]["_source"])
    return render_template('index.html', title='Home', user=user)