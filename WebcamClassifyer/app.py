from flask import Flask,request, render_template, Response
import cv2
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load pre-trained CNN model
model_path = 'model_natanael_recognition_TL.h5'
try:
    model = tf.keras.models.load_model(model_path)
    model.summary()
except Exception as e:
    print(f"Error loading model: {e}")

# Function to process the frame and classify the face
def process_frame(frame):
    img = cv2.resize(frame, (220, 220))
    img = img / 255.0
    img = np.expand_dims(img, axis=3)
    predictions = model.predict(img)
    return predictions

# Function to capture frames from the webcam and classify in real-time
def gen_frames():
    print("Starting video capture")
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Error: Could not access the webcam.")
        return
    while True:
        success, frame = camera.read()
        if not success:
            print("Failed to read frame")
            break
        else:
            predictions = process_frame(frame)
            
            text = f'Prediction: {"Natanael" if np.argmax(predictions) >= 0.5 else "outros"}'
            cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    camera.release()
    print("Released video capture")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/model')
def model_page():
    return render_template('model.html')

@app.route('/webcam')
def webcam():
    return render_template('webcam.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
