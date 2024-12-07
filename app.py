from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__,
            static_url_path='', 
            static_folder='static')

@app.route("/")
def index():
    return send_from_directory("static", 'index.html')

# Route to receive the buttonColors list
@app.route('/submit-colors', methods=['POST'])
def poop():
    print('poop')

if __name__ == '__main__':
    app.run(debug=True)