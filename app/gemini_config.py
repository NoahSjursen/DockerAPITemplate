import google.generativeai as genai
import os



def get_model():
    # Access the API key
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    # Now use the API key
    genai.configure(api_key=GEMINI_API_KEY)

    # Set up the model
    generation_config = {
        "temperature": 0.9,
        "top_p": 0.95,
        "top_k": 32,
        "max_output_tokens": 8024,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE"
        },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)
    return model