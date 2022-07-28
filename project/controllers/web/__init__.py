# -*- coding: utf-8 -*-
__version__ = '0.1'
from project import app
import os
import glob
from flask import session, redirect, url_for


__all__ = [os.path.basename(
    f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]


@app.route('/')
def index():
    if not session.get("name"):
        return redirect(url_for('login'))
    else:
        return redirect(url_for('users'))
    # return render_template('index.html')
