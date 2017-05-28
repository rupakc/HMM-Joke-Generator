from flask import Response,request, Flask
from hmm_text import TextGen
import time
import json

app = Flask(__name__)
api_version_url = '/api/v1/'


@app.route(api_version_url + 'joke')
def generate_joke():
    joke_length = 0
    if 'length' in request.args:
        joke_length = int(request.args['length'])
    text_generator = TextGen('')
    text_generator.load_model('chuck_hmm.bin')
    start_time = time.time()
    if joke_length != 0:
        joke = text_generator.get_short_sentence(joke_length)
    else:
        joke = text_generator.get_sentence()
    end_time = time.time()
    execution_time = (end_time-start_time)*1000.0
    response_dict = dict({'success':True,'joke':joke,'executionTime':execution_time})
    response = Response(json.dumps(response_dict),status=200,mimetype='application/json')

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)