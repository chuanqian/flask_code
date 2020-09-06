from application import app

@app.errorhandler(404)
def error_404(e):
	app.logger.info("dfsadfasdfasdf")
	return "404 not found"