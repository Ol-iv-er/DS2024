from flask import Flask, render_template, redirect, Response, url_for
import cv2



app: Flask = Flask(__name__)
camera: cv2 = cv2.VideoCapture(0)

def gen_detect_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            dectector = cv2.CascadeClassifier("Haarcascades/haarcascade_frontalface_default.xml")
            eye_cascade = cv2.CascadeClassifier("Haarcascades/haarcascade_eye.xml")
            faces = dectector.detectMultiScale(frame, 1.1,7)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Draw the rectange around the face
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)

                # Draw the rectangles around the eyes
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 2)

            _, buffer = cv2.imencode('.jpeg', frame)
            frame = buffer.tobytes()

            yield(b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def generate_frames(image_flipped = False):
    reading_frames = True
    while reading_frames:
        ## Read Camera frames
        frame_success, frames = camera.read()

        if not frame_success:
            return "Failed to read from camera."
        else:
            ret, buffer = cv2.imencode('.jpeg', frames)
            frames = buffer.tobytes()
            if image_flipped:
                frames = cv2.flip(buffer, 1).tobytes()


        yield(b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frames + b'\r\n')


@app.route('/')
def index() -> str:
    return render_template('index.html')

@app.route('/video')
def stream_video() -> Response:
    return Response(generate_frames(), mimetype = 'multipart/x-mixed-replace; boundry=frame')

# when the button is pressed we can just change page
@app.route('/video_flip')
def stream_video_flip() -> Response:
    return Response(generate_frames(image_flipped = True), mimetype = 'multipart/x-mixed-replace; boundry=frame')

@app.route('/submit', methods = ['POST', 'GET'])
def submit() -> Response:
    return redirect(url_for('stream_video_flip'))

@app.route('/video_dectection')
def stream_detected_video() -> Response:
    return Response(gen_detect_frames(), mimetype = 'multipart/x-mixed-replace; boundry=frame')

if __name__ == '__main__':
    app.run(debug=True)