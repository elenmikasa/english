from django.views import generic
from .models import Vocabulary

class IndexView(generic.ListView):
    model = Vocabulary
    template_name = "index.html"
