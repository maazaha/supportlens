import uuid
from django.db import models


class Trace(models.Model):
    """Model for storing chatbot interaction traces."""
    CATEGORY_CHOICES = [
        ('Billing', 'Billing'),
        ('Refund', 'Refund'),
        ('Account Access', 'Account Access'),
        ('Cancellation', 'Cancellation'),
        ('General Inquiry', 'General Inquiry'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_message = models.TextField()
    bot_response = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    response_time_ms = models.IntegerField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"Trace {self.id} - {self.category}"
