from django.core.management.base import BaseCommand
from chatbot.models import Trace
import random


class Command(BaseCommand):
    help = 'Seed the database with sample traces'

    def handle(self, *args, **options):
        # Clear existing traces
        Trace.objects.all().delete()

        sample_data = [
            {
                'user_message': 'How do I view my current billing cycle?',
                'bot_response': 'You can view your billing cycle in the dashboard under the Billing section.',
                'category': 'Billing',
                'response_time_ms': random.randint(500, 2000)
            },
            {
                'user_message': 'I was charged twice for the same month',
                'bot_response': 'I apologize for the inconvenience. Let me check your account and process a refund.',
                'category': 'Refund',
                'response_time_ms': random.randint(500, 2000)
            },
            {
                'user_message': 'I forgot my password and can\'t log in',
                'bot_response': 'I can help you reset your password. Please check your email for the reset link.',
                'category': 'Account Access',
                'response_time_ms': random.randint(500, 2000)
            },
            {
                'user_message': 'I want to cancel my subscription',
                'bot_response': 'I\'m sorry to hear that. Let me guide you through the cancellation process.',
                'category': 'Cancellation',
                'response_time_ms': random.randint(500, 2000)
            },
            {
                'user_message': 'What features are included in the premium plan?',
                'bot_response': 'The premium plan includes advanced analytics, priority support, and unlimited storage.',
                'category': 'General Inquiry',
                'response_time_ms': random.randint(500, 2000)
            },
            {
                'user_message': 'Can you explain the charges on my invoice?',
                'bot_response': 'I\'d be happy to break down your invoice. The charges include base subscription and add-ons.',
                'category': 'Billing',
                'response_time_ms': random.randint(500, 2000)
            },
            {
                'user_message': 'I need a refund for the service outage last week',
                'bot_response': 'Due to the recent outage, we\'re offering prorated refunds. I\'ll process that for you.',
                'category': 'Refund',
                'response_time_ms': random.randint(500, 2000)
            },
            {
                'user_message': 'My account is locked after too many failed attempts',
                'bot_response': 'Accounts are locked after 5 failed login attempts for security. Use the unlock link in your email.',
                'category': 'Account Access',
                'response_time_ms': random.randint(500, 2000)
            },
            {
                'user_message': 'How do I downgrade my plan?',
                'bot_response': 'You can downgrade your plan in settings. The change takes effect at the next billing cycle.',
                'category': 'Cancellation',
                'response_time_ms': random.randint(500, 2000)
            },
            {
                'user_message': 'Is there a mobile app available?',
                'bot_response': 'Yes, we have mobile apps for iOS and Android with full feature support.',
                'category': 'General Inquiry',
                'response_time_ms': random.randint(500, 2000)
            },
            {
                'user_message': 'When will I be billed next?',
                'bot_response': 'Your next billing date is the 15th of each month.',
                'category': 'Billing',
                'response_time_ms': random.randint(500, 2000)
            },
            {
                'user_message': 'I was overcharged for additional users',
                'bot_response': 'Let me review your user count and issue a credit for the extra charges.',
                'category': 'Refund',
                'response_time_ms': random.randint(500, 2000)
            },
            {
                'user_message': 'How do I enable two-factor authentication?',
                'bot_response': 'Go to account settings and select "Enable 2FA" to set up authentication.',
                'category': 'Account Access',
                'response_time_ms': random.randint(500, 2000)
            },
            {
                'user_message': 'I need to close my account permanently',
                'bot_response': 'I understand. Let me help you with account closure and data export.',
                'category': 'Cancellation',
                'response_time_ms': random.randint(500, 2000)
            },
            {
                'user_message': 'Can you integrate with Slack?',
                'bot_response': 'Yes, we offer Slack integration through our API and webhook system.',
                'category': 'General Inquiry',
                'response_time_ms': random.randint(500, 2000)
            },
            {
                'user_message': 'What payment methods do you accept?',
                'bot_response': 'We accept credit cards, PayPal, and bank transfers for all plans.',
                'category': 'Billing',
                'response_time_ms': random.randint(500, 2000)
            },
            {
                'user_message': 'Please refund my subscription fee',
                'bot_response': 'I\'ll process your refund request. It may take 3-5 business days to appear in your account.',
                'category': 'Refund',
                'response_time_ms': random.randint(500, 2000)
            },
            {
                'user_message': 'I can\'t access my account from a new device',
                'bot_response': 'For security, new devices require email verification. Check your inbox.',
                'category': 'Account Access',
                'response_time_ms': random.randint(500, 2000)
            },
            {
                'user_message': 'How do I pause my subscription?',
                'bot_response': 'You can pause your subscription for up to 3 months in your account settings.',
                'category': 'Cancellation',
                'response_time_ms': random.randint(500, 2000)
            },
            {
                'user_message': 'What\'s the difference between plans?',
                'bot_response': 'Basic plan has core features, Pro adds analytics, Enterprise includes custom integrations.',
                'category': 'General Inquiry',
                'response_time_ms': random.randint(500, 2000)
            },
        ]

        for data in sample_data:
            Trace.objects.create(**data)

        self.stdout.write(
            self.style.SUCCESS(f'Successfully seeded {len(sample_data)} sample traces')
        )
