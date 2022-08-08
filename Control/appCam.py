# connect camera->Raspberry Pi Configuration Tool ->Camera Interface ->enabled->reboot
# install Flask on Rpi : sudo apt-get install python3-flask

from flask import Flask, render_template, request,Response
from camera_pi import Camera
import os
from time import sleep
obj = Camera()

app = Flask(__name__)

global direct
direct = "stop"
@app.route('/')
def index():
    """" video streaming home page """
    templateData = {
        'direct' : direct,
    }
    return render_template("index.html",**templateData)


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


@app.route("/<direction>")
def move(direction):
    global direct
    direct = direction
    os.system("python3 control.py "+str(direct))
    templateData = {
        'direct': direct,
    }
    return render_template('index.html', **templateData)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
