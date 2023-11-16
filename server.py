'''Emotion Detector Application

Executing this function initiates the application of emotion detection to be
executed over the Flask channel and deployed on localhost:5000.
This file is server.py.
'''

# Import flask, render_template, request from the flask framework package.
from flask import Flask, render_template, request

# Import the emotion_detector function from the package created earlier.
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app.
app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def emot_detector():
    '''Run emotion detection on the provided text.

    This function receives the text from the HTML interface and runs emotion detection
    using the emotion_detector() function. The output returned shows the emotions,
    their associated scores, and the dominant emotion for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    # Check if the input is blank or contains only whitespace.
    if not text_to_analyze or text_to_analyze.strip() == "":
        return 'Invalid text! Please try again!'

    response = emotion_detector(text_to_analyze)

    # Check if the response is None
    if response is None:
        return 'Error processing text. Please try again.'

    # Extract attributes only if response is not None
    anger = response.get('anger')
    disgust = response.get('disgust')
    fear = response.get('fear')
    joy = response.get('joy')
    sadness = response.get('sadness')
    dominant_emotion = response.get('dominant_emotion')

    if dominant_emotion is None:
        return 'Invalid text! Please try again!'

    return f"For the given statement, the system response is 'anger': {anger},\
    'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}.\
    The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    '''Render the main application page.

    This function initiates the rendering of the main application page over the flask channel.
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
