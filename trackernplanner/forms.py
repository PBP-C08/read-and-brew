from django.forms import ModelForm
from trackernplanner.models import *

class BookTrackerForm(ModelForm):
    class Meta:
        model = BookTracker
        fields = ["book", "page", "progress", "status"]

class BookTrackerMemberForm(ModelForm):
    class Meta:
        model = BookTrackerMember
        fields = ["book", "page", "progress", "status"]

class BookPlannerForm(ModelForm):
    class Meta:
        model = BookPlanner
        fields = ["books", "title", "description"]