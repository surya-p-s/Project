import json
from difflib import get_close_matches

def load_kb(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data:dict=json.load(file)
    return data

def save_kb(file_path: str, data:dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_bestmatch(user_question:str, questions:list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base:dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
      
        
def chat_bot():
    kb:dict=load_kb("E:\\bot\kb.json")
    print("Hi my name is IBot how I can help you today :)\n")
    while True:
        user_input: str=input('You:')

        if user_input.lower()=='quit':
            break
    
        best_match: str | None = find_bestmatch(user_input, [q["question"] for q in kb["questions"]])

        if best_match:
            answer: str =get_answer_for_question(best_match, kb)
            print(f'Bot: {answer}')
        else:
            print("Bot: I don't know. Can you teach me?")
            new_answer: str= input("Type answer or 'skip' to skip: ")

            if new_answer.lower() !='skip':
                kb["questions"].append({"question": user_input, "answer": new_answer})
                save_kb('kb.json',kb)
                print('Bot: Thank You! I learned! ')


if __name__ == '__main__':
    chat_bot()