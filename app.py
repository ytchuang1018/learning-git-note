from flask import Flask

app = Flask(__name__) # setup app

# setup index.html
@app.route("/")  
def index():
    return "Hello!!"

@app.route('/news', methods=['GET'])
def get_news():
    return 'Get news'


@app.route('/news', methods=['POST'])
def post_news():
    return 'Post news'


@app.route('/news', methods=["PUT"])
def put_news():
    return 'PUT news'


@app.route('/news', methods=['DELETE'])
def delete_news():
    return 'Delete news'

app.run()