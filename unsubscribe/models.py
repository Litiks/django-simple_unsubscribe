import uuid

from django.db import models
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.conf import settings
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string

def generate_token():
    return uuid.uuid4().hex

class UnsubscribeDetail(models.Model):
    email = models.EmailField(primary_key=True)
    token = models.CharField(max_length=50, default=generate_token)
    unsub_date = models.DateField(null=True, blank=True, help_text="If set, they will not receive emails")

    def __unicode__(self):
        return self.email

    def unsubscribe_url(self):
        domain = Site.objects.get_current().domain
        return "http://%s%s" % (domain, reverse('unsubscribe', args=[self.token]))

    def resubscribe_url(self):
        domain = Site.objects.get_current().domain
        return "http://%s%s" % (domain, reverse('resubscribe', args=[self.token]))

# Some automatic cleanup. This isn't super necessary, but it's helpful if we delete a user to delete our memory of them as well. This falls in the category if expected behaviour.
def delete_unsubscribe_detail(sender, instance, **kwargs):
    if instance:
        #fetch any details for this email address
        details = UnsubscribeDetail.objects.filter(email__in=[instance.username, instance.email])
        details.delete()
                
models.signals.pre_delete.connect(delete_unsubscribe_detail, sender=User)

# monkey patch the email sending logic to consider and append unsubscription logic
def patch_send_email():
    EmailMessage.send_orig = EmailMessage.send
    def new_send(self, *args, **kwargs):
        if not getattr(self, 'bypass_unsub'):
            # todo: we should fix this to handle multiple recipients.
            if self.to:
                to = self.to[0]
            else:
                to = ''

            site = Site.objects.get_current()

            #check if recipient is already unsubscribed
            detail, created = UnsubscribeDetail.objects.get_or_create(email=to)
            if detail.unsub_date:
                #they're unsubscribed, don't send
                self.to = []    #this will not fail the send function. see https://docs.djangoproject.com/en/dev/topics/email/

            signature = render_to_string('unsubscribe/email/signature.txt', {'site':site}).strip()
            self.body += "\n\n\n%s\n\nTo unsubscribe, click the following link:\n%s" % (signature, detail.unsubscribe_url())
            self.extra_headers['List-Unsubscribe'] = "<%s>" % detail.unsubscribe_url()

            #look for an html body
            if hasattr(self, 'alternatives'):
                for i, alt in enumerate(self.alternatives):
                    content, mimetype = alt
                    if 'html' in mimetype:
                        signature = render_to_string('unsubscribe/email/signature.html', {'site':site})
                        content += "<br><br><br>%s<br><br><a href='%s'>unsubscribe</a> to stop receiving emails from %s" % (signature, detail.unsubscribe_url(), site.name)
                        self.alternatives[i] = (content, mimetype)

        return self.send_orig(*args, **kwargs)

    EmailMessage.send = new_send

patch_send_email()
