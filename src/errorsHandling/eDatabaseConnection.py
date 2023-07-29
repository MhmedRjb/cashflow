# Custom decorator to handle database connection errors
from flask import Blueprint,  jsonify
import pymysql  # Assuming you're using pymysql for database connection
from functools import wraps

def handle_database_errors(route_handler):
    @wraps(route_handler)
    def decorated_route_handler(*args, **kwargs):
        try:
            # Call the original route handler function with the provided arguments
            return route_handler(*args, **kwargs)

        except pymysql.Error as e:
            # If a database connection error occurs, return a 503 error (Service Unavailable)
            error_message = {'error': 'Database connection error'}
            return jsonify(error_message), 503

    return decorated_route_handler
