# coding: utf-8

from django.dispatch import Signal


post_email_confirmation_send = Signal('confirmation')
post_email_confirmation_confirm = Signal('confirmation', 'save_to_content_object', 'old_email')
