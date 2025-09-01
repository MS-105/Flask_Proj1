from flask import Flask

#creating Flask object 
#also telling flask how the app is ran 
app = Flask(__name__)
#if ran directly n
 
if __name__ == "__main__" :
    #start server 
    app.run(debug = True) # url: localhost , port: 500