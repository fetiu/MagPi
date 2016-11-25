import os,sys
from flask import Flask, make_response, render_template, request
#from flask.ext.images import resized_img_src
app =Flask(__name__, static_folder= 'images')


@app.route('/')
def home():
    resp = make_response(render_template('index.html'))
    return resp
@app.route('/controller')
def controller():
    return 'controller'

@app.route('/login')
def login():
    return 'login'

@app.route('/streamer')
def streamer():
    stream_resp = make_response(render_template('stream.html'))
    return stream_resp

def gpio_readall():
    os.system('gpio readall > /home/pi/my_python/log/gpio_readall.log')
    log = open('/home/pi/my_python/log/gpio_readall.log', 'r')
    output = log.readlines()
    log.close()
    return str(output)

@app.route('/hello')
def hello():
    return 'hello'

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
