from application import app,db,manager
from www import *
from flask_script import Server,Command

manager.add_command("runserver", Server(host="0.0.0.0", use_debugger=True, use_reloader=True))

# 生成数据库表
@Command
def create_all():
	from common.models.user import User
	print("enter")
	db.create_all()

manager.add_command("create_all",create_all)

def main():
	manager.run()

if __name__=="__main__":
	# app.run(host="0.0.0.0",port="8887",debug=True)
	manager.run()
	try:
		import sys
		sys.exit(main())
	except Exception as e:
		import traceback
		traceback.print_exc()