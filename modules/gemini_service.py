from google import genai
from dotenv import load_dotenv
import os
import time

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODELS = [
    "gemini-3.8-flash",
    "gemini-3.6-flash",
    "gemini-3.5-flash-lite"
]


def generate_response(prompt):

    for model in MODELS:

        for attempt in range(2):

            try:

                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )

                if response.text:
                    return response.text

                return "Error: Empty response received from AI."

            except Exception as e:

                error = str(e)

                print(f"Model {model} failed: {error}")

                # Retry temporary server/rate errors
                if "503" in error or "429" in error:

                    if attempt == 0:
                        time.sleep(2)
                        continue

                # Try the next model
                break

    return (
        "Error: AI service is temporarily unavailable. "
        "Please try again later."
    )