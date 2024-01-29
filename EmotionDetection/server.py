from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotionDetector():
    """
    Endpoint to detect emotions from text input.
    
    Returns:
        JSON: Emotion detection result.
    """
    data = request.json
    text = data.get('text', '')
    result = emotion_detector(text)
    
    if result['dominant_emotion'] is None:
        return jsonify({"message": "Invalid text! Please try again."}), 400
    
    response = {
        "anger": result['anger'],
        "disgust": result['disgust'],
        "fear": result['fear'],
        "joy": result['joy'],
        "sadness": result['sadness'],
        "dominant_emotion": result['dominant_emotion']
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)