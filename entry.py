# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for
from storage import BLOG_ENTRIES

def entry_page(key):
    if request.method=='GET':
        for blog_entry in BLOG_ENTRIES:
            if blog_entry['key']==key:
                return render_template('entry.html', blog_entry=blog_entry)
        return 'no entry'
    else:
        for i in range(len(BLOG_ENTRIES)):
            if BLOG_ENTRIES[i]['key']==key:
                BLOG_ENTRIES[i]['comments'].append({'name':request.form.get('name'),
                                                    'text':request.form.get('text')})
                break
        return redirect(url_for('entry_page', key=key))