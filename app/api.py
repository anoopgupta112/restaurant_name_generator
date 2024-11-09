# Import necessary modules
from flask import Flask, request, jsonify
from app.langchain_helper import RestaurantGenerator
import os
app = Flask(__name__)

API_URL = os.getenv("API_URL")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

@app.route('/generate', methods=['GET'])
def generate_restaurant():
    cuisine = request.args.get('cuisine')

    if not cuisine:
        return jsonify({"error": "Cuisine parameter is required"}), 400

    generator = RestaurantGenerator()
    response = generator.generate_restaurant_name_and_items(cuisine)
    return jsonify(response)

@app.route('/',methods=['GET'])
def health_check():
    return {"status": "healthy"}


if __name__ == '__main__':
    app.run()


