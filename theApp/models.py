from django.db import models
from django.db.models import Count


class appUpload(models.Model):
    title=models.CharField(max_length=1000)
    image=models.ImageField(null=True, blank=True, upload_to='coverImages/Apps/')
    file= models.FileField(upload_to='actualFiles/Apps/')


    def __str__(self):
        return self.title
    
    # This extra function is to prevent the duplication of uploads of a particular 
    # item in a category. It first converts the title of each upload to lowercase,
    # then it calls the save() function only if this title does not belong to a list 
    # of already uploaded file titles (aupNames). Also, if aupNames is empty, it means 
    # that is the first upload, and the save() method is called directly.

    def save(self, *args, **kwargs):
        title = self.title.lower()
        app_upp_name = appUpload.objects.annotate(Count('title'))

        aupNames = []
        for a in app_upp_name:
            b = str(a).lower()
            aupNames.append(b)

        if aupNames == []:
            super().save(*args, **kwargs)   # Call the save() method
        else:
            if title not in aupNames:
                    super().save(*args, **kwargs)   # Call the save() method


class bookUpload(models.Model):
    title=models.CharField(max_length=1000)
    image=models.ImageField(null=True, blank=True, upload_to='coverImages/Books/')
    file=models.FileField(upload_to='actualFiles/Books/')


    def __str__(self):
        return self.title
    
    # Same explanation as above
    def save(self, *args, **kwargs):
        title = self.title.lower()
        book_upp_name = bookUpload.objects.annotate(Count('title'))

        bupNames = []
        for a in book_upp_name:
            b = str(a).lower()
            bupNames.append(b)

        if bupNames == []:
            super().save(*args, **kwargs) # Call the save() method
        else:
            if title not in bupNames:
                    super().save(*args, **kwargs) # Call the save() method



class miscUpload(models.Model):
    title=models.CharField(max_length=1000)
    image=models.ImageField(null=True, blank=True, upload_to='coverImages/Others/')
    file=models.FileField(upload_to='actualFiles/Others/')

    def __str__(self):
        return self.title

    # Same explanation as above
    def save(self, *args, **kwargs):
        title = self.title.lower()
        misc_upp_name = miscUpload.objects.annotate(Count('title'))

        MupNames = []
        for a in misc_upp_name:
            b = str(a).lower()
            MupNames.append(b)

        if MupNames == []:
            super().save(*args, **kwargs) # Call the save() method
        else:
            if title not in MupNames:
                    super().save(*args, **kwargs) # Call the save() method

class moviesUpload(models.Model):
    title=models.CharField(max_length=1000)
    image=models.ImageField(null=True, blank=True, upload_to='coverImages/Videos/')
    file=models.FileField(upload_to='actualFiles/Videos/')

    def __str__(self):
        return self.title

    # Same explanation as above
    def save(self, *args, **kwargs):
        title = self.title.lower()
        movies_upp_name = moviesUpload.objects.annotate(Count('title'))

        mupNames = []
        for a in movies_upp_name:
            b = str(a).lower()
            mupNames.append(b)

        if mupNames == []:
            super().save(*args, **kwargs) # Call the save() method
        else:
            if title not in mupNames:
                    super().save(*args, **kwargs) # Call the save() method



class apprequest(models.Model):
    requestname =models.CharField(max_length=10000000000000000)


    def __str__(self):
        return self.requestname
    
    # Same explanation as above
    def save(self, *args, **kwargs):
        requestname = self.requestname.lower()
        app_req_name = apprequest.objects.annotate(Count('requestname'))

        aReqNames = []
        for a in app_req_name:
            b = str(a).lower()
            aReqNames.append(b)

        if aReqNames == []:
            super().save(*args, **kwargs) # Call the save() method
        else:
            if requestname not in aReqNames:
                    super().save(*args, **kwargs) # Call the save() method



class bookrequest(models.Model):
    requestname =models.CharField(max_length=10000000000000000)

    def __str__(self):
        return self.requestname
    
    # Same explanation as above
    def save(self, *args, **kwargs):
        requestname = self.requestname.lower()
        book_req_name = bookrequest.objects.annotate(Count('requestname'))

        bReqNames = []
        for a in book_req_name:
            b = str(a).lower()
            bReqNames.append(b)

        if bReqNames == []:
            super().save(*args, **kwargs) # Call the save() method
        else:
            if requestname not in bReqNames:
                    super().save(*args, **kwargs) # Call the save() method

class miscrequest(models.Model):
    requestname =models.CharField(max_length=10000000000000000)

    def __str__(self):
        return self.requestname
    
    # Same explanation as above
    def save(self, *args, **kwargs):
        requestname = self.requestname.lower()
        misc_req_name = miscrequest.objects.annotate(Count('requestname'))

        MReqNames = []
        for a in misc_req_name:
            b = str(a).lower()
            MReqNames.append(b)

        if MReqNames == []:
            super().save(*args, **kwargs) # Call the save() method
        else:
            if requestname not in MReqNames:
                    super().save(*args, **kwargs) # Call the save() method

class moviesrequest(models.Model):
    requestname =models.CharField(max_length=10000000000000000)

    def __str__(self):
        return self.requestname

    # Same explanation as above
    def save(self, *args, **kwargs):
        requestname = self.requestname.lower()
        movies_req_name = moviesrequest.objects.annotate(Count('requestname'))

        mReqNames = []
        for a in movies_req_name:
            b = str(a).lower()
            mReqNames.append(b)

        if mReqNames == []:
            super().save(*args, **kwargs) # Call the save() method
        else:
            if requestname not in mReqNames:
                    super().save(*args, **kwargs) # Call the save() method