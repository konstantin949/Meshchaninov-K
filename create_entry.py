# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for
import datetime, random
from storage import BLOG_ENTRIES

def create_entry_page():
    if request.method=='GET':
        return render_template('create_entry.html')
    else:
        blog={
        'key': str(random.randint(0,10)),
        'title': request.form.get('title'),
        'text': request.form.get('text'),
        'created_at': datetime.datetime.now(),
        'comments': []
        }
        BLOG_ENTRIES.append(blog)
    return redirect(url_for('entry_page', key=blog['key']))
