import csv
import editdistance

f = open("data/CUIs_oneLabel.csv", 'r',encoding="utf-8" )
reader = csv.reader(f,delimiter=',')
cuis=list(reader)
f.close()


f = open("data/CUIs.csv", 'r',encoding="utf-8" )
reader = csv.reader(f,delimiter=',')
cuis_lang=list(reader)
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
        for row in cuis_lang:
            if editdistance.eval(label, row[1])<=1:
                return row[0]
    return -1
    
def get_cui_label(id):
  if id in CUIs:
    return CUIs[id]  
  return -1  
