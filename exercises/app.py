from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return "my fav sport is football"

if __name__ == '__main__':
   app.run(debug = True)