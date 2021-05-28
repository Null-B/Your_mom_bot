from flask import Flask 
from threading import Thread
from flask import request
from flask import jsonify

app = Flask('') 

@app.route('/') 
def home():
    return "Hello. I am alive!"


def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200


print(get_my_ip())
def run():
    app.run(host='0.0.0.0',port=8080) 



def keep_aliveO():
    t = Thread(target=run)
    t.start()