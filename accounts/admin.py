from django.contrib import admin
from accounts.models import Profile,Address
from django.utils.html import format_html
admin.site.register(Address)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'gender', 'phone', 'date_of_birth','image')
    search_fields = ('name','gender')
    


    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-phone', 'user')
        return queryset

    user_info.short_description = 'Info'
    def admin_photo(self):
        return '<img src="%s" height="150"/>' % self.photo.url
    admin_photo.allow_tags = True

admin.site.register(Profile, UserProfileAdmin)




