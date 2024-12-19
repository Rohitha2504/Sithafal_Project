from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the tokenizer and language model (use the correct model name)
tokenizer = AutoTokenizer.from_pretrained('gpt2')  # You can replace 'gpt2' with your model
language_model = AutoModelForCausalLM.from_pretrained('gpt2')  # Similarly, replace with the correct model

def generate_response(query, relevant_context):
    # Combine the query with the relevant context to form the input text
    input_text = query + " " + relevant_context
    
    # Tokenize the input text
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    
    # Print the length of input_ids for debugging purposes
    print("Input length:", len(input_ids[0]))  # To check the length of the input_ids tensor
    
    try:
        # Generate a response with a limit on the number of new tokens
        output = language_model.generate(
            input_ids,
            max_new_tokens=150,  # Limit the number of new tokens generated
            pad_token_id=tokenizer.eos_token_id  # Ensure the pad token is handled properly
        )

        # Decode the generated tokens to text
        output_text = tokenizer.decode(output[0], skip_special_tokens=True)
        
        # Return the generated text as the response
        return output_text
    except Exception as e:
        print(f"Error during response generation: {e}")
        return "Error generating response"
