from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "This is homepage !"
    
@app.route("/salvador")
def salvador():
    return "Hello, Salvador"
    
if __name__ == "__main__":
    app.run(debug=True)