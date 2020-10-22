from werkzeug.exceptions import HTTPException

from app.app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError

app = create_app()


# 全局异常
@app.errorhandler(Exception)
def framework_error(e):
    # APIException
    # HTTPException
    # Exception
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        status = e.code
        msg = e.description
        code = e.code
        return APIException(msg, code, status)
    else:
        if app.config["DEBUG"]:
            raise e
        else:
            return ServerError()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
