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
        return -1


def getCui(text):
    url = 'https://labs.tib.eu/sdm/umlsmatching/umlsmatching?type=cui'
    payload = '{"data":"'+text+'"}'
    r = requests.post(url, data=payload.encode('utf-8'), headers=headers)
    if r.status_code == 200:
        response=r.json()
        return response['cui']
    else:
        return -1


