import requests

from config import get_secret

from ai.prompts import (
    SYSTEM_PROMPT,
    build_user_prompt
)


class GroqClient:

    def __init__(self):

        self.api_key = get_secret("GROQ_API_KEY")

        self.model = get_secret(
            "GROQ_MODEL",
            "llama-3.1-70b-versatile"
        )

    def ask(
        self,
        question,
        context="",
        diagnostics=None
    ):

        if not self.api_key:

            raise Exception(
                "Groq API Key not configured."
            )

        headers = {

            "Authorization":
            f"Bearer {self.api_key}",

            "Content-Type":
            "application/json"

        }

        payload = {

            "model": self.model,

            "temperature": 0.25,

            "max_tokens": 1800,

            "messages": [

                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },

                {
                    "role": "user",
                    "content": build_user_prompt(
                        question,
                        context,
                        diagnostics
                    )
                }

            ]
        }

        response = requests.post(

            "https://api.groq.com/openai/v1/chat/completions",

            headers=headers,

            json=payload,

            timeout=60

        )

        response.raise_for_status()

        return response.json()["choices"][0]["message"]["content"]
