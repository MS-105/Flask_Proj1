from flask import Flask, render_template, request

#creating Flask object + also telling flask how the app is ran
app = Flask(__name__)

#url Routing


@app.route("/") #default method = ["GET"]
def welcome():
    
    return "<h1>hello</h1>"

@app.route("/index")
def index():
    return "welcome to index page"

@app.route("/username/<username>")
def welcome2(username):
    return f"hello {username}"

#fCALCULATOR


@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    result = None
    num1 = request.values.get("num1")  # works for both GET and POST
    num2 = request.values.get("num2")
    operation = request.values.get("operation")

    if num1 and num2 and operation:  # only calculate if all present
        try:
            num1 = float(num1)
            num2 = float(num2)

            if operation == "add":
                result = num1 + num2
            elif operation == "sub":
                result = num1 - num2
            elif operation == "mul":
                result = num1 * num2
            elif operation == "div":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error: Division by zero"
        except Exception as e:
            result = f"Error: {e}"

    return render_template("calculator.html", result=result, num1=num1, num2=num2, operation=operation)



#if ran directly n 
if __name__ == "__main__" :
    #start server 
    app.run(debug = True) # url: localhost , port: 500