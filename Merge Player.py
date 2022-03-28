# _*_coding:utf-8 _*_
from flask import Flask
from flask import Response
import mp3play

app = Flask(__name__)

@app.route('/audio/pcm_mp3/<file_key>')
def stream_mp3(file_key):
    def generate():
        path = 'http://win.web.nf01.sycdn.kuwo.cn/2aaa6c09748e5184ea1cec392c23811a/6240803a/resource/n1/80/89/665154269.mp3'
        with open(path, 'rb') as fmp3:
            data = fmp3.read(1024)
            while data:
                yield data
                data = fmp3.read(1024)

    return Response(generate(), mimetype="audio/mpeg3")

if __name__ == '__main__':
    # app.run(debug=True)
    # so the other machine can visit the website by ip
    app.run(host='127.0.0.1')