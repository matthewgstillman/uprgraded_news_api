from django.shortcuts import render, redirect
import requests, datetime
from api_key import api_key
# Create your views here.
def index(request):
    url = ('https://newsapi.org/v2/top-headlines?',
       'country=us&'
       'apiKey=8c10097819d448beab0f6ac908990fa5')
    response = requests.get(url)
    news_data = response.json()
    articles = news_data['articles']
    print(articles)
    # print news_data.json()
    context = {
        'articles': articles,
        'news_data': news_data,
        # 'news_source': news_source,
        'response': response
    }
    return render(request, 'upgraded_news_api/index.html', context)

def abc(request):
    url = ('https://newsapi.org/v2/top-headlines?'
       'sources=abc-news&'
       'apiKey=8c10097819d448beab0f6ac908990fa5')
    response = requests.get(url)
    abc_news_data = response.json()
    abc_articles = abc_news_data['articles']
    print(abc_articles)
    context = {
        'abc_articles': abc_articles,
        'abc_news_data': abc_news_data,
        'response': response,
    }
    return render(request, 'upgraded_news_api/abc.html', context)

def ap(request):
    url = ('https://newsapi.org/v2/top-headlines?'
       'sources=associated-press&'
       'apiKey=8c10097819d448beab0f6ac908990fa5')
    response = requests.get(url)
    ap_news_data = response.json()
    ap_articles = ap_news_data['articles']
    print(ap_articles)
    context = {
        'ap_articles': ap_articles,
        'ap_news_data': ap_news_data,
        'response': response,
    }
    return render(request, 'upgraded_news_api/ap.html', context)

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

def bleacherreport(request):
    url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bleacher-report&'
       'apiKey=8c10097819d448beab0f6ac908990fa5')
    response = requests.get(url)
    bleacher_report_news_data = response.json()
    bleacher_report_articles = bleacher_report_news_data['articles']
    print(bleacher_report_articles)
    context = {
        'bleacher_report_articles': bleacher_report_articles,
        'bleacher_report_news_data': bleacher_report_news_data,
        'response': response,
    }
    return render(request, 'upgraded_news_api/bleacherreport.html', context)

def bloomberg(request):
    url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bloomberg&'
       'apiKey=8c10097819d448beab0f6ac908990fa5')
    response = requests.get(url)
    bloomberg_news_data = response.json()
    bloomberg_articles = bloomberg_news_data['articles']
    print(bloomberg_articles)
    context = {
        'bloomberg_articles': bloomberg_articles,
        'bloomberg_news_data': bloomberg_news_data,
        'response': response,
    }
    return render(request, 'upgraded_news_api/bloomberg.html', context)


def cnn(request):
    url = ('https://newsapi.org/v2/top-headlines?'
       'sources=cnn&'
       'apiKey=8c10097819d448beab0f6ac908990fa5')
    response = requests.get(url)
    cnn_news_data = response.json()
    cnn_articles = cnn_news_data['articles']
    print(cnn_articles)
    context = {
        'cnn_articles': cnn_articles,
        'cnn_news_data': cnn_news_data,
        'response': response,
    }
    return render(request, 'upgraded_news_api/cnn.html', context)

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


def politico(request):
    url = ('https://newsapi.org/v2/top-headlines?'
       'sources=politico&'
       'apiKey=8c10097819d448beab0f6ac908990fa5')
    response = requests.get(url)
    politico_news_data = response.json()
    politico_articles = politico_news_data['articles']
    print(politico_articles)
    context = {
        'politico_articles': politico_articles,
        'politico_news_data': politico_news_data,
        'response': response
    }
    return render(request, 'upgraded_news_api/politico.html', context)

def usatoday(request):
    url = ('https://newsapi.org/v2/top-headlines?'
       'sources=usa-today&'
       'apiKey=8c10097819d448beab0f6ac908990fa5')
    response = requests.get(url)
    usa_today_news_data = response.json()
    usa_today_articles = usa_today_news_data['articles']
    print(usa_today_articles)
    context = {
        'usa_today_articles': usa_today_articles,
        'usa_today_news_data': usa_today_news_data,
        'response': response
    }
    return render(request, 'upgraded_news_api/usa_today.html', context)

def wsj(request):
    url = ('https://newsapi.org/v2/top-headlines?'
       'sources=the-wall-street-journal&'
       'apiKey=8c10097819d448beab0f6ac908990fa5')
    response = requests.get(url)
    wsj_news_data = response.json()
    wsj_articles = wsj_news_data['articles']
    print(wsj_articles)
    context = {
        'wsj_articles': wsj_articles,
        'wsj_news_data': wsj_news_data,
        'response': response
    }
    return render(request, 'upgraded_news_api/wsj.html', context)

def wapost(request):
    url = ('https://newsapi.org/v2/top-headlines?'
       'sources=the-washington-post&'
       'apiKey=8c10097819d448beab0f6ac908990fa5')
    response = requests.get(url)
    wapost_news_data = response.json()
    wapost_articles = wapost_news_data['articles']
    print(wapost_articles)
    context = {
        'wapost_articles': wapost_articles,
        'wapost_news_data': wapost_news_data,
        'response': response
    }
    return render(request, 'upgraded_news_api/wapost.html', context)

