import requests, os, openai

''' API REQUEST FROM OPENAI GPT 4'''

openai.api_key = os.getenv("OPENAI_API_KEY")

ELEVEN_LABS_API_KEY = os.getenv("ELEVEN_LABS_API_KEY")


character = "You are a thespian with over 20 years' experience in acting, script analysis, entertainment, content creator, emotional, character development, collaboration, performance, auditions, research and training."

def text_to_text_response(prompt):
  # Function used to call the GPT 4 API and returns the result
    system = {"role": "system", "content": character}
    user = {"role":"user", "content":prompt}
    try:
        response = openai.ChatCompletion.create( model="gpt-4", max_tokens=500, temperature=0.1, messages= [system, user])
        completion = response["choices"][0]["message"]["content"]
      
        return completion
    except Exception as e: 
        return ("Failed to get text response from GPT4 API")

