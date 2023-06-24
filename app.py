from flask import Flask, render_template
import prompt

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/prompt_page')
def prompt_page():
    #motion = prompt.create_motion()
    return render_template('prompt.html')
    
@app.route('/run_motion')
def run_motion():
    motion = prompt.create_motion()
    return motion