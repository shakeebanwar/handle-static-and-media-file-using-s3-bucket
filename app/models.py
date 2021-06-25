from django.db import models
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
import qrcode
# Create your models here.
class Super_AdminAccount(models.Model):

   
    name=models.CharField(max_length=255, default="First Name")
    qr_code= models.ImageField(upload_to='SuperAdmin/',default="SuperAdmin/dummy.jpg")
    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas = Image.new('RGB', (300, 300), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)