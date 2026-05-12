from flask import Flask, request, jsonify, send_from_directory
import os
from json_to_xml import json_to_xml

app = Flask(__name__, static_folder='static')

# Serve the frontend UI
@app.route('/')
def index():
    return app.send_static_file('index.html')

# API Endpoint for conversion
@app.route('/api/convert', methods=['POST'])
def convert_json():
    try:
        # Get the JSON data from the request body
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        # Call our transformation function
        xml_output = json_to_xml(data)
        
        # Return the XML as a JSON response
        return jsonify({'xml': xml_output}), 200
        
    except Exception as e:
        # Handle invalid JSON or other errors securely
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    # Run the server on port 5000
    app.run(debug=True, port=5000)
