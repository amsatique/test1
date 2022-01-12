from elasticsearch import Elasticsearch
import time


def loop():
    es = Elasticsearch(['https://elastic:5gCM65s1VT3PNasGq3f91G08@localhost:9201'], verify_certs=False, timeout=60, ssl_show_warn=False)

    res = es.search(index="employee", query={'match_all' : {}})

    for hit in res['hits']['hits']:
        print("%(first_name)s %(last_name)s: %(about)s" % hit["_source"])
    time.sleep(3)
    
def main():
    print("Hello World!")
    loop()

if __name__ == "__main__":
    main()
