from django.shortcuts import render
from django.views import View
from .models import *
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseNotFound,HttpResponse
# Create your views here.
class ShowArticlesView(View):
    def get(self, request):
        articles = Article.objects.all()
        articles_authors = Article.author.through.objects.all()
        authors = Author.objects.all()
        context={
            'articles': articles,
            'articles_authors': articles_authors,
            'authors': authors,
        }
        return render(request, 'articles_app/blog.html', context)
    
    
class ShowBlogDetailsView(View):
    def get(self, request, slug):
        article = Article.objects.get(slug = slug)
        image_list = os.listdir(settings.MEDIA_ROOT+'/images/articles/article_'+str(article.id))
        article.view_number+=1
        article.save()
        articles_authors = Article.objects.get(id=article.id).author.through.objects.all()
        authors = Author.objects.all()
        context={
            'article': article,
            'articles_authors': articles_authors,
            'authors': authors,
            'media_url': settings.MEDIA_URL,
            'image_list': image_list,
        }
        return render(request, 'articles_app/blog_details.html', context)


class ShowArticlePdfView(View):
    def get(self, request, article_id):
        fs = FileSystemStorage()
        file_name = 'article_'+str(article_id)+'.pdf'
        file_path = 'pdf_files/'+file_name
        if fs.exists(file_path):
            with fs.open(file_path) as pdf:
                response = HttpResponse(pdf, content_type = 'application/pdf')
                response['Content-Disposition'] = 'inline;file_name='+file_name
                return response

        else :
            return HttpResponseNotfound('The requested pdf file ws not found in our server')



