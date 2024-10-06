from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone 
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    family = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    email = models.EmailField(max_length=200, verbose_name='ایمیل', null=True, blank=True)
    mobile = models.CharField(max_length=100, verbose_name='شماره تماس', null=True, blank=True)
    is_active = models.BooleanField(default=False, verbose_name='وضعیت')
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسندکان'
        db_table = 't_author'


class ArticleGroup(models.Model):
    group_title = models.CharField(max_length=100, verbose_name='عنوان گروه مقالات')

    def __str__(self):
        return self.group_title
    
    class Meta:
        verbose_name = 'گروه مقاله'
        verbose_name_plural = 'گروه مقاله ها'
        db_table = 't_article_group'


class Article(models.Model):
    group = models.ForeignKey(ArticleGroup, on_delete=models.CASCADE, verbose_name='گروه مقاله')
    title = models.CharField(max_length=200, verbose_name='عنوان مقاله')
    image_name = models.CharField(max_length=200, verbose_name='تصویر اصلی مقاله', null=True, blank=True)
    author = models.ManyToManyField(Author, verbose_name='نویسنده مقاله ها')
    short_text = models.TextField(verbose_name='متن خلاصه مقاله')
    text = models.TextField(verbose_name='متن مقاله')
    key_words = models.CharField(max_length=200, verbose_name='کلمات کلیدی')
    register_date = models.DateField(auto_now_add=True, verbose_name='تاریخ درج مقاله')
    publish_date = models.DateField(default=timezone.now, verbose_name='تاریخ انتشار مقاله')
    update_date = models.DateField(auto_now_add=True, verbose_name='تاریخ آخرین ویرایش مقاله')
    is_active = models.BooleanField(default=False, verbose_name='وضعیت')
    pdf_file_name = models.CharField(max_length=200, verbose_name='فایل pdf مقاله')
    view_number = models.PositiveSmallIntegerField(default=0 ,verbose_name='تعداد بازدید')
    slug = models.SlugField(max_length=200)
    

    def __str__(self):
       return self.title


    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'
        db_table = 't_article'
        
        
class ArticleGalery(models.Model):
    image_name = models.CharField(max_length=200, verbose_name='نام تصویر')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='گروه مقاله')
    
    def __str__(self):
        return self.image_name

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'
        db_table = 't_article_galery'