# Just have this file be used in the main script. It will contain the functions and stuff for calling and handling responses
import json
import requests
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, ConceptsOptions

summary = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam vitae semper nulla. Aenean laoreet vel erat a semper. Nam quis sem pulvinar, feugiat dui in, dignissim libero. Morbi sit amet viverra augue. In hac habitasse platea dictumst. Praesent hendrerit magna eu nisi dictum, eu imperdiet turpis sollicitudin. Nullam ullamcorper libero ac placerat posuere. Morbi hendrerit dui cursus enim faucibus, quis commodo lacus efficitur. Quisque et aliquam neque. Suspendisse in convallis dolor. Fusce rutrum, neque non maximus vulputate, magna felis efficitur augue, ut tincidunt odio libero at velit. Sed a odio facilisis, aliquam felis et, molestie dolor. Pellentesque iaculis vulputate porttitor."

smmryAPI = "441DD3B507"
authenticator = IAMAuthenticator('_nf9lfcQviYt2nyNlwF1LF_-2q86K8wzdecm-b-Gf_G9')
nlu = NaturalLanguageUnderstandingV1(version='2019-01-25', authenticator=authenticator)


def get_concepts(text):
    concepts = nlu.analyze(text=text, features=Features(concepts = ConceptsOptions(limit=3))).get_result()
    return concepts.json()

def parse_concepts(text):
    concepts = get_concepts(text)
    parsedInfo = []
    for concept, counter in concepts:
        parsedInfo[counter] = concept['text']
        counter = counter + 1
    return parsedInfo
    
"""
Max 1000 Chars
"""
def get_summary(text):
    url = 'https://api.smmry.com/
    data={'SM_API_KEY':smmryAPI, 'sm_api_input':text}
    
    summaryResponse = requests.post(url, data, timeout=20, allow_redirects=True)
    print(summaryResponse.json())

get_summary(summary)