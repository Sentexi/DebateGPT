from flask import Flask, render_template
import prompt

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/prompt')
def prompt():
    motion = prompt.create_motion()
    return render_template('prompt.html')