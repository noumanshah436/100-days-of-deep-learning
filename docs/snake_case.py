import re

def to_snake_case(text):
    # Replace any non-alphanumeric characters (except underscore) with spaces
    text = re.sub(r'[^a-zA-Z0-9_]', ' ', text)
    # Insert underscore before uppercase letters (unless it's the first character)
    text = re.sub(r'(?<!^)(?=[A-Z])', '_', text)
    # Replace spaces and multiple underscores with a single underscore
    text = re.sub(r'[\s_]+', '_', text)
    # Convert to lowercase
    return text.lower()

 
word_with_spaces = "day7_ Multi-head Attention"
snake_case_word_with_spaces = to_snake_case(word_with_spaces)
print(f"Original: {word_with_spaces}")
print(f"Snake Case: {snake_case_word_with_spaces}")
 

#   python docs/snake_case.py