from flask import Flask
from flask import send_file
app = Flask(__name__)

@app.route('/download')
def downloadFile ():
    path = "test_file.zip"
    #return send_file(path, as_attachment=True)
    return send_file(path)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)