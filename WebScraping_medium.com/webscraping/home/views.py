from django.shortcuts import render, HttpResponse
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from home.models import Search_History

def index(request):
    return render(request, 'index.html')

def scraper(request):
    if request.method == "POST":
        tags = request.POST.get('tags')

        url= "https://medium.com/search?q=" + tags 

        r = requests.get(url)
        htmlContent = r.content
        soup = BeautifulSoup(htmlContent, 'html.parser')

        all_titles = []
        titles = soup.find_all('div', class_="section-inner sectionLayout--insetColumn")
        for title in titles:
            all_titles.append(title.h3.text)
        size = len(all_titles)

        all_authors = []
        authors = soup.find_all('a', class_="ds-link ds-link--styleSubtle link link--darken link--accent u-accentColor--textNormal u-accentColor--textDarken")
        for author in authors:
            all_authors.append(author.text)

        all_links = []
        links = soup.find_all('div', class_="postArticle-content")
        for link in links:
            all_links.append(link.a.get('href'))

        all_dates = []
        dates = soup.find_all('div', class_="ui-caption u-fontSize12 u-baseColor--textNormal u-textColorNormal js-postMetaInlineSupplemental")
        for date in dates:
            all_dates.append(date.a.time.text)

        all_times = []
        times = soup.find_all('span', class_="readingTime")
        for time in times:
            all_times.append(time.get('title'))

        i=0
        data = []
        while i<size:
            data.append([all_titles[i], all_authors[i], all_links[i], all_dates[i], all_times[i]])
            i=i+1

        context = {
            "tagName": tags,
            "datas": data
        }
        return render(request, 'scraper.html', context)

def blog(request):
    if request.method == "POST":
        blog_tag = request.POST.get('blogTag')
        blog_link = request.POST.get('blogLink')
        blog_title = request.POST.get('blogTitle')
        blog_author = request.POST.get('blogAuthor')
        blog_date = request.POST.get('blogDate') 
        blog_time = request.POST.get('blogTime')

        r = requests.get(blog_link)
        htmlContent = r.content
        soup = BeautifulSoup(htmlContent, 'html.parser')

        image = soup.find('figure', class_="paragraph-image")
        blog_image = image.img.get('src')

        all_details = []
        details = soup.find_all('p')
        for detail in details:
            all_details.append(detail.text)
        j = 3
        blog_detail = ""
        while j < len(all_details):
            blog_detail = blog_detail + all_details[j]
            j = j + 1

        info = {
            "blog_Link": blog_link,
            "blog_Title": blog_title,
            "blog_Author": blog_author,
            "blog_Date": blog_date,
            "blog_Image": blog_image,
            "blog_Time": blog_time,
            "blog_Detail": blog_detail
        }

        history = Search_History(Blog_Tag=blog_tag, Blog_Title=blog_title, Blog_Author=blog_author, Publishing_Date=blog_date, Estimated_Reading_Time=blog_time, date=datetime.today())
        history.save()

        return render(request, 'blog.html', info)