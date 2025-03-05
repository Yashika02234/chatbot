"""
This module defines the routes for the Travel Planner Bot Flask application.
It includes routes for the home page, NLP testing, and weather data retrieval.
"""

from flask import render_template, jsonify, request
from app.services.nlp_service import extract_destination
from app.services.weather_service import get_weather

def init_routes(app):
    """
    Initialize the routes for the Flask application.

    Args:
        app (Flask): The Flask application instance.
    """
    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/test-nlp")
    def test_nlp():
        text = "I want to visit Paris next month."
        destination = extract_destination(text)
        return jsonify({"input": text, "extracted_destination": destination})

    @app.route("/weather")
    def weather():
        city = request.args.get("city", "Paris")  # Default to Paris if no city is provided
        weather_data = get_weather(city)
        if weather_data:
            return jsonify(weather_data)
        return jsonify({"error": "Failed to fetch weather data"}), 500
