# -*- coding=utf-8 -*-
"""
주요 기능: 
    - 매매 신호 수신
    - 매매 결과 송신
    - 사용자 인증

사용례: 
    - 
"""

##@@@ 모듈 import
##============================================================

##@@ Built-In 모듈
##------------------------------------------------------------
import os, sys
import requests
import time
import json
import zlib
import base64
import string

##@@ Package 모듈
##------------------------------------------------------------
# from flask import Flask
from flask import Flask, render_template, request

##@@ User 모듈
##------------------------------------------------------------
# sys.path.append(os.path.join(os.path.dirname(__file__), '../../Assistant/Message'))
# from Slack import Slack

##@@@ 전역 상수/변수
##============================================================

##@@ Section
##------------------------------------------------------------



##@@@ 보조 함수
##============================================================

##@@ Section
##------------------------------------------------------------



##@@@ 실행 함수
##============================================================

##@@ Section
##------------------------------------------------------------
app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello World!"


@app.route('/hi/<name>')
def hi(name):
    return f"Hi! {name}"


@app.route('/handle_post', methods=['POST'])
def handle_post():
    params = json.loads(request.get_data(), encoding='utf-8')
    if len(params) == 0:
        return 'No parameter'

    params_str = ''
    for key in params.keys():
        params_str += 'key: {}, value: {}<br>'.format(key, params[key])
    return params_str


@app.route('/send_post', methods=['GET'])
def send_post():
    params = {
        "param1": "test1",
        "param2": 123,
        "param3": "한글"
    }
    res = requests.post("http://127.0.0.1:6868/handle_post", data=json.dumps(params))
    return res.text


plantuml_alphabet = string.digits + string.ascii_uppercase + string.ascii_lowercase + '-_'
base64_alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
b64_to_plantuml = bytes.maketrans(base64_alphabet.encode('utf-8'), plantuml_alphabet.encode('utf-8'))
plantuml_to_b64 = bytes.maketrans(plantuml_alphabet.encode('utf-8'), base64_alphabet.encode('utf-8'))


def plantuml_encode(plantuml_text):
    """zlib compress the plantuml text and encode it for the plantuml server"""
    zlibbed_str = zlib.compress(plantuml_text.encode('utf-8'))
    compressed_string = zlibbed_str[2:-4]
    return base64.b64encode(compressed_string).translate(b64_to_plantuml).decode('utf-8')

# def plantuml_decode(plantuml_url):
#     """decode plantuml encoded url back to plantuml text"""
#     data = base64.b64decode(plantuml_url.translate(
#         plantuml_to_b64).encode("utf-8"))
#     dec = zlib.decompressobj()  # without check the crc.
#     header = b'x\x9c'
#     return dec.decompress(header + data).decode("utf-8")


if __name__ == "__main__":
    # app.run(debug=True, host='0.0.0.0', port=4545)
    app.run(debug=True, host='127.0.0.1', port=6868)

    ## NOTE: post test
    # browser:: http://127.0.0.1:6868/send_post

    # uml = "Bob -> Alice : hi, Alice"
    # encoded = plantuml_encode(uml)
    # print(f"encoded: {encoded}")
    # f"https://www.plantuml.com/plantuml/png/{encoded}"
    # "https://www.plantuml.com/plantuml/png/SyfFKj2rKt3CoKnELR1IoCZKWR01"

    # Forked from https://gist.github.com/dyno/94ef6bb9644a88d6981d6a1a9eb70802
    # https://plantuml.com/text-encoding
    # https://github.com/dougn/python-plantuml/blob/master/plantuml.py#L64





    # uml = """
    # @startuml
    # Bob -> Alice : hello
    # @enduml
    # """

    # # url = "SyfFKj2rKt3CoKnELR1Io4ZDoSa700=="

    # # print(plantuml_decode(url))
    # # print(plantuml_encode(plantuml_decode(url)))


    # # import base64

    # # uml = """
    # # @startuml
    # # Bob -> Alice : hello
    # # @enduml
    # # """

    # # uml_bytes = uml.encode('ascii')
    # # uml_base64 = base64.b64encode(uml_bytes)
    # # uml_base64_str = uml_base64.decode('ascii')

    # # print(f"uml_bytes: {uml_bytes}")
    # # print(f"uml_base64: {uml_base64}")
    # # print(f"uml_base64_str: {uml_base64_str}")



