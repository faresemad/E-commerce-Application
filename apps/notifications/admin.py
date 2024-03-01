from django.contrib import admin

from apps.notifications.models import BroadcastNotification


@admin.register(BroadcastNotification)
class BroadcastNotificationAdmin(admin.ModelAdmin):
    list_display = ("message", "sent", "created_at")
    list_filter = ("sent", "created_at")
    search_fields = ("message",)
    readonly_fields = ("created_at",)
    fieldsets = (
        (None, {"fields": ("message", "sent")}),
        ("Date Information", {"fields": ("created_at",), "classes": ("collapse",)}),
    )
    ordering = ("-created_at",)
    actions = ["mark_as_sent"]

    @admin.action(description="Mark selected notifications as sent")
    def mark_as_sent(self, request, queryset):
        queryset.update(sent=True)
