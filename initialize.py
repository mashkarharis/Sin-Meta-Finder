from elasticsearch7 import Elasticsearch, helpers
import json
import configs
import os

def load_songs():
    song_dir=os.path.join(os.getcwd(), "songs")
    for filename in os.listdir(song_dir):
        with open(os.path.join(song_dir, filename), 'r') as f:
            data = json.load(f)
            yield{
                "_index": configs.INDEX,
                "_source":data
            }

if __name__=="__main__":

    print("\nInitializing . . .")
    
    es_client = Elasticsearch(HOST=configs.HOST, PORT=configs.PORT)
    print("\nConnecting . . .")
    print(es_client.info())

    exists = es_client.indices.exists(index=configs.INDEX)
    print("\nIndex Already Exists :",exists)

    if exists:
        result = es_client.indices.delete(index=configs.INDEX)
        print("\nExisting Index Deleting, Result")
        print(result)

    result = es_client.indices.create(index=configs.INDEX,body=configs.PARAMS)
    print("\nNew Index Creating, Result")
    print(result)

    # result = es_client.indices.put_settings(index=configs.INDEX,body=configs.PARAMS.get("settings"))
    # print("\nConfiguring Settings, Result")
    # print(result)

    # result = es_client.indices.put_mapping(index=configs.INDEX,body=configs.PARAMS.get("mappings"))
    # print("\nConfiguring Mapping, Result")
    # print(result)

    print("Adding Data . . .")
    result = helpers.bulk(es_client,load_songs())
    print("Data Added, Result")
    print(result)


