from django.contrib import admin
from .models import Board
from .models import Topic
from .models import Post
from .models import Trial


class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class TopicAdmin(admin.ModelAdmin):
    list_display = ('subject', 'board', 'starter', 'views', 'last_updated')
    list_filter = ('last_updated',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('topic', 'message', 'created_by', 'updated_at')


def set_trial_to_enrolled(request, queryset):
    queryset.update(enrolled=True)


class TrialAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'enrolled')
    list_filter = ('enrolled',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    actions = {'set_trial_to_enrolled', 'set_trial_to_not_enrolled', }
    fields = (('name', 'slug'), 'type', 'enrolled')

    def set_trial_to_enrolled(self, request, queryset):
        count = queryset.update(enrolled=True)
        self.message_user(request, '{} updates is done '.format(count))

    def set_trial_to_not_enrolled(self, request, queryset):
        count = queryset.update(enrolled=False)
        self.message_user(request, '{} trials are now not enrolled'.format(count))

    set_trial_to_enrolled.short_description = 'set the enrolled to true'
    set_trial_to_not_enrolled.short_description = 'set the enrolled to false'

    # def get_ordering(self, request):
    #     if request.user.is_superuser:
    #         return ('name', 'type')
    #     return ('title', )


admin.site.register(Board, BoardAdmin)

admin.site.register(Topic, TopicAdmin)

admin.site.register(Post, PostAdmin)

admin.site.register(Trial, TrialAdmin)
