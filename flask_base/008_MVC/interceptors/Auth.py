from application import app

@app.before_request
def before_request():
	app.logger.info("before")
	return

@app.after_request
def after_request( response ):
	app.logger.info("after")
	return response