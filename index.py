#!/usr/bin/env python

# -*- coding: utf-8 -*-

from app import app
from app.controllers import *

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)