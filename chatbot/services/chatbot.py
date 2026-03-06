from .openai_client import OpenAIClient


class Chatbot:
    """Service for handling chatbot interactions."""

    SYSTEM_PROMPT = """
You are a helpful customer support agent for a SaaS billing platform. 
You answer customer questions about billing, subscriptions, refunds, 
account access, and general product questions. 
Keep answers clear, short, and helpful.
"""

    def __init__(self):
        self.client = OpenAIClient()

    def get_response(self, user_message: str) -> str:
        """Generate a chatbot response to the user message."""
        return self.client.generate_response(
            system_prompt=self.SYSTEM_PROMPT,
            user_message=user_message
        )
