#### Response相应
##### 文本响应
```python
@index_page.route("/text")
def text():
	return "text/html"

@index_page.route("/text_same")
def text_same():
	return "text/html",200
```
##### json格式响应
```python
# 第一种方式，自己设置响应头信息
@index_page.route("/jsons")
def jsons():
	data= {"a":"b"}
	response = make_response(json.dumps(data))
	response.headers["Content-Type"]="application/json"
	return response

# 第二种方式，使用flask中封装好的jsonify,jsonify中封装了相应头信息
@index_page.route("/json_same")
def json_same():
	data={"a":"b"}
	response = make_response(jsonify(data))
	return response
```
##### 模板相应
**第一种方式**：使用flask中封装的render_templates来实现
```python
# 文件结构为：
# 	-当前文件
# 	-templates
# 		-hello.html
@index_page.route("/templates")
def templates():
	return render_template("hello.html")
```
```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>Hello Flask</title>
	<link rel="stylesheet" href="">
</head>
<body>
	<h1>今天你好吗？</h1>
</body>
</html>
```
**第二种方式**：使用jinja2模板来实现
```python
# 模板中传递变量(方式1)
@index_page.route("/templates_cdbl1")
def templates_cdbl1():
	name = "你今天还好吗？"
	return render_template("hello.html",name=name)

#模板中传递变量(方式2)
@index_page.route("/templates_cdbl2")
def templates_cdbl2():
	name = "你今天高兴吗？"
	context = {"name":name}
	return render_template("hello.html", **context)


#模板中传递变量(方式3)
@index_page.route("/templates_cdbl3")
def templates_cdbl3():
	context = {}
	context["user"] = {"name":"name","qq":"1178995389@qq.com","main":"https://www.cnblogs.com/qianchuan/"}
	context["tem_num"] = [1,2,3,4,5]
	return render_template("hello.html", **context)
```
```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Hello Flask</title>
    <link rel="stylesheet" href="">
</head>

<body>
    <h1>今天你好吗？</h1>
    <br>
    {% if user %}
    <h1>昵称：{{ user.name }}</h1>
    <h1>联系QQ:{{ user.qq }}</h1>
    <h1>主页:{{ user.main }}</h1>
    {% endif %}
    {% for temp_num in tem_num %}
    {{ temp_num }}
    {% endfor %}
</body>

</html>
```
> jinja2模板继承：判断jinja中最强大的部分就是模板继承。模板继承允许你构建一个包含你站点共同元素的基本模板"骨架"，并定义子模版可以覆盖的块。听起来复杂，实际上很简单
```python
# 模板继承
@index_page.route("/extend_template")
def extend_template():
	return render_template("extend_template.html")
```
```html
<!-- -template
	-common
		-layout.html
	-extend_template.html -->

<!-- layout.html -->
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>这里是统一模板</title>
	<link rel="stylesheet" href="">
</head>
<body>
{% block content %} {% endblock %}
</body>
</html>

<!-- extend_template.html -->
{% block content %}
<h1>今天的你开心吗？</h1>
{% endblock %}
```