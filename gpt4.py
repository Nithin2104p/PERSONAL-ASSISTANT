import g4f

def GPT(message):
    try:
        response=g4f.ChatCompletion.create(
            model="gpt-4-32k-0613",
            provider=g4f.Provider.GPTalk,
            messages=[{"role":"user","content":message}],
            stream=True
        )
        ms=""
        for i in response:
            ms+=i
            print(i,end="",flush=True)
        return ms
    except Exception as e:
        print("i cant get you,try again bcz :",e)
        
# GPT("write python code for addition of two numbers in javascript")

