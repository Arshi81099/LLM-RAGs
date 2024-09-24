from flask import Flask, request, jsonify
from rags import RAGS  

app = Flask(__name__)

model = RAGS()

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.get_json()

    prompt = data.get('prompt', None)
    max_length = data.get('max_length', 50)
    temperature = data.get('temperature', 0.7) 
    top_k = data.get('top_k', 50)  
    top_p = data.get('top_p', 0.9)

    if not prompt:
        return jsonify({'error': 'Prompt is required!'}), 400

    try:
        generated_text = model.generate(prompt, max_length, temperature, top_k, top_p)
        return jsonify({'generated_text': generated_text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
