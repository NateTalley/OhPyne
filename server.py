from flask import Flask, send_file, jsonify

app = Flask(__name__)

@app.route('')
def home()
    return send_file('ohpyne.html')

@app.route('apiproxy', methods=['GET', 'POST'])
def proxy_endpoint()
    # Your AI logic goes here
    return jsonify({response AI data loaded successfully})

if __name__ == '__main__'
    app.run(port=8000)