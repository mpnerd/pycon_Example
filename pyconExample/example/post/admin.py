from django.contrib import admin
from post.models import Category, Post, Comment
from django.contrib.admin import AdminSite

class CommentAdminSite(AdminSite):
	 site_header = 'Comment administration'

comment_admin = CommentAdminSite(name='comment admin')
comment_admin.register(Comment, CommentAdmin)

class PostAdmin(admin.ModelAdmin):
	form = MyPostAdminForm
	list_per_page = 10
	list_display = ('id', 'title', 'member','is_deleted', 'created_at', )
	list_editable = ('is_deleted', )
	list_filter = ('member__permission','category__name', 'is_deleted', )
	fields = ('member', 'category', 'title', ) 

	fieldsets = (('�⺻����', {'fields': (('member', 'category', ), )}),('����׳���', {'fields': ('title', 'subtitle', 'content',)}),('����', {'fields': ('is_deleted', 'deleted_at',)}))
	def get_urls(self):
		urls = super(PostAdmin, self).get_urls()
		post_urls = [url(r'^status/$', self.admin_site.admin_view(self.post_status_view))]
		return post_urls + urls
	def post_status_view(self, request):
		context = dict(	self.admin_site.each_context(request),	posts=Post.objects.all(),key1=value1,key2=value2,)
		return TemplateResponse(request, "admin/post_status.html", context)

admin.site.register(Post)
admin.site.register(Category) 
admin.site.register(Comment)	