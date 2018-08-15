import datetime
import os
import random

import imgkit
from flask import Flask
from flask import request
from flask import send_file

# __file__ refers to the file settings.py
APP_ROOT = os.path.dirname(os.path.abspath(__file__))  # refers to application_top
APP_TEMPLATE = os.path.join(APP_ROOT, 'template')

app = Flask(__name__)


def get_prepared_html(input_data):
    with open(os.path.join(APP_TEMPLATE, 'template.html'), 'r') as template:
        data = template.read()
    html_string = data.format(**input_data)
    return html_string


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/receipt')
def get_receipt():
    input_data = {}
    input_data['amount'] = request.args.get('amount')
    input_data['recv_by'] = request.args.get('recv_by')
    input_data['recv_from'] = request.args.get('recv_from')
    input_data['purpose'] = request.args.get('purpose')
    input_data['date'] = datetime.date.today()
    input_data['recpt_number'] = "TUFRCPT" + str(random.randint(1, 101))
    html_string = get_prepared_html(input_data)
    imgkit.from_string(html_string, os.path.join(APP_TEMPLATE, 'out.jpg'))
    return send_file(os.path.join(APP_TEMPLATE, 'out.jpg'), mimetype='image/gif')


port = int(os.getenv("PORT", 3000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
