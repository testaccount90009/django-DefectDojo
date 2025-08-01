

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app  # noqa: F401

__version__ = "2.48.5"
__url__ = "https://github.com/DefectDojo/django-DefectDojo"
__docs__ = "https://documentation.defectdojo.com"
