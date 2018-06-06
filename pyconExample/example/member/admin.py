from django.contrib import admin
from member.models import Member



class MemberAdmin(admin.ModelAdmin):
	actions = ['set_certification_date']
	action_form = SetCertificationDateForm # SelectDateWidget 
	list_per_page = 5
	list_display = ('id', 'email','username','permission', 'is_certificated', 'certification_date', 'post_count', ) 
	list_editable = ('permission', )
	list_filter = ('permission', ) 
	search_fields = ('username', ) 
	ordering = ('-id', 'email', 'permission', ) 

	def post_count(self, obj):
		return Post.objects.filter(member=obj).count()

	post_count.short_description = '�ۼ��� �� ��'

	def set_certification_date(self, request, queryset):
		year, month, day = . . .#POSTRequest������������
		if year and month and day:
			date_str = '{0}-{1}-{2}'.format(year, month, day)
			date = strptime(date_str, "%Y-%d-%m").date()
			for member in queryset:
				Member.objects\.filter(id=member.id)\.update(is_certificated=True, certification_date=date)
			messages.success(request, '{0}����ȸ���������߽��ϴ�.'.format(len(queryset)))

		else:
			messages.error(request,'��¥�����õ����ʾҽ��ϴ�.')


admin.site.register(Member)
admin.site.register(Member, MemberAdmin)