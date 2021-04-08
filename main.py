import csv
from elasticsearch import Elasticsearch


es = Elasticsearch(['http://node3.research.tib.eu:9200'])
indexName="umls"

def search_elastic(term,k=1):
    results=[]
    elasticResults=es.search(index=indexName, body={
              "query": {
                "fuzzy" : { "label" : term } 
              }
               ,"size":5
    }
           )
    for result in elasticResults['hits']['hits'][:k]:
        results.append([result["_source"]["label"],result["_source"]["cui"],result["_score"]])
    return results



f = open("data/CUIs_oneLabel.csv", 'r',encoding="utf-8" )
reader = csv.reader(f,delimiter=',')
cuis=list(reader)
f.close()

    
CUIs=dict()
CUIsLabel=dict()
for cui in cuis:
    CUIs[cui[0]]=cui[1]
    CUIsLabel[cui[1]]=cui[0]
    
    
def get_cui_id(label):
    label=label.lower().strip().replace('_',' ')
    if label in CUIsLabel:
        return CUIsLabel[label]
    else:
        elastic_results=search_elastic(label)
        if len(elastic_results)!=0:
            return elastic_results[0][1]
        else:
            return -1
    return -1
    
def get_cui_label(id):
  if id in CUIs:
    return CUIs[id]  
  return -1  

