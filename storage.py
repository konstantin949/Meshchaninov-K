# -*- coding: utf-8 -*-
import datetime


BLOG_ENTRIES = [
    {
        'key': 'some_id',
        'title': 'It\'s first entry',
        'text': """The term normalisation comes from the database world. It refers to transforming the schema of a 
        database to remove redundant information. Also, redundant information means the same data that is stored in more 
        than one place.""",
        'created_at': datetime.datetime.now(),
        'comments': [
            {
                'name': 'Julius Koronci',
                'text': 'Nice article'
            },
            {
                'name': 'Alexander Shirokov',
                'text': 'Thanks for good article'
            }
        ]
    },
{
        'key': 'some_id2',
        'title': 'It\'s first entry2',
        'text': """The term normalisation comes from the database world. It refers to transforming the schema of a 
        database to remove redundant information. Also, redundant information means the same data that is stored in more 
        than one place.""",
        'created_at': datetime.datetime.now(),
        'comments': [
            {
                'name': 'Julius Koronci',
                'text': 'Nice article'
            },
            {
                'name': 'Alexander Shirokov',
                'text': 'Thanks for good article'
            }
        ]
    },{
        'key': 'some_id3',
        'title': 'It\'s first entry3',
        'text': """The term normalisation comes from the database world. It refers to transforming the schema of a 
        database to remove redundant information. Also, redundant information means the same data that is stored in more 
        than one place.""",
        'created_at': datetime.datetime.now(),
        'comments': []
    }
]
