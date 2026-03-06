import os
from typing import Optional
import httpx
from openai import OpenAI


class OpenAIClient:
    """Client for interacting with OpenAI API."""

    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv('OPENAI_API_KEY'),
            http_client=httpx.Client()
        )
        self.model = "gpt-4o-mini"

    def generate_response(self, system_prompt: str, user_message: str) -> str:
        """Generate a response using OpenAI chat completion."""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.7,
                max_tokens=500
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")
