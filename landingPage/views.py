from django.shortcuts import render
from datetime import datetime

def index(request):
    """
    View function for the index page.

    Retrieves the current datetime and passes it to the rendered response as a context variable.

    Args:
        request: A HttpRequest object representing the current request.

    Returns:
        A rendered response to the 'index.html' template with the current datetime passed as a context variable.
    """
    now = datetime.now()  # get the current datetime
    return render(request, 'index.html', {'now': now})
