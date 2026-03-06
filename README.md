# SupportLens

A lightweight observability platform for a support chatbot built with Django, OpenAI API, and SQLite.

## Features

- **Chatbot Interface**: Interactive chat for customer support
- **Backend API**: RESTful API for traces and analytics
- **Observability Dashboard**: Real-time analytics with charts and trace tables
- **LLM Integration**: Uses OpenAI GPT-4o-mini for chatbot responses and classification
- **Category Classification**: Automatically categorizes interactions into 5 categories

## Tech Stack

- **Backend**: Django 5.1.1
- **Database**: SQLite
- **LLM Provider**: OpenAI API
- **Frontend**: Django Templates + Chart.js
- **Deployment**: Ready for any Django-compatible hosting

## Setup Instructions

1. **Clone the repository** (or create the project as described)

2. **Create virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Copy `.env.example` to `.env`
   - Add your OpenAI API key: `OPENAI_API_KEY=your_api_key_here`

5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Seed sample data** (optional):
   ```bash
   python manage.py seed_traces
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the application**:
   - Chat interface: http://127.0.0.1:8000/
   - Dashboard: http://127.0.0.1:8000/dashboard/

## API Endpoints

### POST /api/traces
Create a new trace.

**Request Body**:
```json
{
  "user_message": "How do I reset my password?",
  "bot_response": "Click the 'Forgot Password' link...",
  "response_time_ms": 1200
}
```

### GET /api/traces
Get all traces, optionally filtered by category.

**Query Parameters**:
- `category`: Filter by category (Billing, Refund, etc.)

### GET /api/analytics
Get aggregated analytics data.

**Response**:
```json
{
  "total_traces": 150,
  "average_response_time": 1250.5,
  "categories": {
    "Billing": {"count": 45, "percentage": 30.0},
    "Refund": {"count": 20, "percentage": 13.3},
    ...
  }
}
```

### POST /chat
Chatbot endpoint for user interactions.

**Request Body** (form data):
```
message=How do I cancel my subscription?
```

## Project Structure

```
supportlens/
├── manage.py
├── supportlens/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── chatbot/
│   ├── models.py          # Trace model
│   ├── views.py           # API and UI views
│   ├── urls.py            # URL routing
│   ├── services/          # Business logic
│   │   ├── openai_client.py
│   │   ├── classifier.py
│   │   └── chatbot.py
│   ├── templates/
│   │   └── chatbot/
│   │       ├── chat.html
│   │       └── dashboard.html
│   └── management/
│       └── commands/
│           └── seed_traces.py
├── requirements.txt
├── .env.example
└── README.md
```

## Categories

Interactions are automatically classified into:

- **Billing**: Invoices, charges, subscriptions
- **Refund**: Refund requests, disputes
- **Account Access**: Login issues, password reset
- **Cancellation**: Cancel/pause subscriptions
- **General Inquiry**: Product questions, features

## Development

- Uses clean architecture with service layer separation
- Type hints and docstrings throughout
- Error handling and logging
- Modular, production-ready code structure

## License

This project is for demonstration purposes.
