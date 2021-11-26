from django.db import models

class Pattern(models.Model):

    class Meta:
        db_table = "pattern"

    title   = models.CharField(verbose_name="タイトル",max_length=30)
    img     = models.ImageField(verbose_name="画像",upload_to="shop/pattern/")


    def __str__(self):
        return self.title
