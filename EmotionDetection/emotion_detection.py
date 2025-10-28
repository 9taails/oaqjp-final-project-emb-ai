import requests, json

# Function that takes some text as input and runs returns
# the emotional footprint of the text, as well as how strong that footprint is.
def emotion_detector(text_to_analyze):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    text_obj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=text_obj, headers=header)
    json_dict = json.loads(response.text)

    # Add error handling
    if response.status_code == 200:

        emotions = json_dict["emotionPredictions"][0]["emotion"]

        #Find the dominant emotion using bubble sort

        max_value = emotions["anger"]   # Setting the comparison base to first emotion on the list
        max_emotion = "anger"           # Setting the default emotion name to anger
        
        for emotion in emotions:
            score = emotions[emotion]
            if score > max_value:
                max_value = score
                max_emotion = emotion

        anger = emotions["anger"]
        disgust = emotions["disgust"]
        fear = emotions["fear"]
        joy = emotions["joy"]
        sadness = emotions["sadness"]
        dominant_emotion = max_emotion

    elif response.status_code == 400:

        # Set all emotion scores to None when there is no text input from the user

        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None

    # Create a filtered dictionary with emotions and their scores only
    output = {  
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
        }
    
    return output

