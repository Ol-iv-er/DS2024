#from flask import Flask, render_template, Response
import cv2



app: Flask = Flask(__name__)
camera: cv2 = cv2.VideoCapture(0)

def generate_frames():
    reading_frames = True
    while reading_frames:
        ## Read Camera frames
        frame_success, frames = camera.read()
        if not frame_success:
            break
        else:
            ret, buffer = cv2.imencode('.jpeg', frames)
            frames = buffer.tobytes()

        yield(b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frames + b'\r\n')


@app.route('/')
def index():
    return render_template('camera_index.html')

@app.route('/video')
def stream_video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundry=frame')

if __name__ == '__main__':
    app.run(debug=True)