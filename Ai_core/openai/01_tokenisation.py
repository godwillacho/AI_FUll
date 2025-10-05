import tiktoken 
"""
This script demonstrates how to tokenize a text string using the `tiktoken` library for the GPT-4o model.
Steps:
1. Imports the `tiktoken` library.
2. Loads the encoding configuration for the GPT-4o model.
3. Defines a sample text string.
4. Encodes the text into tokens using the model's encoding.
5. Prints the resulting list of tokens.
Note:
- The decoding functionality is commented out and not used in this script.
"""

enc = tiktoken.encoding_for_model('gpt-4o')
text = 'hey There! My name is Godwill Acho'

token = enc.encode(text)
print('Tokens', token)

decod = enc.decode([48467, 3274, 0, 3673, 1308, 382, 4809, 21053, 143389])
print(decod)