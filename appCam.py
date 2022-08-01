# connect camera->Raspberry Pi Configuration Tool ->Camera Interface ->enabled->reboot
# install Flask on Rpi : sudo apt-get install python3-flask

from flask import Flask, render_template, Response
from camera_pi import Camera
obj = Camera()


app = Flask(__name__)


@app.route('/')
def index():
    """" video streaming home page """
    return render_template("index.html")


def gen(camera):
    """" video streaming generator function """
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(obj),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
