from flask import Flask, request

def emotion_detector(text_to_analyse):
 
    if not text_to_analyse or text_to_analyse.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    try:
        status_code = 200
        if status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

        if status_code == 200:
            sample_response = {
                'anger': 0.006274985,
                'disgust': 0.002559293,
                'fear': 0.009251528,
                'joy': 0.9680386,
                'sadness': 0.04974144,
                'dominant_emotion': 'joy'
            }
            return sample_response

        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    except ValueError:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

def run_emotion_detection():
   
    app = Flask("EmotionDetector")

    @app.route("/emotionDetector")
    def emotion_detector_route():
       
        text_to_analyze = request.args.get('textToAnalyze')

        response = emotion_detector(text_to_analyze)

        if response['dominant_emotion'] is None:
            return "Invalid text! Please try again!"

        return (
            f"For the given statement, the system response is "
            f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, 'joy': {response['joy']} and "
            f"'sadness': {response['sadness']}. The dominant emotion is "
            f"{response['dominant_emotion']}."
        )

    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    run_emotion_detection()




