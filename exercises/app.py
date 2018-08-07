from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
#def home_page(year=2020):
    #return render_template (
    	#"index.html",year= year)


def likes_same_sport():
    players = ["marco asensio", "ronaldo", "iscoo"] 
    return render_template("index.html",players = players)


if __name__ == '__main__':
   app.run(debug = True)