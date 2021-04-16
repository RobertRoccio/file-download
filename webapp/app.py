from flask import Flask
from flask import send_file
app = Flask(__name__)

@app.route('/download')
def downloadFile ():
    path = "/test_file.zip"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(port=5000,debug=True)