from flask_restful import Api


class APIException(Exception):
  def __init__(self, code, message):
    self._code = code
    self._message = message

  @property
  def code(self):
    return self._code

  @property
  def message(self):
    return self._message

  def __str__(self):
    return self.__class__.__name__ + ': ' + self.message


class RepoNotAllowedException(APIException):
  def __init__(self):
    super().__init__(403, 'Repo is not allowed to run')


class ParametersFormatIncorrectException(APIException):
  def __init__(self, message):
    super().__init__(400, message)


class JobNotFoundException(APIException):
  def __init__(self):
    super().__init__(404, 'Job doesn\'t exists')

class ExceptionHandler(Api):
    def handle_error(self, e):
      if not hasattr(e, 'data'):
        e.data = e
      if isinstance(e, APIException):
        return self.make_response({'status': e.code, 'message': e.message}, e.code)
      return super(ExceptionHandler, self).handle_error(e)
