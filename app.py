from slacker import Slacker
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, jsonify, abort, make_response, request, url_for
import forecastio


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False, threaded=True)
