from django.shortcuts import render, redirect
import requests, datetime
# Create your views here.
def index(request):
    url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=8c10097819d448beab0f6ac908990fa5')
    response = requests.get(url)
    news_data = response.json()
    articles = news_data['articles']
    # print news_source
    print(articles)
    # print news_data.json()
    context = {
        'articles': articles,
        'news_data': news_data,
        # 'news_source': news_source,
        'response': response
    }
    return render(request, 'upgraded_news_api/index.html', context)

def bbc(request):
    url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=8c10097819d448beab0f6ac908990fa5')
    response = requests.get(url)
    bbc_news_data = response.json()
    bbc_articles = bbc_news_data['articles']
    print(bbc_articles)
    context = {
        'bbc_articles': bbc_articles,
        'bbc_news_data': bbc_news_data,
        'response': response,
    }
    return render(request, 'upgraded_news_api/bbc.html', context)

def foxnews(request):
    url = ('https://newsapi.org/v2/top-headlines?'
       'sources=fox-news&'
       'apiKey=8c10097819d448beab0f6ac908990fa5')
    response = requests.get(url)
    fox_news_data = response.json()
    fox_news_articles = fox_news_data['articles']
    print(fox_news_articles)
    context = {
        'fox_news_articles': fox_news_articles,
        'fox_news_data': fox_news_data,
        'response': response,
    }
    return render(request, 'upgraded_news_api/foxnews.html', context)


def nytimes(request):
    url = ('https://newsapi.org/v2/top-headlines?'
       'sources=the-new-york-times&'
       'apiKey=8c10097819d448beab0f6ac908990fa5')
    response = requests.get(url)
    ny_times_news_data = response.json()
    ny_times_articles = ny_times_news_data['articles']
    print(ny_times_articles)
    context = {
        'ny_times_articles': ny_times_articles,
        'ny_times_news_data': ny_times_news_data,
        'response': response
    }
    return render(request, 'upgraded_news_api/nytimes.html', context)