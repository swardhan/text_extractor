from flask import Flask, render_template, request
from flask_restful import Resource, Api, reqparse
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'arjuna'
api = Api(app)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class ImageUpload(Resource):
    def post(self):
        data = request.get_json()
        image_data = data['image']
        # Saving Image to Database
        fh = open("imageToSave.png", "wb")
        fh.write(image_data.decode('base64'))
        fh.close()
        return {"message": "Imaga Uploaded"}



api.add_resource(ImageUpload, '/uploadimage')

if  __name__ == '__main__':
    app.run(debug=True)
