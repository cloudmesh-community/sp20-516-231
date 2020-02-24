from flask import jsonify
import connexion
app = connexion.App(__name__, specification_dir='./')
app.add_api('echo.yaml')
@app.route('/')
def home():
    msg = {'msg',"It's working!"}
    return jsonify(msg)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
