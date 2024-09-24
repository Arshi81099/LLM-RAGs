from flask import Flask, request, jsonify
from rags import RAGS  # Import the RAGS model from rags.py

app = Flask(__name__)

# Initialize the RAGS model
model = RAGS()

# API route to generate text from a prompt
@app.route('/generate', methods=['POST'])
def generate_text():
    # Get the input JSON data
    data = request.get_json()

    # Get the prompt and parameters from the request data
    prompt = data.get('prompt', None)
    max_length = data.get('max_length', 50)
    temperature = data.get('temperature', 0.7)  # Default temperature to 0.7
    top_k = data.get('top_k', 50)  # Default top_k to 50
    top_p = data.get('top_p', 0.9)  # Default top_p to 0.9

    # Ensure the prompt is provided
    if not prompt:
        return jsonify({'error': 'Prompt is required!'}), 400

    try:
        # Use the RAGS model to generate text
        generated_text = model.generate(prompt, max_length, temperature, top_k, top_p)
        return jsonify({'generated_text': generated_text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
