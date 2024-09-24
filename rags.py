from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class RAGS:
    def __init__(self, model_name='gpt2'):
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        self.model.eval() 

    def generate(self, prompt, max_length=50, temperature=0.9, top_k=50, top_p=0.85, repetition_penalty=1.2):
        inputs = self.tokenizer(prompt, return_tensors='pt')
        
        with torch.no_grad():
            outputs = self.model.generate(
                inputs.input_ids,
                max_length=max_length,
                temperature=temperature,  
                top_k=top_k,             
                top_p=top_p,              
                repetition_penalty=repetition_penalty,  
                num_return_sequences=1,
                pad_token_id=self.tokenizer.eos_token_id 
            )
        
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return generated_text
