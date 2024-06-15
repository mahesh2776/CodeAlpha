def chat():
    print("Chatbot:Hello! i am your chatbot")
    print("Chatbot:feel free to ask anything.If you want to exit please type Bye")
    while(True):
        k=input("You: ")
        if k.lower()=="bye":
            print("Chatbox: I enjoyed a lot...thanks for chatting with me")
            break
        else:
            f=respond(k)
            print("chatbox: ",f)
def respond(k):
    if "hello" in k.lower() or "hi" in k.lower():
        return "hi,how are you>"
    elif "how are you" in k.lower():
        return "I am doing great"
    elif "open" in k.lower():
        return "Sorry, I dont have permissions for that task"
    elif "bye" in k.lower():
        return "Bye had a great time with you"
    else:
        return "Sorry ,I didnt understand "
if __name__=="__main__":
    chat()
    