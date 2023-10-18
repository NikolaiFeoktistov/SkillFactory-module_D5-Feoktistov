
from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import NewsForm

def news_list(request):
    news_list = News.objects.all()
    paginator = Paginator(news_list, 10)  # Разбиваем новости на страницы, по 10 новостей на каждой
    page = request.GET.get('page')
    news = paginator.get_page(page)
    return render(request, 'news/news_list.html', {'news': news})


def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'news/news_detail.html', {'news': news})


def news_search(request):
    # Получение параметров поиска из GET-запроса
    search_date = request.GET.get('date')
    search_title = request.GET.get('title')
    search_author = request.GET.get('author')

    # Фильтрация новостей на основе параметров поиска
    news_list = News.objects.all()

    if search_date:
        news_list = news_list.filter(pub_date__gte=search_date)

    if search_title:
        news_list = news_list.filter(title__icontains=search_title)

    if search_author:
        news_list = news_list.filter(author__username=search_author)

    # Реализация постраничного вывода
    paginator = Paginator(news_list, 10)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    return render(request, 'news/news_search.html', {'news': news})


def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect('news:news_detail', news.id)
    else:
        form = NewsForm()
    return render(request, 'news/news_form.html', {'form': form})

def news_edit(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            news = form.save()
            return redirect('news:news_detail', news.id)
    else:
        form = NewsForm(instance=news)
    return render(request, 'news/news_form.html', {'form': form, 'news': news})

def news_delete(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if request.method == 'POST':
        news.delete()
        return redirect('news:news_list')
    return render(request, 'news/news_confirm_delete.html', {'news': news})