import base64
import os

from django.db import models
from localflavor.us.models import PhoneNumberField
from PIL import Image
import imghdr
import StringIO
from django.core.files.base import ContentFile

DONOR_LEVELS = (
    ("P", "Platinum ($1000)"),
    ("G", "Gold ($500)"),
    ("S", "Silver ($250)"),
    ("B", "Bronze ($100)"),
    ("I", "Individual ($50)"),
    ("O", "Other")
)

DONATION_TYPES = (
#    ("B", "Bank Account"),
    ("C", "Credit Card"),
    ("P", "PayPal"),
    ("G", "Pledge"),
)

class Donor(models.Model):
    """
    Model for Donors to DCPYthon.
    """
    email = models.EmailField()
    phone = PhoneNumberField(blank=True, null=True)
    name = models.CharField(max_length=100, help_text="If institutional donation, point of contact's name")

    public_name = models.CharField(max_length=100, verbose_name="Display Name", blank=True, null=True)
    public_url = models.URLField(blank=True, null=True, verbose_name="Display Url")
    public_slogan = models.CharField(max_length=200, verbose_name="Display Slogan", blank=True, null=True)
    public_logo = models.ImageField(upload_to="donor_logos", verbose_name="Display Logo", blank=True, null=True)


    level = models.CharField(max_length=1, choices=DONOR_LEVELS, blank=True, null=True)
    secret = models.CharField(max_length=90)
    reviewed = models.BooleanField(default=False)
    valid_until = models.DateField(blank=True, null=True)

    def save (self, *args, **kwargs):
        # ensure there is a secret
        if not self.secret:
            self.secret = base64.urlsafe_b64encode(os.urandom(64))
        # ensure the image is in a valid format
        image = self.public_logo.file
        if self.public_logo:
            valid_image = self.process_image(image)
            if valid_image != image:
                self.public_logo.save("{}.png".format(self.pk), valid_image, save=False)
        # if self.public_logo:
        #     self.public_logo = self.process_image(self.public_logo.file)
        super(Donor, self).save(*args, **kwargs)

    def process_image(self, f):
        """
        return a file object with the image contained in the f that is:
            a png, gif or jpeg
            no more than 800x450
            no less than 16:9 ratio
        """
        image = Image.open(f)
        width, height = image.size

        if height <= 450 and imghdr.what(f) in ['png', 'gif', 'jpeg'] and 1.0*width/height >= 16.0/9:
            return f

        # ensure no more than 450x800
        if height > 450:
            image.thumbnail((450, 800), Image.ANTIALIAS)
            width, height = image.size

        # ensure no more than 16:9 aspect ratio
        if 1.0*width/height < 16.0/9:
            new_width = height*16/9
            new_image = Image.new('RGBA', (new_width, height))
            x = (new_width - width)/2
            y = 0
            new_image.paste(image, (x, y, x + width, y + height))
            image = new_image

        # generate a png
        string_file = StringIO.StringIO()
        new_image.save(string_file, "PNG")
        string_file.seek(0)
        f = ContentFile(string_file.read())
        return f

    def pending(self):
        return not self.reviewed or self.donations.filter(reviewed=False).count()

    def __unicode__(self):
        if self.public_name:
            return u"{} (contact: {}, {})".format(self.public_name, self.name, self.email)
        else:
            return u"{} ({})".format(self.name, self.email)

class Donation(models.Model):
    """
    Model representing one donation
    """
    donor = models.ForeignKey(Donor, related_name='donations')
    datetime = models.DateTimeField()
    type = models.CharField(max_length=1, choices=DONATION_TYPES)
    completed = models.BooleanField(default=False)
    donation = models.DecimalField(decimal_places=2, max_digits=10)
    transaction_id = models.CharField(max_length=50)

    valid_until = models.DateField(blank=True, null=True)
    level = models.CharField(max_length=1, choices=DONOR_LEVELS, blank=True, null=True)
    reviewed = models.BooleanField(default=False)

    def __unicode__(self):
        return u"${} donation from {} on {}".format(self.donation, self.donor.public_name or self.donor.name, self.datetime)
