# from django.db import models
#
#
# # Create your models here.
#
#
# class Languagee(models.Model):
#     name = models.CharField(max_length=20)
#     code = models.CharField(max_length=5)
#     status = models.BooleanField()
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name
#
#
# llist = Languagee.objects.filter(status=True)
# list1 = []
# for rs in llist:
#     list.append((rs.code, rs.name))
# langlist = (list1)
#
#
# class Setting(models.Model):
#     STATUS = (
#         ('True', 'True'),
#         ('False', 'False'),
#     )
#     title = models
#
#
# class Settinglang(models.Model):
#     setting = models.ForeignKey(Setting, on_delete=models.CASCADE)
#     lang = models.CharField(max_length=6,choices=langlist)
#     title = models.CharField(max_length=150)
#     Keywords = models.CharField(max_length=255)
#     descripition = models.CharField(max_length=255)
#     # about = =RichTextUploadingField