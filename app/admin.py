from django.contrib import admin
from .models import Product,category,tag,gameplayimages,youtubevideo,mygames

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','name')

class categoryAdmin(admin.ModelAdmin):
    list_display=('id','name')

class tagAdmin(admin.ModelAdmin):
    list_display=('id','name')

class gameplayimagesAdmin(admin.ModelAdmin):
    list_display=('id','Prod')

class youtubevideoAdmin(admin.ModelAdmin):
    list_display=('id','Prod')

class mygamesAdmin(admin.ModelAdmin):
    list_display=('id','product')


#Register your models here
admin.site.register(Product,ProductAdmin)
admin.site.register(category,categoryAdmin)
admin.site.register(tag,tagAdmin)
admin.site.register(gameplayimages,gameplayimagesAdmin)
admin.site.register(youtubevideo,youtubevideoAdmin)
admin.site.register(mygames,mygamesAdmin)


##Create Admin templates for the models
#class GenreAdmin(admin.ModelAdmin):
#    list_display=('id','name')

#class MovieAdmin(admin.ModelAdmin):
#    list_display_links=('id','title')
#    list_display=('id','title','release_year','price','in_stock')
#    #exclude=('in_stock','price')# exclude columns you dont want to modify
#    #fields=('title','genre','in_4k')


## Register your models here.
#admin.site.register(Genre,GenreAdmin)
#admin.site.register(Movie,MovieAdmin)

