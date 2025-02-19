# Just have this file be used in the main script. It will contain the functions and stuff for calling and handling responses
import json
import requests #pip install
from ibm_watson import NaturalLanguageUnderstandingV1 #pip install ibm_watson
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, ConceptsOptions

authenticator = IAMAuthenticator('_nf9lfcQviYt2nyNlwF1LF_-2q86K8wzdecm-b-Gf_G9')
nlu = NaturalLanguageUnderstandingV1(version='2019-01-25', authenticator=authenticator)

def get_concepts(text):
    concepts = nlu.analyze(text=text, features=Features(concepts = ConceptsOptions(limit=1))).get_result()
    return concepts['concepts']

def parse_concepts(text):
    concepts = get_concepts(text)
    parsedInfo = []
    for i in range(len(concepts)):
        parsedInfo.append(concepts[i]['text'])
    return parsedInfo
