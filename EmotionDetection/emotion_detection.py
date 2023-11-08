''' Module for Emotion Detection package: emotion_detection.py
'''
'''
import json
import requests
import ibm_watson # import watson_nlp

def emotion_detector(text_to_analyse):
    # Function to run emotion detection of user text input 
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)

    # syntax_model = watson_nlp.load('syntax_izumo_en_stock')
    # syntax_prediction = syntax_model.run(text_to_analyse)
    
    if response.status_code == 200:
        emotion_predictor = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_predictor.items(), key=lambda x: x[1])[0]
        return {
            'anger': emotion_predictor['anger'],
            'disgust': emotion_predictor['disgust'],
            'fear': emotion_predictor['fear'],
            'joy': emotion_predictor['joy'],
            'sadness': emotion_predictor['sadness'],
            'dominant_emotion': dominant_emotion
        }
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        return None

    # return syntax_prediction
'''

import os
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve service credentials from environment variables
api_key = os.getenv("IBM_WATSON_API_KEY")
service_url = os.getenv("IBM_WATSON_SERVICE_URL")

# Initialize the IBM Watson Natural Language Understanding service
authenticator = IAMAuthenticator(api_key)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version="2021-08-01",
    authenticator=authenticator
)
natural_language_understanding.set_service_url(service_url)

def emotion_detector(text_to_analyze):
    try:
        response = natural_language_understanding.analyze(
            text=text_to_analyze,
            features={"emotion": {}}
        ).get_result()

        if response is not None:
            emotions = response.get("emotion", {}).get("document", {}).get("emotion", {})
            dominant_emotion = max(emotions, key=emotions.get)

            return {
                "anger": emotions.get("anger"),
                "disgust": emotions.get("disgust"),
                "fear": emotions.get("fear"),
                "joy": emotions.get("joy"),
                "sadness": emotions.get("sadness"),
                "dominant_emotion": dominant_emotion
            }
        else:
            return None

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Example usage
text_to_analyze = "I am feeling very happy today!"
result = emotion_detector(text_to_analyze)
print(result)
