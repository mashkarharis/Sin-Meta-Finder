# Sin-Meta-Finder
Metaphor Source Recommendation System For Sinhala Songs / Poetry

## Language 
- Sinhala Language
## Scope
- Best Sinhala Hit Songs (2000 - 2015)
## Audience
- Writers who write songs/poetry in the Sinhala language
## Technologies
- Python
- Flask
- Elastic Search / Kibana
- HTML/JS/CSS/JQuery
## How To Run
1. Download and Install Elastic Search [link](https://www.elastic.co/downloads/elasticsearch)
2. Download and Install Kibana [link](https://www.elastic.co/downloads/kibana)
3. Install Plugin icu_analysis by running *bin\elasticsearch-plugin install analysis-icu*
4. Run *bin\elasticsearch.bat* to start Elastic Search
5. Run *bin\kibana.bat* to start Kibana
6. Make sure kibana running on [ http://localhost:5601](http://localhost:5601) 
7. Download this project
8. In project root folder create virtual environment by
    1. Run *python -m pip install virtualenv*
    2. Run *python -m venv env*
    3. Activate environment by running *env\Scripts\activate*
    4. Install requirements by running *python -m pip install -r requirements.txt*
    5. Verify installation by *python -m pip list*
9. Run *python initialize.py* to initialization
10. Run *python app.py* to start flask server
11. Now system is running
## How To Use
1. Go to [http://127.0.0.1:5000](http://127.0.0.1:5000), which is the home page of app
2. Then type queries which will return results
3. You can click link cell and metaphor cell for further exploration.
4. Moreover query processing result for each search will be shown in a blue texted box

## Screenshot
![screenshot](https://github.com/mashkarharis/Sin-Meta-Finder/blob/main/extra/ss.PNG)
## Query Processing Result
This will be shown in blue texted box as shown below,\
![configs](https://github.com/mashkarharis/Sin-Meta-Finder/blob/main/extra/query_processing_result.PNG)

## Suggestions While Typing
![suggestions](https://github.com/mashkarharis/Sin-Meta-Finder/blob/main/extra/search.png)
## What Can You Search
#### Boost by Song Name
Ex:-  රන් කුරහන් මල ගීතය
#### Boost by Singer
Ex:-  රුක්මන් ගැයූ ගීත
#### Boost by Source (උපමේය)
Ex:- සුරඟන සදහා උපමේය
#### Boost By Target (උපමා)
Ex:- අම්මා සදහා උපමා

## Sorting
#### Default Sorting
None\
අම්මා සදහා උපමා
#### If Query Contains Words Like "නවතම", "අලුත්", "නව", "අලුත්ම"
Sort By Publish Date Descending\
Ex:- අම්මා සදහා නවතම උපමා
#### If Query Contains Words Like 'ජනප්‍රිය', 'ප්‍රචලිත', 'ප්‍රසිද්ධ', 'ජනප්‍රියම', 'ප්‍රචලිතම' 'ප්‍රචලිතම'
Sort By Popularity Descending\
Ex:- අම්මා සදහා ප්‍රසිද්ධ උපමා
## Limiting Factors
#### Default Limiting Factor
Ex:- ඉරාජ් ගැයු ගීත
10 Songs Will Be Shown
#### If Query Contains Some Number That Will Be The Limiting Factor
Ex:- ඉරාජ් ගැයු ගීත 3 ක්
3 Songs Will Be Shown

## Stop Words
#### Stop Words Are Taken From,
Link : [https://github.com/nlpcuom/Sinhala-Stopword-list](https://github.com/nlpcuom/Sinhala-Stopword-list)

## Corpus
Contains 110 Songs. Can be found at,

    songs/
        song-1.json
        song-2.json
        ...
        song-110.json
## Corpus Storing Settings (ES)
```
"settings": {
        "index": {
            "number_of_shards": 1,
            "number_of_replicas": 1
        },
        "analysis": {
            "analyzer": {
                "sinhala-tokens-ngram": { # Indexing Time
                    "type": "custom",
                    "tokenizer": "icu_tokenizer", # Divide Into Words, ICU_TOKENIZER Best With Asian Languages
                    "char_filter": ["punctuation_char_replace_filter"], # For Short Texts We Replace Special Characters
                    "token_filter": [
                        "edge_n_gram_filter" # Create N-Grams For Each Divided Words
                    ]
                },
                "sinhala-tokens-words": { # Indexing TIme
                    "type": "custom",
                    "tokenizer": "icu_tokenizer", # Divide Into Words, ICU_TOKENIZER Best With Asian Languages
                    "char_filter": ["punctuation_char_remove_filter"]  # For Long Texts We Remove Special Characters
                    # Don't Do N-Gram Because We Apply This For Long Sentences Like Lyrics. N-Gram Will Be An Overhead
                },
                "sinhala-search": { # Searching Time
                    "type": "custom",
                    "tokenizer": "standard", # Divide Into Words, ICU_TOKENIZER Best With Asian Languages
                    "char_filter": ["punctuation_char_replace_filter"],  # For Short Texts We Replace Special Characters
                },
            },
            "char_filter": {
                "punctuation_char_remove_filter": {
                    "type": "mapping",
                    "mappings": [".=>", "|=>", "-=>", "_=>", "'=>", "/=>", ",=>"]
                },
                "punctuation_char_replace_filter": {
                    "type": "mapping",
                    "mappings": [".=>\\u0020", "|=>\\u0020", "-=>\\u0020", "_=>\\u0020", "'=>\\u0020", "/=>\\u0020", ",=>\\u0020"]
                }
            },
            "token_filter": {
                "edge_n_gram_filter": {
                    "type": "edge_ngram",
                    "min_gram": "2",
                    "max_gram": "10",
                    "side": "front"
                }
            }
        }
}
```
## Corpus Mapping
```
"mappings": {
        "properties": {
            "id": {
                "type": "long"
            },
            "name": {
                "type": "text",
                "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        },
                },
                "analyzer": "sinhala-tokens-ngram",
                "search_analyzer": "sinhala-search",
            },
            "youtube_link": {
                "type": "text"
            },
            "singers": {
                "type": "text",
                "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        },
                },
                "analyzer": "sinhala-tokens-ngram",
                "search_analyzer": "sinhala-search"
            },
            "metaphors": {
                "type": "nested",
                "properties": {
                    "meta_id": {
                        "type": "long"
                    },
                    "targets": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            },
                        },
                        "analyzer": "sinhala-tokens-ngram",
                        "search_analyzer": "sinhala-search"
                    },
                    "source": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            },
                        },
                        "analyzer": "sinhala-tokens-ngram",
                        "search_analyzer": "sinhala-search"
                    },
                    "interpretation": {
                        "type": "completion",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            },
                        },
                        "analyzer": "sinhala-tokens-words",
                        "search_analyzer": "sinhala-search"
                    }
                }
            },
            "view_count": {
                "type": "long"
            },
            "published_on": {
                "type": "date"
            },
            "length": {
                "type": "long"
            },
            "lyrics": {
                "type": "completion",
                "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        },
                },
                "analyzer": "sinhala-tokens-words",
                "search_analyzer": "sinhala-search"
            }
        }
}
```
## Query Processing Steps
![steps_of_query_processing](https://github.com/mashkarharis/Sin-Meta-Finder/blob/main/extra/query_processing_steps.jpg)

