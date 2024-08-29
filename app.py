import os
from flask import Flask, request
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

shutdown_flag = False

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/log')
def log_message():
    logging.info("Endpoint /log chiamato")
    return "Messaggio loggato"

@app.route('/shutdown', methods=['GET'])
def shutdown():
    global shutdown_flag
    shutdown_flag = True
    logging.info("Richiesta di shutdown ricevuta")
    return "Shutdown in corso"

@app.route('/health')
def health():
    if shutdown_flag:
        return "Shutting down", 503
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)