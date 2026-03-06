import time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Trace
from .services.classifier import Classifier
from .services.chatbot import Chatbot


@csrf_exempt
@login_required
@require_http_methods(["POST"])
def create_trace(request):
    """API endpoint to create a new trace."""
    try:
        data = request.POST or request.json()
        user_message = data.get('user_message')
        bot_response = data.get('bot_response')
        response_time_ms = int(data.get('response_time_ms', 0))

        if not user_message or not bot_response:
            return JsonResponse({'error': 'user_message and bot_response are required'}, status=400)

        # Classify the interaction
        classifier = Classifier()
        category = classifier.classify_interaction(user_message, bot_response)

        # Save the trace
        trace = Trace.objects.create(
            user_message=user_message,
            bot_response=bot_response,
            category=category,
            response_time_ms=response_time_ms
        )

        return JsonResponse({
            'id': str(trace.id),
            'user_message': trace.user_message,
            'bot_response': trace.bot_response,
            'category': trace.category,
            'timestamp': trace.timestamp.isoformat(),
            'response_time_ms': trace.response_time_ms
        }, status=201)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@login_required
@require_http_methods(["GET"])
def get_traces(request):
    """API endpoint to get traces with optional filtering."""
    category = request.GET.get('category')
    traces = Trace.objects.all()
    if category:
        traces = traces.filter(category=category)

    data = [
        {
            'id': str(trace.id),
            'user_message': trace.user_message,
            'bot_response': trace.bot_response,
            'category': trace.category,
            'timestamp': trace.timestamp.isoformat(),
            'response_time_ms': trace.response_time_ms
        }
        for trace in traces
    ]
    return JsonResponse({'traces': data})

@login_required
@require_http_methods(["GET"])
def get_analytics(request):
    """API endpoint to get analytics data."""
    traces = Trace.objects.all()
    total_traces = traces.count()
    if total_traces == 0:
        return JsonResponse({
            'total_traces': 0,
            'average_response_time': 0.0,
            'categories': {}
        })

    average_response_time = sum(trace.response_time_ms for trace in traces) / total_traces

    categories = {}
    category_counts = {}
    for trace in traces:
        category_counts[trace.category] = category_counts.get(trace.category, 0) + 1

    for cat in Trace.CATEGORY_CHOICES:
        cat_name = cat[0]
        count = category_counts.get(cat_name, 0)
        percentage = (count / total_traces) * 100 if total_traces > 0 else 0
        categories[cat_name] = {
            'count': count,
            'percentage': round(percentage, 2)
        }

    return JsonResponse({
        'total_traces': total_traces,
        'average_response_time': round(average_response_time, 2),
        'categories': categories
    })


@csrf_exempt
@require_http_methods(["POST"])
def chat(request):
    """Endpoint for chatbot interaction."""
    try:
        data = request.POST or request.json()
        user_message = data.get('message')

        if not user_message:
            return JsonResponse({'error': 'message is required'}, status=400)

        chatbot = Chatbot()
        start_time = time.time()
        bot_response = chatbot.get_response(user_message)
        response_time_ms = int((time.time() - start_time) * 1000)

        # Save trace
        classifier = Classifier()
        category = classifier.classify_interaction(user_message, bot_response)

        trace = Trace.objects.create(
            user_message=user_message,
            bot_response=bot_response,
            category=category,
            response_time_ms=response_time_ms
        )

        return JsonResponse({
            'response': bot_response,
            'trace_id': str(trace.id)
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def chat_view(request):
    """UI view for the chat interface."""
    return render(request, 'chatbot/chat.html')


def dashboard_view(request):
    """UI view for the dashboard."""
    return render(request, 'chatbot/dashboard.html')


@require_http_methods(["POST"])
def login_view(request):
    """Handle user login."""
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid credentials'})


@require_http_methods(["POST"])
def signup_view(request):
    """Handle user signup."""
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    if User.objects.filter(username=username).exists():
        return JsonResponse({'success': False, 'error': 'Username already exists'})
    if User.objects.filter(email=email).exists():
        return JsonResponse({'success': False, 'error': 'Email already exists'})
    user = User.objects.create_user(username=username, email=email, password=password, is_active=False)
    return JsonResponse({'success': True, 'message': 'Account created. Wait for admin activation.'})


def logout_view(request):
    """Handle user logout."""
    logout(request)
    return redirect('chat_view')
