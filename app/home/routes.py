# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app.home import blueprint
from flask import render_template, redirect, url_for, request
import requests
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound

@blueprint.route('/index')
@login_required
def index():

    return render_template('index.html', segment='index')

@blueprint.route('/mission')
@login_required
def missionApi():
    # response = requests.get('https://jsonplaceholder.typicode.com/posts')
    response = requests.get('http://localhost:3000/dataPackage')
    

    
    
    if response.status_code != 200:
        # This means something went wrong.
        print('{} {}'.format(response.status_code))
    
    package_data_list = response.json()

    package_data_list1 = response.json()
    

    return render_template('mission.html', package_data_list = package_data_list,  package_data_list1 = package_data_list1 )
    
@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith( '.html' ):
            template += '.html'

        # Detect the current page
        segment = get_segment( request )

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template( template, segment=segment )

    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
    except:
        return render_template('page-500.html'), 500

# Helper - Extract current page name from request 
def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  

# @app.route("/users", methods=['GET'])
# def get_user():
#     return {
#         "user": "John Doe",
#     }