# coding:utf-8
import yzm_predict_api
from flask import Flask, jsonify, request
import base64

app = Flask(__name__)

@app.route('/captcha/v1/singlewindows', methods=['GET'])
def translate_single_windows():
    if 'url' in request.args:
        single_url = request.args['url']
#        print(single_url)
        content = yzm_predict_api.predict_url(single_url)
        return jsonify({"captcha": content,"captcha_jpg":"http://172.16.0.53/captcha/captcha.jpg"})


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "UP"})


#    if 'captcha' in request.args:
#        yzm = request.args['captcha']
#        print("para:",yzm)
#        print("para_type:",type(yzm))
#        content = yzm_predict_api.predict_yzm(yzm)
#        return jsonify({"captcha": content})


if __name__ == "__main__":
#    print("url=https://app.singlewindow.cn/cas/plat_cas_verifycode_gen")
#    captcha=base64.b64encode(open('yzm_download/1539575497643336.jpg','rb').read())
#    print("orig:",captcha)
#    print("orig_type:",type(captcha))
    app.run(host='172.16.0.53', port=7777, debug=False)
