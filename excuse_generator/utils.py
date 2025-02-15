import os
import random
import json
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_schema": content.Schema(
    type = content.Type.OBJECT,
    properties = {
      "cringe_excuse": content.Schema(
        type = content.Type.STRING,
      ),
    },
  ),
  "response_mime_type": "application/json",
}

vibe_choices = ["Hilarious and Witty","Serious and Logical", "Overdramatic and Extra"]
desperation_choices = ["chill","medium","high"]



def generate_random_excuse(prompt=None):
    prompt = f'''
    Vibe: {random.choice(vibe_choices)}
    Desperation Level: {random.choice(desperation_choices)}
    Situation:
    ''' 
    model = genai.GenerativeModel(
      model_name="gemini-2.0-flash",
      generation_config=generation_config,
      system_instruction="Generate a hilariously cringe excuse text that I can send to my partner to get out of a situation. The excuse should match the given vibe and desperation level, making it as ridiculous, dramatic, or absurd as needed.\"\n\nInput:\nVibe: <vibe>\nDesperation Level: <desperation level>\nSituation: <situation>\n\nOutput:\nA single cringe-worthy excuse text, written in a way that sounds believable (or not).\nShould align with the vibe and desperation level selected.\nCan include emojis, exaggeration, or ridiculous justifications for extra effect.\nNo explanations - just a raw excuse message ready to copy and send.\n\n<<<output format>>{cringe_excuse: excuse}<<<output format>>",
    )

    chat_session = model.start_chat()

    response = chat_session.send_message(prompt)

    return json.loads(response.text)

def generate_custom_excuse(prompt=None):
    model = genai.GenerativeModel(
      model_name="gemini-2.0-flash",
      generation_config=generation_config,
      system_instruction="Generate a hilariously cringe excuse text that I can send to my partner to get out of a situation. The excuse should match the given vibe and desperation level, making it as ridiculous, dramatic, or absurd as needed.\"\n\nInput:\nVibe: <vibe>\nDesperation Level: <desperation level>\nSituation: <situation>\n\nOutput:\nA single cringe-worthy excuse text, written in a way that sounds believable (or not).\nShould align with the vibe and desperation level selected.\nCan include emojis, exaggeration, or ridiculous justifications for extra effect.\nNo explanations - just a raw excuse message ready to copy and send.\n\n<<<output format>>{cringe_excuse: excuse}<<<output format>>",
    )

    chat_session = model.start_chat()

    response = chat_session.send_message(prompt)

    return json.loads(response.text)