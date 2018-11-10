from flask_restful import Resource

class Home(Resource):
  def get(self):
    return {'hello world': 'Welcome to Khmer Spelling checker API'}
