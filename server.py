from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Instantiate Flask
app = Flask("Emotion Detector")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector", methods=['GET'])
def RunSentimentAnalysis():
    
    text_to_analyze = request.args.get("textToAnalyze") #Retrieve the input from the user

    response = emotion_detector(text_to_analyze)    # Run it through the detector function

    # Assign each score to an emotion variable so it is easier to format for the output.
    anger = response["anger"] 
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sad = response["sadness"] 
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion is None:
        return "<b>Invalid text! Please try again!</b>"
    
    # Set the output message with a cleaner formatting.
    output = (f"<p>For the given statetement, the system response is:</p><p>Anger: {anger}</p><p>Disgust: {disgust}</p><p>Fear: {fear}</p><p>Joy: {joy}</p><p>Sadness: {sad}</p><p>The dominant emotion is <b>{dominant_emotion.upper()}</b>.</p>")

    return output   

if __name__ == "__main__":
    app.run(debug=True)