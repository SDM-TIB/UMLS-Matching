# -*- coding: utf-8 -*-

import requests
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

def getLabel(text):
    url = 'https://labs.tib.eu/sdm/umlsmatching/umlsmatching?type=label'
    payload = '{"data":"'+text+'"}'
    r = requests.post(url, data=payload.encode('utf-8'), headers=headers)
    if r.status_code == 200:
        response=r.json()
        return response['label']
    else:
        return ""



def getCui(text, mode='short'):
    if mode=='short':
        url = 'https://labs.tib.eu/sdm/umlsmatching/umlsmatching?type=cui'
        payload = '{"data":"'+text+'"}'
        r = requests.post(url, data=payload.encode('utf-8'), headers=headers)
        if r.status_code == 200:
            response=r.json()
            return response['cui']
        else:
            return ""
    elif mode=='long':
        url = 'http://node3.research.tib.eu:5005/api_umls?mode=long&type=cui'
        payload = '{"data":"'+text+'"}'
        r = requests.post(url, data=payload.encode('utf-8'), headers=headers)
        if r.status_code == 200:
            response=r.json()
            return response['entities']
        else:
            return ""

