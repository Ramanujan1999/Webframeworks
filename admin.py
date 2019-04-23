from django.contrib import admin
from .models import Registration,LeaveApplication,Complaint

admin.site.register(Registration)
admin.site.register(LeaveApplication)
admin.site.register(Complaint)
