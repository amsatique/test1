from elasticsearch import Elasticsearch
import time
import os

# elk = 'https://elastic:5gCM65s1VT3PNasGq3f91G08@localhost:9201'
elk = os.environ.get('ES_CONF')
print(elk)
try: 
    elk
except NameError:
    exit

def loop(es_url):
    es = Elasticsearch([es_url], verify_certs=False, timeout=60, ssl_show_warn=False)

    res = es.search(index="employee", query={'match_all' : {}})

    for hit in res['hits']['hits']:
        print("%(first_name)s %(last_name)s: %(about)s" % hit["_source"])
    time.sleep(60)
    
def main():
    print("Hello World!")
    loop(elk)

if __name__ == "__main__":
    main()
