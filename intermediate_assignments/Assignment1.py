from flask import Flask,request,render_template
import os
app=Flask(__name__)
UPLOAD_FOLDER=os.path.join(os.path.expanduser("~"), "desktop")
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
@app.route('/')
def display_page():
    return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload_file():
    try:
        file=request.files['file']
        filename=file.filename
        file_location=os.path.join(app.config['UPLOAD_FOLDER'],filename)
        file.save(file_location)
        with open(file_location) as f:
            read_file=f.read()

            return render_template('content.html',text=read_file)

    except Exception as e:
        return e
if __name__=='__main__':
    app.run()