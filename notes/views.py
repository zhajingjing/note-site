from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Article, Notes
# from .notes_form import NotesForm
from transformers import pipeline


def index(request):
    latest_article_list = Article.objects.order_by("-pub_date")[:5]
    context = {
        "latest_article_list": latest_article_list,
    }
    return render(request, "notes/index.html", context)


def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, "notes/article.html", {"article": article})


def create_you(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == "GET":
        notes_obj = Notes()
        notes_obj.reference_text = request.GET.get('ref',default='')
        notes_obj.notes_text = ""
        return render(request, "notes/notes_form.html", {"article": article, "notes": notes_obj, "mode": 0})
    elif request.method == "POST":
        _reference_text = request.POST.get('reference_text',default='')
        _notes_text = request.POST.get('notes_text',default='')
        article.notes_set.create(reference_text=_reference_text, notes_text=_notes_text, create_user='zjjing@umich.edu')
        return HttpResponseRedirect(reverse("notes:article",args=(article.id,)))


def create_ai(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == "GET":
        notes_obj = Notes(type=1)
        notes_obj.reference_text = request.GET.get('ref',default='')
        summarizer = pipeline("summarization", "facebook/bart-large-cnn")
        notes_obj.notes_text = summarizer(notes_obj.reference_text, do_sample=False)[0]['summary_text']
        return render(request, "notes/notes_form.html", {"article": article, "notes": notes_obj, "mode": 0})
    elif request.method == "POST":
        _reference_text = request.POST.get('reference_text',default='')
        _notes_text = request.POST.get('notes_text',default='')
        article.notes_set.create(type=1, reference_text=_reference_text, notes_text=_notes_text, create_user='zjjing@umich.edu')
        return HttpResponseRedirect(reverse("notes:article",args=(article.id,)))


def update(request, notes_id):
    notes_obj = get_object_or_404(Notes, pk=notes_id)
    if request.method == 'POST':
        notes_obj.notes_text = request.POST.get('notes_text',default='')
        notes_obj.save()
        return HttpResponseRedirect(reverse("notes:article", args=(notes_obj.article_id,)))
    else:
        return render(request, "notes/notes_form.html", {"notes": notes_obj, "mode": 1})


def delete(request, notes_id):
    notes_obj = get_object_or_404(Notes, pk=notes_id)
    article_id = notes_obj.article.id
    notes_obj.delete()
    return HttpResponseRedirect(reverse("notes:article", args=(article_id,)))
    
