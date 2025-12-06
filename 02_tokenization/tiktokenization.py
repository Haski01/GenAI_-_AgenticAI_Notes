import tiktoken

# Load GPT-4o tokenizer
encoding = tiktoken.encoding_for_model("gpt-4o-mini")

text = """
Hey buddy! This is Asad, Nice to meet you!
"""

# Encode text → list of token IDs
tokens = encoding.encode(text)

print(f"Tokens: {tokens}")
print(f"Total token count: {len(tokens)}")
