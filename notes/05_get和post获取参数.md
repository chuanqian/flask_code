#### GET和POST回去参数
##### get请求用request.args.get("键名")
```python
@index_page.route("/get")
def get():
	var_a = request.args.get("a","I like eat furit.") if "a" in request.args else ""
	var_b = "method: %s, params: %s, var_a: %s" % (request.method,request.args,var_a)
	return var_b
```
##### post请求用request.form["键名"]
```python
@index_page.route("/post",methods = ["POST"])
def post():
	var_a = request.form["a"] if "a" in request.form else ""
	var_b = request.form["b"] if "b" in request.form else ""
	return "method: %s, params: %s, var_a: %s, var_b: %s" % (request.method,req,var_a,var_b)
```
##### get和post请求都可用request.values方式获取数据
```python
@index_page.route("/post",methods = ["POST"])
def post():
	req = request.values
	var_a = req["a"] if "a" in req else ""
	var_b = req["b"] if "b" in req else ""
	return "method: %s, params: %s, var_a: %s, var_b: %s" % (request.method,req,var_a,var_b)

@index_page.route("/get")
def get():
	req = request.values
	var_a = req["a"] if "a" in req else ""
	var_b = "method: %s, params: %s, var_a: %s" % (request.method,request.args,var_a)
	return var_b
```
##### post请求上传文件
> 注意点：请求头里边参数必须有:enctyoe="multipart/from-data"
```python
@index_page.route("/upload",methods = ["POST"])
def upload():
	file = request.files["a"] if "a" in request.files else None
	return "method: %s, params: %s,file: %s" % (request.method,request.files,file)
```