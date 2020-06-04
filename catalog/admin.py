from django.contrib import admin

from .models import User, Measure, UsersMeasurement

#admin.sitr.register(Measure)
#admin.site.register(User)
#admin.site.register(UsersMeasurement)

class UserAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'user_login')
    fields = ['first_name', 'last_name', ('date_of_birth', 'user_login')]

# Register the admin class with the associated model
admin.site.register(User, UserAdmin)


@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for BookInstance using the decorator
@admin.register(UsersMeasurement) 
class UsersmeasurementAdmin(admin.ModelAdmin):
    list_filter = ('status', 'date_measure')

