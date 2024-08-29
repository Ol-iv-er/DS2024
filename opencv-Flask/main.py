from flask import Flask, render_template, redirect, Response, url_for
import cv2



app: Flask = Flask(__name__)
camera: cv2 = cv2.VideoCapture(0)

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
def index():
    return render_template('index.html')

@app.route('/video')
def stream_video():
    return Response(generate_frames(), mimetype = 'multipart/x-mixed-replace; boundry=frame')

# when the button is pressed we can just change page
@app.route('/video_flip')
def stream_video_flip():
    return Response(generate_frames(image_flipped = True), mimetype = 'multipart/x-mixed-replace; boundry=frame')

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    return redirect(url_for('stream_video_flip'))

if __name__ == '__main__':
    app.run(debug=True)