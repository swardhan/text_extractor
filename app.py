from flask import Flask, render_template, request
from flask_restful import Resource, Api, reqparse
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'arjuna'
api = Api(app)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/uploadform')
def form():
    return render_template('form.html')

class ImageUpload(Resource):
    def post(self):
        print(request.is_json)
        data = request.get_json()
        image_data = data['image']
        # Saving Image to Database
        fh = open("imageToSave.png", "wb")
        fh.write(image_data.decode('base64'))
        fh.close()
        return render("Image Uploaded")



api.add_resource(ImageUpload, '/uploadimage')

if  __name__ == '__main__':
    app.run(debug=True)
