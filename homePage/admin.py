from django.contrib import admin
from .models import information, socialMedia, education, experience, portofolio, blog
from django.utils.html import mark_safe
# from .forms import *
# Register your models here.


class Information(admin.ModelAdmin):
    list_display = ["__str__", "Phone",
                    "Address", "image_about", "Description"]
    

class SocialMedia(admin.ModelAdmin):
    list_display = ["__str__", "Facebook", "Instagram", "Twitter", "Linkedin"]


class Education(admin.ModelAdmin):
    list_display = ["__str__", "Specialty", "College", "YearStart", "YearEnd", "description"]


class Experience(admin.ModelAdmin):
    list_display = ["__str__", "Post", "Location","YearStart", "YearEnd"]


class Portofolio(admin.ModelAdmin):
    list_display = ["__str__", "Title",
                    "Description", "Picture", "Type", "download_project"]



    

class Blog(admin.ModelAdmin):
    # form = BlogAdminForm
    list_display = ["__str__", "Blog_thumbnail",
                    "Blog_category", "Blog_date", "Blog_content"]






admin.site.register(information, Information)

admin.site.register(socialMedia, SocialMedia)

admin.site.register(education, Education)

admin.site.register(experience, Experience)

admin.site.register(portofolio, Portofolio)

admin.site.register(blog, Blog)
