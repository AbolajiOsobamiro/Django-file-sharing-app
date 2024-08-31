from django.contrib import admin
from . import models

admin.site.register(models.appUpload),
admin.site.register(models.miscUpload),
admin.site.register(models.moviesUpload),
admin.site.register(models.apprequest),
admin.site.register(models.bookUpload)
admin.site.register(models.bookrequest)
admin.site.register(models.miscrequest)
admin.site.register(models.moviesrequest)


