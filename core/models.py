from django.db import models

class Goal(models.Model):
    title = models.CharField("Title", max_length=200)
    description = models.TextField("Description", blank=True)
    image = models.ImageField("Icon", upload_to="static/img/", blank=True, null=True)

    class Meta:
        verbose_name = "Goals"
        verbose_name_plural = "Goals"

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="static/img/", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class SiteSettings(models.Model):
    # Hero section
    hero_title = models.CharField("Hero Title", max_length=250, blank=True)
    hero_background = models.ImageField(
        "Hero Background", upload_to="static/img/", blank=True, null=True
    )

    # About section
    about_text = models.TextField("About text", blank=True)

    # Contact info
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=250, blank=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Site Settings"
