from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["timestamp"]
    list_filter = ["timestamp"]
    search_fields = ["comments"]

    class Meta:
        model = Feedback


admin.site.register(Feedback, FeedbackAdmin)
