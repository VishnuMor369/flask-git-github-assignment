from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv(override=True)

mongo_uri = os.getenv("MONGODB_URI")
client = MongoClient(mongo_uri)
db = client.test
collection = db['todo_collection']

app = Flask(__name__ ,template_folder="../frontend/templates")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    try:
        form_data = dict(request.form)
        collection.insert_one(form_data)

        return render_template('index.html',message="Todo item submitted successfully!")

    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True)