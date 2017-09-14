from flask import Flask, request
import MeCab
import json

app = Flask(__name__)


def parse_text(text):
    tagger = MeCab.Tagger("-Owakati")
    result = tagger.parse(text)
    print('result=', result)
    return result.split(' ')


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/parse', methods=['GET', 'POST'])
def parse():
    if request.method == 'GET':
        text = request.args.get('text')
    if request.method == 'POST':
        text = request.form['text']

    print('text=', text)
    if text:
        words = parse_text(text.encode('utf-8'))
        return json.dumps({'result': words})
    return json.dumps({'error': 'no text'})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
