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
                "sinhala-ngram": {
                    "type": "custom",
                    "tokenizer": "icu_tokenizer",
                    "char_filter": ["punctuation_char_remove_filter"],
                    "token_filter": [
                        "edge_n_gram_filter"
                    ]
                },
                "sinhala": {
                    "type": "custom",
                    "tokenizer": "icu_tokenizer",
                    "char_filter": ["punctuation_char_filter"]
                },
                "english": {
                    "type": "custom",
                    "tokenizer": "classic",
                    "char_filter": ["punctuation_char_filter"],
                },
                "sinhala-search": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "char_filter": ["punctuation_char_remove_filter"]
                },
            },
            "char_filter": {
                "punctuation_char_filter": {
                    "type": "mapping",
                    "mappings": [".=>", "|=>", "-=>", "_=>", "'=>", "/=>", ",=>"]
                },
                "punctuation_char_remove_filter": {
                    "type": "mapping",
                    "mappings": [".=>\\u0020", "|=>\\u0020", "-=>\\u0020", "_=>\\u0020", "'=>\\u0020", "/=>\\u0020", ",=>\\u0020"]
                }
            },
            "token_filter": {
                "edge_n_gram_filter": {
                    "type": "edge_ngram",
                    "min_gram": "2",
                    "max_gram": "6",
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
                "analyzer": "sinhala-ngram",
                "search_analyzer": "sinhala-search"
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
                "analyzer": "sinhala-ngram",
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
                        "analyzer": "sinhala-ngram",
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
                        "analyzer": "sinhala-ngram",
                        "search_analyzer": "sinhala-search"
                    },
                    "interpretation": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            },
                        },
                        "analyzer": "sinhala",
                        "search_analyzer": "sinhala-search"
                    }
                }
            },
            "view_count": {
                "type": "long"
            },
            "published_on": {
                "type": "text"
            },
            "length": {
                "type": "long"
            },
            "lyrics": {
                "type": "text",
                "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        },
                },
                "analyzer": "sinhala",
                "search_analyzer": "sinhala-search"
            }
        }
    }
}


configs = {
    "settings": {
        "index": {
            "number_of_shards": 1,
            "number_of_replicas": 1
        },
        "analysis": {
            "analyzer": {
                "sinhala-ngram": {
                    "type": "custom",
                    "tokenizer": "icu_tokenizer",
                    "char_filter": ["punc_char_filter"],
                    "token_filter": [
                        "edge_n_gram_filter"
                    ]
                },
                "sinhala": {
                    "type": "custom",
                    "tokenizer": "icu_tokenizer",
                    "char_filter": ["punc_char_filter"]
                },
                "english": {
                    "type": "custom",
                    "tokenizer": "classic",
                    "char_filter": ["punc_char_filter"],
                },
                "sinhala-search": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "char_filter": ["punc_char_filter"]
                },
            },
            "char_filter": {
                "punc_char_filter": {
                    "type": "mapping",
                    "mappings": [".=>", "|=>", "-=>", "_=>", "'=>", "/=>", ",=>", "?=>"]
                }
            },
            "token_filter": {
                "edge_n_gram_filter": {
                    "type": "edge_ngram",
                    "min_gram": "2",
                    "max_gram": "20",
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
            "title": {
                "type": "text",
                "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        },
                },
                "analyzer": "sinhala-ngram",
                "search_analyzer": "sinhala-search"
            },
            "artist": {
                "type": "text",
                "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        },
                },
                "analyzer": "sinhala-ngram",
                "search_analyzer": "sinhala-search"
            },
            "genre": {
                "type": "text",
                "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        },
                },
                "analyzer": "sinhala-ngram",
                "search_analyzer": "sinhala-search"
            },
            "lyrics": {
                "type": "text",
                "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        },
                },
                "analyzer": "sinhala-ngram",
                "search_analyzer": "sinhala-search"
            },
            "music": {
                "type": "text",
                "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        },
                },
                "analyzer": "sinhala-ngram",
                "search_analyzer": "sinhala-search"
            },
            "guitar_key": {
                "type": "text",
                "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        },
                },
            },
            "beat": {
                "type": "text",
                "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        },
                },
            },
            "song_lyrics": {
                "type": "text",
                "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        },
                },
                "analyzer": "sinhala",
                "search_analyzer": "sinhala-search"
            },
            "number_of_visits": {
                "type": "long"
            },
            "number_of_shares": {
                "type": "long"
            }
        }
    }
}
