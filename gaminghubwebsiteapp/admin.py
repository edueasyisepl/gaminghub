from django.contrib import admin, sites
from gaminghubwebsiteapp.models import your_profile
from gaminghubwebsiteapp.models import otp_verify, image_mod, game_scheduler, Contact

# Register your models here.
admin.site.register(your_profile)
admin.site.register(otp_verify)
admin.site.register(image_mod)
admin.site.register(game_scheduler)
admin.site.register(Contact)
