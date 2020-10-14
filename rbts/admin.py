from django.contrib import admin

from rbts.models import BotCredentials, Target


class RedditCredentialAdmin(admin.ModelAdmin):
    fields = (
        ('user',),
        ('username', 'password',),
        ('client_id', 'client_secret')
    )

admin.site.register(BotCredentials, RedditCredentialAdmin)
admin.site.register(Target)
