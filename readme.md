Now we study 
### routing


### variable rule
![hello](assets\${currentFileNameWithouExt}\2025-09-01-19-03-26.png)


### request and render_template 

1. request is a proxy global objecct we import it here to know the latest/ current server request for eq:- POST GET UPDATE DELETE 
2. render_template is a function in templates class and renders whatever .html file given in as arguement ...(it takes the path).</br>
One important thing about it is that the file has to be save in <b>templates</b> folder of whatever the enviroment we create 

```python
if request.method == "GET":
    return render_template("form.html")
```
### calculator 
1. calulator.html 
2. request getting postted 
3. changning the input recieved into float with 
```py
 num1 = request.values.get("num1") 
 num1 = float(num1)```

4. calculating 
```python 
 if operation == "add":
                result = num1 + num2```
5.return to the html page along with the result.(optional: send back the way otherwise since the page will be refreshed there wont be any thing in the boxes )
```python
 return render_template("calculator.html", result=result, num1=num1, num2=num2, operation=operation)

```

GET request is used to display the form initially.

When you first open /calculator in your browser, it sends a GET request.

Flask calls your route function. At this point:

if request.method == "POST":
    # calculation happens here


request.method is not POST yet, so the calculation code is skipped.

The function reaches the return render_template(...) line and renders the form (calculator.html) empty.

POST request happens after you submit the form.

The browser sends the entered numbers and operation to the same /calculator route.

Now request.method == "POST", so Flask performs the calculation and then renders the template again with the result.

