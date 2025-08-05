from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UserProfile, Skill, RoadmapStep, Schedule, Task, Quote, Video

admin.site.register(UserProfile)
admin.site.register(Skill)
admin.site.register(RoadmapStep)
admin.site.register(Schedule)
admin.site.register(Task)
admin.site.register(Quote)
admin.site.register(Video)
