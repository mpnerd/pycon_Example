class MyPostAdminForm(forms.ModelForm):
	def clean_content(self): # clean_{field_name}	
	content = self.cleaned_data['content'] 
	words = ['�ɽ��ϴ�','������', '������', ]
	error_message = '[{0}] {1}'.format(', '.join(words),'�͡�')
	if any(word in content for word in words):
		raise forms.ValidationError(error_message) 	return content