from django.contrib import admin
from .models import Feedback, About


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["timestamp"]
    list_filter = ["timestamp"]
    search_fields = ["comments"]

    class Meta:
        model = Feedback


admin.site.register(Feedback, FeedbackAdmin)


class AboutMeAdmin(admin.ModelAdmin):
    list_display = ["user", "content"]

    class Meta:
        model = About


admin.site.register(About, AboutMeAdmin)