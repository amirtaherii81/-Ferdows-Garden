from django.db import models
from django.utils import timezone



# Create your models here.
class WorkshopStatus(models.Model):
    status_code = models.IntegerField(primary_key=True, verbose_name='کد وضعیت')
    status_title = models.CharField(max_length=200, verbose_name='عنوان وضعیت')

    def __str__(self):
        return self.status_title

    class Meta:
        verbose_name = 'وضعیت'
        verbose_name_plural = 'وضعیت ها'
        db_table = 't_workshopstatus'
#----------------------------------------------------------------

def upload_workshop_image(instance, filename):
    return f'images/workshop/{filename}'

class Workshop(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    image_name = models.ImageField(upload_to=upload_workshop_image , verbose_name='تصویر اصلی')
    date_time = models.DateTimeField(verbose_name='تاریخ و زمان برگزاری')
    place = models.CharField(max_length=200, verbose_name='مکان برگزاری')
    teacher = models.CharField(max_length=100, verbose_name='مدرس')
    information = models.TextField(verbose_name='اطلاعات')
    registration = models.TextField(verbose_name='شرایط ثبت نام')
    report_text = models.TextField(null=True, blank=True, verbose_name='متن گزارش')
    view_number = models.IntegerField(default=0, verbose_name='تعداد بازدید')
    register_date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ثبت')
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    status = models.ForeignKey(WorkshopStatus, on_delete=models.CASCADE, verbose_name='وضعیت کارگاه')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'کارگاه'
        verbose_name_plural = 'کارگاه ها'
        db_table = 't_workshop'
        
#---------------------------------------------------------- 
def upload_gallery_image(instance, filename):
    return f"images/workshop/reports/{instance.workshop.id}/{filename}"
        
class WorkshopGallery(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, verbose_name='کارگاه ها')
    image = models.ImageField(upload_to=upload_gallery_image, verbose_name='تصویر')

    def __str__(self):
        return f"{self.workshop}"

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'
        db_table = 't_workshopgallery'
    