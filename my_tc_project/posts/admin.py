from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "timeToRead"]
	list_filter = ["timestamp", "timeToRead"]
	search_fields = ["title", 'timeToRead']
	class Meta:
		model = Post 

admin.site.register(Post, PostAdmin) 