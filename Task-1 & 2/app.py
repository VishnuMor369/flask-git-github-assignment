from flask import Flask
#For json file conversion
import json

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    # reads the data from backend (data)/data.json
    with open('backend (data)/data.json', 'r') as file:
        #Loads the data and convert into json format
        data = json.load(file)

    return data

if __name__ == '__main__':
    app.run(debug=True)