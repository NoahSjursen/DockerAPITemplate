
import os
from gemini_config import get_model

async def method_1(arg_1: str, arg_2: str, arg_3: str):
    model = get_model() # get the model from gemini_config.py
    prompt = f"Arg 1: {arg_1}, Arg 2: {arg_2}, Arg 3: {arg_3}"
    response = model.generate_content(prompt) # generate content from the model
    return {"message": response.text}


