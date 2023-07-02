from flask import Flask, json
import logging

app = Flask(__name__)

log_config = '%(asctime)s %(levelname)s in %(module)s: %(message)s'
logging.basicConfig(format=log_config, level=logging.INFO)


@app.route('/hello')
def hello_world():
    app.logger.info("GET hello")
    return 'Hello World!'


@app.route('/html')
def handler_html():
    app.logger.info("GET html")
    return '<h1>This is html</h1><p1>Some text in html</p1>'


@app.route('/json')
def handler_json():
    abs_dict = json.dumps([
        {
            "name": "Eugen",
            "age": 28,
            "phone": "0996663322",
        },
        {
            "name": "Alex",
            "age": 25,
            "phone": "0996665511",
        },
    ])
    app.logger.info("GET json")
    return abs_dict


if __name__ == '__main__':
    app.run()
