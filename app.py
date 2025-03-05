from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='speed_tester')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists('speed_tester'):
        os.makedirs('speed_tester')
    app.run(debug=True)