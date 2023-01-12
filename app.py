
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
        session["results"]=[]
    if not session.get("msg"):
        session["msg"]=["WELCOME"]

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
    get_sorting_type = processor.get_sorter(tokens)
    get_range = processor.get_range(tokens)
    query_text = processor.query_text(tokens)
    
    
    query={
        "multi_match":{
         "query":query_text,
         "fields":get_boosters,
         "operator":"or",
         "type":"best_fields",
         "fuzziness":"AUTO"
      }
    }


    if get_sorting_type!=None:
        sort=[
            get_sorting_type
        ]
        response = es_client.search(index=configs.INDEX,query=query,sort=sort,size=get_range)
    
    else:
        response = es_client.search(index=configs.INDEX,query=query,size=get_range)
    
    songs_num = len(response["hits"]["hits"])
    songs=[]
    for i in range(songs_num):
        songs.append(response["hits"]["hits"][i]["_source"])
    
    msg =[]
    msg.append("search term : "+str(search_term))
    msg.append("tokens : "+str(query_text))
    msg.append("sorting type : "+str(get_sorting_type))
    msg.append("max range : "+str(get_range))
    msg.append("boosters : "+str(get_boosters))
    msg.append("no of results : "+str(songs_num))


    session["results"]=songs
    session["msg"]=msg
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
    all=str(typed).split()
    last=all.pop()
    all_str=""
    for i in all:
        all_str+=i+" "

    query= {
            "interpretation": {
                "prefix": last,
                "completion": {
                    "field": "metaphors.interpretation"
                }
            },
            "lyrics": {
                "prefix": last,
                "completion": {
                    "field": "lyrics"
                }
            }
        }
    
    response = es_client.search(index=configs.INDEX,suggest=query)

    suggestions=set()

    for val in response['suggest']["interpretation"][0]['options']:        
        text = ""
        for chr in str(val['text']):
            if chr not in "[!@#$%^&*()[];:,./<>?\|`~-=_+]":
                text+=chr
        words = text.strip().split()
        for word in words:
            if last in word:
                suggestions.add(all_str+word)

    for val in response['suggest']["lyrics"][0]['options']:
        text = ""
        for chr in str(val['text']):
            if chr not in "[!@#$%^&*()[];:,./<>?\|`~-=_+]":
                text+=chr
        words = text.strip().split()
        for word in words:
            if last in word:
                suggestions.add(all_str+word)

    return list(suggestions)

if __name__ == '__main__':
    app.run(debug=True)