from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Memory(models.Model):
    memory_title = models.CharField(max_length=300, verbose_name='عنوان')
    memory_text = models.TextField(verbose_name='متن')
    register_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)
    user_registered = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.memory_title
    
    class Meta:
        verbose_name = 'خاطره'
        verbose_name_plural = 'خاطرات'
        db_table = 't_memory'



def upload_galery_image(instace, filename):
    return f'images/memory/{instace.memory.memory_title}/galery/{filename}'

class MemoryGallery(models.Model):
    memory_image_name = models.ImageField(upload_to=upload_galery_image, verbose_name='تصویر خاطره')
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE, related_name='images')
    
    def __str__(self):
        return self.memory_image_name
    
    class Meta:
        verbose_name = 'تصویر خاطره'
        verbose_name_plural = 'تصاویر خاطره'
        db_table = 't_memory_galery'


class MemoryLike(models.Model):
    user_like = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table = 't_MemoryLike'