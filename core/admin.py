from django.contrib import admin
from django.utils.html import format_html
from .models import ReadingText

@admin.register(ReadingText)
class ReadingTextAdmin(admin.ModelAdmin):
    list_display = ('subject', 'date', 'english_preview', 'urdu_preview')
    search_fields = ('subject', 'english_text', 'urdu_text')

    # Short previews in list view
    def english_preview(self, obj):
        return (obj.english_text[:50] + '...') if obj.english_text else '—'
    english_preview.short_description = "English Text"

    def urdu_preview(self, obj):
        if obj.urdu_text:
            return format_html(
                '<div style="direction:rtl; font-family:\'Jameel Noori Nastaleeq\', serif; font-size:16px;">{}...</div>',
                obj.urdu_text[:50]
            )
        return '—'
    urdu_preview.short_description = "Urdu Text"

    # Custom form field styling for full editor
    class Media:
        css = {
            'all': (
                'https://fonts.googleapis.com/earlyaccess/notonastaliqurdudraft.css',
                'https://cdn.jsdelivr.net/gh/jameel-noori-fonts/jameel-noori-nastaleeq/jameel-noori-nastaleeq.css',
            )
        }
        js = ()
