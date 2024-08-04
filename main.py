import json

from difflib import get_close_matches

#get_close_matches is going to allow us to try to match the best response for the input which 
#we give to our chat bot

#function to load knowledge base from JSON File into the program
#file path will return us dictionary
def load_knowledge_base(file_path: str) -> dict:  # takes file path as input and reads the json file at that path 
    with open(file_path,'r') as file:
        data: dict =json.load(file) #deserialization(Repesentation of JSON data using Native Python Objects such as list and Strings)
    return data

#function thats going to save the dictonary of responses to the knowledge base(json file) so that the next time we use the program we will 
#have the old responses in the memory. so that we can load it later again>>
def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=8)#serialization(pakaging python object into JSON format )

#Function which is going to find the Best Match from the dictionary
def find_best_match(user_question: str, question: list[str])-> str | None: #identifying The best response
    matches: list =get_close_matches(user_question,question,n=1,cutoff=0.6)
    return matches[0] if matches else None
        
#Function that gets the answer for each question
#takes input  question of type string and  a knowledge base to type dictionary
def get_answer_for_question(question:str,knowledge_base:dict) -> str | None:  #Retrives the answer associated with a given question from a knowledge base.
    for q in knowledge_base["questions"]:
         if q["question"]==question:
             return  q["answer"]


def chat_bot():
    #It loads the initial knowledge base from a JSON file and enters into a loop to interact with the user.
    knowledge_base: dict =load_knowledge_base('knowledge_base.json')

    while True:
        #infinite loop
        user_input: str=input('You: ')
        
        #exit condition
        if user_input.lower() == 'quit':
            break

        # Data type for best match is optional string or none
        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f'Bot: {answer}')
        else:
            print('Bot: I dont know the answer can you teach me?')
            new_answer: str =input('Type the answer or "skip" to skip: ')

            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({"question":user_input,"answer":new_answer})
                #appending Question and answers associated with it in knowledge base 
                save_knowledge_base('knowledge_base.json',knowledge_base)
                print('Bot: Thank you! I learned a new Response!')
   
if __name__== '__main__':
    chat_bot()

# •	It executes the chat_bot function when the script is run.

# •	The program starts by loading the knowledge base from a JSON file.
# •	It then enters a loop where the user can input questions.
# •	If the user inputs "quit," the loop breaks, and the program ends.
# •	If the user's input matches a question in the knowledge base, the chatbot retrieves and prints the corresponding answer.
# •	If there's no exact match, the chatbot uses get_close_matches to find a close match. If one is found, it retrieves and prints the corresponding answer.
# •	If no match is found, the chatbot asks the user to provide an answer and updates the knowledge base with the new question-answer pair.
# •	The updated knowledge base is then saved to the JSON file.
# This way, the chatbot learns and improves its responses over time based on user input.
