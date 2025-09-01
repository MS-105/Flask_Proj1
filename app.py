from flask import Flask

#creating Flask object + also telling flask how the app is ran
app = Flask(__name__)

#url Routing


@app.route("/") #default method = ["GET"]
def welcome():
    
    return "<h1>hello</h1>"

@app.route("/index")
def index():
    return "welcome to index page"

#if ran directly n 
if __name__ == "__main__" :
    #start server 
    app.run(debug = True) # url: localhost , port: 500