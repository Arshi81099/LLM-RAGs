from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class RAGS:
    def __init__(self, model_name='gpt2'):
        # Load pre-trained GPT-2 tokenizer and model
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        self.model.eval()  # Set model to evaluation mode

    def generate(self, prompt, max_length=50, temperature=0.9, top_k=50, top_p=0.85, repetition_penalty=1.2):
        # Tokenize the input prompt
        inputs = self.tokenizer(prompt, return_tensors='pt')
        
        # Generate text with temperature, top_k, top_p, and repetition_penalty
        with torch.no_grad():
            outputs = self.model.generate(
                inputs.input_ids,
                max_length=max_length,
                temperature=temperature,   # Control randomness in generation
                top_k=top_k,               # Only consider the top-k tokens
                top_p=top_p,               # Nucleus sampling (cumulative probability sampling)
                repetition_penalty=repetition_penalty,  # Penalizes repetition
                num_return_sequences=1,
                pad_token_id=self.tokenizer.eos_token_id  # EOS token for padding
            )
        
        # Decode the generated tokens into text
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return generated_text
