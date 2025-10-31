from django.shortcuts import render, get_object_or_404
from .models import ReadingText


# ----------------- HOME / LIST VIEW -----------------
def text_list(request):
    # Get entries with non-empty English or Urdu text
    english_texts = ReadingText.objects.exclude(english_text__exact='').order_by('-date')
    urdu_texts = ReadingText.objects.exclude(urdu_text__exact='').order_by('-date')
    context = {
        'english_texts': english_texts,
        'urdu_texts': urdu_texts
    }
    return render(request, 'core/text_list.html', context)


# ----------------- ENGLISH READING PAGE -----------------
def text_english_read(request, pk):
    text = get_object_or_404(ReadingText, pk=pk)
    return render(request, 'core/text_english_read.html', {'text': text})


# ----------------- URDU READING PAGE -----------------
def text_urdu_read(request, pk):
    text = get_object_or_404(ReadingText, pk=pk)
    return render(request, 'core/text_urdu_read.html', {'text': text})
