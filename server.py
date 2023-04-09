import os
from flask import Flask, render_template, request, jsonify
from chains import query_chain, search_agent
import markdown

q = query_chain()
s = search_agent()

# get path for static files
static_dir = os.path.join(os.path.dirname(__file__), 'static')  
if not os.path.exists(static_dir): 
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

# start server
server = Flask(__name__, static_folder=static_dir, template_folder=static_dir)

@server.route('/')
def landing():
    return render_template('index.html')

@server.route('/query', methods=['POST'])
def query():
    data = request.json
    response = q.predict(input=data["input"])
    return jsonify({'query': data["input"],
                    'response': str(response),
                    'markdown': markdown.markdown(response, 
                    extensions=['fenced_code', 'codehilite'])})

@server.route('/search', methods=['POST'])
def search():
    data = request.json
    response = s.run(input=data["input"])
    return jsonify({'search': data["input"],
                    'response': str(response),
                    'markdown': markdown.markdown(response, 
                    extensions=['fenced_code', 'codehilite'])})