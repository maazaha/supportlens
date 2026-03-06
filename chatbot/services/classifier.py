from typing import Literal
from .openai_client import OpenAIClient

Category = Literal['Billing', 'Refund', 'Account Access', 'Cancellation', 'General Inquiry']


class Classifier:
    """Service for classifying chatbot interactions."""

    def __init__(self):
        self.client = OpenAIClient()

    def classify_interaction(self, user_message: str, bot_response: str) -> Category:
        """Classify the interaction into one of the predefined categories."""
        prompt = f"""
Classify the following customer support interaction into ONE category.

Categories:

Billing → invoices, charges, subscription pricing, payment methods
Refund → refund requests, charge disputes, money back
Account Access → login issues, password reset, locked accounts, MFA
Cancellation → cancel subscription, downgrade plan, close account
General Inquiry → product questions, features, how-to, anything else

Rules:
- Return ONLY the category name.
- If multiple topics appear, choose the PRIMARY intent.
- Never return anything outside the 5 categories.

Interaction:

User message:
{user_message}

Bot response:
{bot_response}

Category:
"""

        response = self.client.generate_response(
            system_prompt="You are a classifier that categorizes customer support interactions.",
            user_message=prompt
        )

        # Clean the response to ensure it's one of the categories
        response = response.strip()
        valid_categories = ['Billing', 'Refund', 'Account Access', 'Cancellation', 'General Inquiry']
        if response in valid_categories:
            return response  # type: ignore
        else:
            # Fallback to General Inquiry if invalid
            return 'General Inquiry'
