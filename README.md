# LLM-RAGs

# RAGS Text Generation API

This project implements an advanced text generation API using GPT-2 from Huggingface's `transformers` library. The model is served via a Flask API, allowing users to generate text based on a provided prompt.

## Features

- Utilizes GPT-2 for text generation
- Supports advanced text generation parameters like:
  - `temperature`
  - `top_k` (Top-K sampling)
  - `top_p` (Nucleus sampling)
  - `repetition_penalty` (to avoid repetition)

## Prerequisites

Ensure you have Python 3.7 or higher installed. Install the required dependencies before running the application.

## Installation

1. Clone the repository and navigate to the project directory:

   git clone https://github.com/your-username/rags-text-generation-api.git
   cd rags-text-generation-api

2. Install the required dependencies:

    pip install transformers torch flask

3. Running the Application

    To run the Flask API:
    python app.py

This will start the Flask server on http://127.0.0.1:5000.

## API Usage
POST /generate - Generates text based on a given prompt.

## Request
Endpoint: /generate
Method: POST
Content-Type: application/json
Body Parameters:
- prompt (string, required): The initial text prompt to generate from.
- max_length (int, optional): Maximum length of the generated text. Default is 50.
- temperature (float, optional): Sampling temperature. Default is 0.9.
- top_k (int, optional): Number of top K tokens to consider. Default is 50.
- top_p (float, optional): Nucleus sampling threshold. Default is 0.85.
- repetition_penalty (float, optional): Penalty for repeating sequences. Default is 1.2.

## Example Request

curl -X POST http://127.0.0.1:5000/generate \
-H "Content-Type: application/json" \
-d '{
  "prompt": "Once upon a time in a faraway land",
  "max_length": 100,
  "temperature": 0.9,
  "top_k": 50,
  "top_p": 0.85,
  "repetition_penalty": 1.2
}'


## Example Response
{
  "generated_text": "Once upon a time in a faraway land, there was a peaceful village hidden deep within the forest. The villagers were kind and lived harmoniously with nature until one fateful day when..."
}


## Configuration Options
You can modify the behavior of text generation by adjusting the following parameters:

- max_length: Controls how long the generated text will be.
- temperature: Higher values (like 0.9) produce more diverse results, while lower values (like 0.7) make the output more deterministic.
- top_k: Restricts the token selection to the top k most probable next tokens.
- top_p: Uses nucleus sampling, where the cumulative probability of the selected tokens is p.
- repetition_penalty: A value greater than 1.0 penalizes repetitive tokens in the output.

