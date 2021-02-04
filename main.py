import csv

f = open("data/CUIs_oneLabel.csv", 'r',encoding="utf-8" )
reader = csv.reader(f,delimiter=',')
cuis=list(reader)
f.close()

    
CUIs=dict()
CUIsLabel=dict()
for cui in cuis:
    CUIs[cui[1]]=cui[0]
    CUIsLabel[cui[0]]=cui[1]
    
    
def get_cui_id(label):
  if label in CUIsLabel
    return CUIsLabel[label]
    
def get_cui_label(id):
  if label in CUIs
    return CUIs[id]    
