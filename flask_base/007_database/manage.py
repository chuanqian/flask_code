from application import app,db
# from www import *

if __name__=="__main__":
	from common.models.user import User
	print("0")
	db.create_all()
	# app.run(host="0.0.0.0",port="8887",debug=True)