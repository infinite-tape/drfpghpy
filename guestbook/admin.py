from django.contrib import admin
from guestbook.models import GuestBook, GuestBookEntry


class GuestBookEntryAdmin(admin.ModelAdmin):
    pass
admin.site.register(GuestBookEntry, GuestBookEntryAdmin)


class EntryInline(admin.TabularInline):
    model = GuestBookEntry
    extra = 1


class GuestBookAdmin(admin.ModelAdmin):
    inlines = [EntryInline]
admin.site.register(GuestBook, GuestBookAdmin)
