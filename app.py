
import os
import configs
import re
from flask import Flask , render_template, send_from_directory,request,redirect,url_for,session
from flask_session import Session
from elasticsearch7 import Elasticsearch
from Processor import Processor


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
es_client = Elasticsearch(HOST=configs.HOST, PORT=configs.PORT)
Session(app)
 

@app.route('/')
def home():

    if not session.get("results"):
        session["results"]={}
    if not session.get("msg"):
        session["msg"]=""

    results=session["results"]
    msg=session["msg"]
    return render_template('home.html',results=results,msg=msg)

@app.route('/submit',methods=['POST'])
def submit():
    search_term =  request.form['form-search']
    processor = Processor()

    search_term = processor.strip(search_term)
    search_term = processor.special_char_remove(search_term)
    tokens = processor.tokenize(search_term)
    tokens = processor.stop_word_remove(tokens)
    get_boosters=processor.get_boosters(tokens)
    

    
    
    
    query={
        "nested": {
            "path":"metaphors",
            "query": {
                "bool": {
                    "must": [
                        { "match": { "metaphors.targets": "ඇස" } }
                    ]
                }
            }
        }
    }
    response = es_client.search(index=configs.INDEX,query=query)
    songs_num = response["hits"]["total"]["value"]
    songs=[]
    for i in range(songs_num):
        songs.append(response["hits"]["hits"][i]["_source"])
    
    metas={}
    for song in songs:
        for meta in song["metaphors"]:
            if search_term in meta["targets"]:
                source=meta["source"]
                if source not in metas.keys():
                    metas[source]=[]
                metas[source].append({
                    "id":song["id"],
                    "name":song["name"],
                    "youtube_link":song["youtube_link"],
                    "singers":song["singers"],
                    "source":meta["source"],
                    "interpretation":meta["interpretation"],
                    "possible_targets":meta["targets"],
                    "view_count":song["view_count"],
                    "published_on":song["published_on"],
                    "length":song["length"],
                    "lyrics":song["lyrics"]             
                })


    session["results"]=metas
    session["msg"]=tokens#"උපමා "+str(len(metas))+" ක් සොයාගන්නා ලදි"
    return redirect(url_for('home'))
        


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'templates'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route('/styles.css')
def styles():
    return send_from_directory(os.path.join(app.root_path, 'templates'),
                          'styles.css',mimetype='text/css')


@app.get('/suggestions/<typed>')
def suggestions(typed):
    query= {
            "source": {
                "prefix": typed,
                "completion": {
                    "field": "metaphors.interpretation"
                }
            },
            "lyrics": {
                "prefix": typed,
                "completion": {
                    "field": "lyrics"
                }
            }
        }
    
    response = es_client.search(index=configs.INDEX,suggest=query)

    suggestions=set()

    for val in response['suggest']["source"][0]['options']:        
        text = ""
        for chr in str(val['text']):
            if chr not in "[!@#$%^&*()[];:,./<>?\|`~-=_+]":
                text+=chr
        words = text.strip().split()
        for word in words:
            if typed in word:
                suggestions.add(word)

    for val in response['suggest']["lyrics"][0]['options']:
        text = ""
        for chr in str(val['text']):
            if chr not in "[!@#$%^&*()[];:,./<>?\|`~-=_+]":
                text+=chr
        words = text.strip().split()
        for word in words:
            if typed in word:
                suggestions.add(word)

    return list(suggestions)

if __name__ == '__main__':
    app.run(debug=True)