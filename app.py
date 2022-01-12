from elasticsearch import Elasticsearch
import time
import os

elk = os.environ.get('ES_CONF')

try: 
    elk
except NameError:
    exit

def loop(es_url):
    es = Elasticsearch([es_url], verify_certs=False, timeout=5, ssl_show_warn=False)

    res = es.search(index="employee", query={'match_all' : {}})

    for hit in res['hits']['hits']:
        print("%(first_name)s %(last_name)s: %(about)s" % hit["_source"])
    time.sleep(60)
    print("Waiting for next loop")
        
def main():
    print("Hello World!")
    while True:
        loop(elk)

if __name__ == "__main__":
    main()
