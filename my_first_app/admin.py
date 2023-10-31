from django.contrib import admin
from my_first_app.models import Аpartments



@admin.register(Аpartments)
class АpartmentsAdmin(admin.ModelAdmin):
    list_display=["adress","price","name","guests","beds","photo"]
    
