from parsing_questions import parse_text, get_substring
import json
import subprocess

# Read text_string from file
with open("question_dump.txt", "r", encoding="utf-8") as file:
    text_string = file.read()
print('opened file')

parsed_questions = []
for question in text_string.split('Question: '):
    parsed_question = parse_text(question)
    parsed_questions.append(parsed_question)

json_data = json.dumps(parsed_questions, indent=4)
# print(f'Built json: {json_data}')

# Write json_data to file
with open("questions.json", "w") as file:
    file.write(json_data)

# trigger streamlit app 
import subprocess


# Capturing the output of a shell command
result = subprocess.run(["streamlit", "run", "exam.py"], capture_output=True, text=True)
print(result.stdout)

