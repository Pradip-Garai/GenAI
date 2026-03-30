from dotenv import load_dotenv
load_dotenv()

import re
import time
import sys
import threading
import os

from langchain.chat_models import init_chat_model

model = init_chat_model("google_genai:gemini-2.5-flash")
model2 = init_chat_model("groq:llama-3.3-70b-versatile")
model3 = init_chat_model("mistral-tiny")
model4 = init_chat_model("openrouter:openrouter/free")  

val = True


# Typing effect function
def typing_effect(text, delay=0.01):
    print()
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)



# Thinking animation
stop_loading = False


def thinking():
    
    animation = ["Thinking.", "Thinking..", "Thinking..."]
    i = 0
    while not stop_loading:
        print("\r" + animation[i % len(animation)], end="", flush=True)
        time.sleep(0.5)
        i += 1

print("\nOpenRouter: ")
while val:
    query = input("\nAsk Anything : ")
    print()

    try:
        # Start thinking animation
        stop_loading = False
        t = threading.Thread(target=thinking)
        t.start()

        # API call
        response1 = model4.invoke(query)

        # Stop animation FIRST
        stop_loading = True
        time.sleep(0.1)   # 🔥 give time to stop
        t.join()

        # Clear line properly 
        sys.stdout.write("\r" + " " * 50 + "\r")
        sys.stdout.flush()
 
        content = response1.content

        # Cleaning
        content = content.replace("**", "")
        content = content.replace('"', '')
        content = content.replace("###", "\n")
        content = re.sub(r"- ", "\n• ", content)
        content = re.sub(r"\n+", "\n", content)
        typing_effect(content) 

        Continue = input("\nContinue? YES/NO: ").lower()
        if Continue == "yes":
            val = True
        else:
            val = False

    except Exception as e:
        print("Mistral Error:", e)