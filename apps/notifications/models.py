from django.db import models


class BroadcastNotification(models.Model):
    message = models.CharField(max_length=255)
    sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = "Broadcast Notification"
        verbose_name_plural = "Broadcast Notifications"
        ordering = ("-created_at",)
