import requests

def emotion_detector(text_to_analyze):
""" Function that takes some text as input and runs returns
the emotional footprint of the text, as well as how strong that footprint is."""

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    text_obj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=text_obj, headers=header)

    return response.text