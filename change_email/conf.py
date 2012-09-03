from django.conf import settings as django_settings

from easysettings import AppSettings


class Settings(AppSettings):
    """
Default settings for django-change-email.
"""
    EMAIL_CHANGE_DELETE_SUCCESS_REDIRECT_URL = '/account/email/change/'
    EMAIL_CHANGE_FROM_EMAIL = django_settings.DEFAULT_FROM_EMAIL
    EMAIL_CHANGE_HTML_EMAIL = False
    EMAIL_CHANGE_HTML_EMAIL_TEMPLATE = 'change_email/mail/body.html'
    EMAIL_CHANGE_SUBJECT_EMAIL_TEMPLATE = 'change_email/mail/subject.txt'
    EMAIL_CHANGE_TIMEOUT = 7
    EMAIL_CHANGE_TXT_EMAIL_TEMPLATE = 'change_email/mail/body.txt'


settings = Settings()
