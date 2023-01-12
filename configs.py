HOST = "http://localhost"
PORT = 9200
INDEX = 'sinmeta'
PARAMS = {
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
    },
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
}


