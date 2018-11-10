from flask_restful import reqparse, Resource
from word_segmentation_v2 import WordSegmentation

parser = reqparse.RequestParser()
parser.add_argument('sentences')

class SpellingCheck(Resource):
  def post(self):
    args = parser.parse_args()
    sentences = args['sentences']

    return sentences, 201
