import requests

def emotion_detector(text_to_analyze):
    if not text_to_analyze:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        data = response.json()['text']
        
        emotions = {
            'anger': data['emotion']['document']['emotion']['anger'],
            'disgust': data['emotion']['document']['emotion']['disgust'],
            'fear': data['emotion']['document']['emotion']['fear'],
            'joy': data['emotion']['document']['emotion']['joy'],
            'sadness': data['emotion']['document']['emotion']['sadness']
        }
        
        dominant_emotion = max(emotions, key=emotions.get)
        
        emotions['dominant_emotion'] = dominant_emotion
        
        return emotions
    else:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
