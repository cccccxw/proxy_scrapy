#!/usr/bin/python3
# -*- coding: utf-8 -*-


from flask import Flask

from db.get_one_proxy import get_one_proxy



app = Flask(__name__)
app.debug = True


@app.route('/get/')
def get_one():
    a = get_one_proxy('ValueProxy')
    if a:
        return a
    else:
        return 'not value proxy'

def star_flask():
    app.run(host = '0.0.0.0',port = 9000,threaded=True)

if __name__ == '__main__':
    star_flask()
