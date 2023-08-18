import re
import json

def get_substring(string, substring):
    string = ''.join(char for char in string if not char.isdigit())
    index = string.find(substring)
    if index != -1:
        return string[:index]
    else:
        return string

def parse_text(text):
    # questions = []

    # question_matches = re.findall(r"Question:\s+(\d+)\n(.*?)\n([ABCDE])\.\n", text, re.DOTALL)
    newline_splits = text.split('\n')
    # print(f'newline_splits: {newline_splits}')
    Question = None
    Choices = []
    Answer = ""

    for split in newline_splits: 
        if split in ["A.", "B.", "C.", "D.", "E.", "F."]:
            if Question is None:
                Question = get_substring(text, previous_split)
                # print(f'\nQuestion: {Question}')
            
            choice = previous_split
            Choices.append(choice)
            # print(f"choice: {choice}")

        if "Answer: " in split:
            # print(f'\nsplit: {split}')
            ans_choice = split[-1] #split.strip("Answer: ")
            # print(f'ans_choice: {ans_choice}')

            Answer = Choices[ord(ans_choice) - ord('A')]
            # print(f'Answer: {Answer}')

        previous_split = split
    
    Explanation = text.split("Explanation/Reference:")[-1]
    # print(f'Explanation: {Explanation}')

    question = {
            "question": Question,
            "choices": Choices,
            "answer": Answer,
            "explanation": Explanation
        }
    
    return question


# # Read text_string from file
# with open("question_dump.txt", "r", encoding="utf-8") as file:
#     text_string = file.read()
# print('opened file')

# parsed_questions = []
# for question in text_string.split('Question: '):
#     parsed_question = parse_text(question)
#     parsed_questions.append(parsed_question)

# json_data = json.dumps(parsed_questions, indent=4)
# # print(f'Built json: {json_data}')

# # Write json_data to file
# with open("questions.json", "w") as file:
#     file.write(json_data)