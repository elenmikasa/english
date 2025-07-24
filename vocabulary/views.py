import logging
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Vocabulary
from .forms import VocabularyCreateForm, InquiryForm
from django.shortcuts import redirect

logger = logging.getLogger(__name__)

class IndexView(generic.ListView):
    model = Vocabulary
    template_name = "index.html"
    paginate_by = 2

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('vocabulary:inquiry')

    def form_valid(self, form):
        form.send_email()
        #messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class VocabularyDetailView(generic.DeleteView):
    model = Vocabulary
    template_name = "vocabulary_detail.html"

class VocabularyCreateView(generic.CreateView):
    model = Vocabulary
    template_name = 'vocabulary_create.html'
    form_class = VocabularyCreateForm
    success_url = reverse_lazy('vocabulary:index')

    def form_valid(self, form):
        vocabulary = form.save(commit=False)
        vocabulary.save()
        messages.success(self.request, '単語を登録しました。')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, '単語の登録に失敗しました。')
        return super().form_invalid(form)
    
class VocabularyUpdateView(generic.UpdateView):
    model = Vocabulary
    template_name = 'vocabulary_update.html'
    form_class = VocabularyCreateForm

    def get_success_url(self):
        return reverse_lazy('vocabulary:vocabulary_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '単語を更新しました。')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, '単語の更新に失敗しました。')
        return super().form_invalid(form)
    
class VocabularyDeleteView(generic.DeleteView):
    model = Vocabulary
    template_name = 'vocabulary_delete.html'
    success_url = reverse_lazy('vocabulary:index')

    def form_valid(self, form):
        messages.success(self.request, "単語を削除しました。")
        return super().form_valid(form)