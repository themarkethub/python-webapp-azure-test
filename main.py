from __future__ import print_function

from flask import *
import jsonpickle
from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import bcrypt
from hashlib import md5
from flask_login import current_user, login_user
from flask_security import login_required
from flask import Flask
from flask import request
from flask import Flask, jsonify
from flask import abort
from flask_pymongo import PyMongo
import os
from bson.json_util import dumps
from flask import Flask, render_template, url_for, json, request, flash, redirect
import json
import requests
from werkzeug import secure_filename
import os
import pickle
import sys
import csv
import time
import sys
import datetime
from flask_login import LoginManager

from jinja2 import Environment, PackageLoader
from flask import make_response, flash
from flask import session as login_session

from flask import abort
from flask import make_response
from flask import request
from flask import url_for
import json
from bson import json_util
import os
# add mongo db alta


import pprint
import os
import flask
from werkzeug.routing import BaseConverter, ValidationError
from itsdangerous import base64_encode, base64_decode
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import urllib, json

import httplib2
import json
import requests
import random
import string
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, IntegerField, TextAreaField, validators, StringField, SubmitField
import logging
from transitions import Machine
import random
from insightly import Insightly


from apiclient import discovery
from apiclient.http import MediaIoBaseDownload, MediaFileUpload
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, Azure!!'

if __name__ == '__main__':
  app.run()
