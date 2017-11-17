from django.shortcuts import render

# Create your views here.
def index(request):
    """
        The main view of our website
    """

    # Data can be passed to template via context dictionary
    # The context consists of pairs of name (string) and value (any object)
    # Templates can then refer to these names and retrieve the data
    context = {
        'a_string': 'this is a test of passing data to a template',
        'a_number': 7357
    }

    return render(request, 'index.html', context)
