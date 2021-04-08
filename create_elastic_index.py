# -*- coding: utf-8 -*-

import csv
import json

f = open("data/CUIs.csv", 'r',encoding="utf-8" )
reader = csv.reader(f,delimiter=',')
cuis_lang=list(reader)
f.close()


rows=[]
for row in cuis_lang:
    index=dict()
    index["_source"]={'cui': row[0] , 'label': row[1] , 'lang': row[2]}
    rows.append(index)
    
    
with open("data/umlsDump.json", "w", encoding="utf-8") as output:
    for row in rows:
        output.write(json.dumps(row))
        output.write('\n')

    


