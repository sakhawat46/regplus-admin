from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify


#start Section  System Settings
class LogoSettings(models.Model):
    logo_light = models.ImageField(upload_to='app_config/', verbose_name="Logo Light")
    logo_dark = models.ImageField(upload_to='app_config/', verbose_name="Logo Dark")
    favicon = models.ImageField(upload_to='app_config/', verbose_name="Favicon")
    invoice_logo = models.ImageField(upload_to='app_config/', verbose_name="Invoice Logo")

    website_logo_width = models.PositiveIntegerField(blank=True, null=True, verbose_name="Website Logo Width (px)")
    invoice_logo_width = models.PositiveIntegerField(blank=True, null=True, verbose_name="Invoice Logo Width (px)")

    def __str__(self):
        return f"Logo Settings {self.id}"


class GeneralSettings(models.Model):
    APPLICATION_DIRECTIONS = [
        ('left', 'Left'),
        ('right', 'Right'),
    ]

    application_name = models.CharField(max_length=255, verbose_name="Application Name")
    author = models.CharField(max_length=255, verbose_name="Author")
    default_menu = models.BooleanField(default=True, help_text="Enable or disable the default menu.")
    search_feature = models.BooleanField(default=True, help_text="Enable search on the frontend.")
    whatsapp_button_direction = models.CharField(max_length=10,choices=APPLICATION_DIRECTIONS,default='right',verbose_name="Whatsapp Button Direction")
    scroll_to_top_direction = models.CharField(max_length=10,choices=APPLICATION_DIRECTIONS,default='left',verbose_name="Scroll To Top Direction")
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.application_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"General Settings: {self.application_name}"


class ColorSettings(models.Model):
    COLOR_MODES = [('light', 'Light'), ('dark', 'Dark')]

    default_color_mode = models.CharField(max_length=10, choices=COLOR_MODES, default='dark', verbose_name="Default Color Mode")
    primary_color = models.CharField(max_length=7, help_text="Hex code for the primary color (e.g., #3366FF)", verbose_name="Primary Color")
    primary_hover_link_color = models.CharField(max_length=7, help_text="Hex code for primary hover and link color", verbose_name="Primary Hover & Link Color")
    whatsapp_button_shed_color = models.CharField(max_length=7, help_text="Hex code for WhatsApp button color", verbose_name="WhatsApp Button Shed Color")

    def __str__(self): return f"Color Settings ({self.default_color_mode.title()} mode)"


class ContactSettings(models.Model):
    email = models.EmailField(verbose_name="Email")
    phone_whatsapp = models.CharField(max_length=20, verbose_name="Phone (WhatsApp)")
    price_range = models.CharField(max_length=50, verbose_name="Price Range")
    address = models.CharField(max_length=255, verbose_name="Address")
    state = models.CharField(max_length=100, verbose_name="State")
    postal = models.CharField(max_length=20, verbose_name="Postal")
    country = models.CharField(max_length=100, verbose_name="Country")

    def __str__(self): return f"Contact Settings for {self.email}"


class CurrencySettings(models.Model):
    currency_name = models.CharField( max_length=20)
    currency_symbul = models.CharField( max_length=5)
    enable_purchasing = models.BooleanField(default=True)
    enable_auto_invoicing = models.BooleanField(default=True)

    def __str__(self): return f"Currency Settings for {self.currency_name}"


class HRMSettings(models.Model):
    clock_in_max_time = models.TimeField(
        verbose_name="HRM Attendance Clock In Max Time",
        default='09:00:00'  # Add default time (9 AM)
    )
    clock_out_min_time = models.TimeField(
        verbose_name="HRM Attendance Clock Out Min Time",
        default='17:00:00'  # Add default time (5 PM)
    )

    def __str__(self):
        return "HRM Settings"


class SMSSettings(models.Model):
    twilio_sid = models.CharField(max_length=100, verbose_name="Twilio SID")
    auth_token = models.CharField(max_length=100, verbose_name="Auth Token")
    twilio_number = models.CharField(max_length=20, verbose_name="Twilio Number")

    def __str__(self): return "SMS Settings"


class SocialSettings(models.Model):
    google_analytics_code = models.CharField(max_length=100,verbose_name="Google Analytics Measurement Code",blank=True, null=True)
    facebook_pixel_code = models.TextField(verbose_name="Facebook Pixel Code",blank=True, null=True)
    facebook_chat_code = models.TextField(verbose_name="Facebook Chat Code",blank=True, null=True)
    whatsapp_button_enabled = models.BooleanField(default=False,verbose_name="WhatsApp Button")
    facebook_chat_button_enabled = models.BooleanField(default=False,verbose_name="Facebook Chat Button")

    def __str__(self): return "Social Settings"


class OtherSettings(models.Model):
    custom_css = models.TextField(verbose_name="Custom CSS", blank=True, null=True)
    custom_js = models.TextField(verbose_name="Custom JS", blank=True, null=True)

    def __str__(self): return "Other Settings"

#end Section  System Settings


#start Section  Footer Settings

class FooterLayout(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "Footer Layout Section.  "


class FooterTop(models.Model):
    subtitle = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    button_text = models.CharField(max_length=100)
    button_url = models.URLField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.subtitle} - {self.title}"


class SocialLinks(models.Model):
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    pinterest = models.URLField(blank=True, null=True)

    def __str__(self):
        return "Social Links"


class SubscribeForm(models.Model):
    title = models.CharField(max_length=150)
    placeholder = models.CharField(max_length=150)
    description = models.TextField()
    button_text = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class FooterColumn(models.Model):
    title = models.CharField(max_length=100)
    content_choice = models.CharField(max_length=100, blank=True, null=True)  # Optional dropdown value
    description = RichTextField(help_text="Use <ul> and <li> tags")

    class Meta:
        verbose_name = "Footer Column"
        verbose_name_plural = "Footer Columns"

    def __str__(self):
        return self.title


class FooterBottom(models.Model):
    small_text = models.TextField(verbose_name="Small Text (Under Logo)")

    first_column_title = models.CharField(max_length=100)
    first_column_choice = models.CharField(max_length=100)
    first_column_description = RichTextField(help_text="Use <ul> and <li> tags")

    second_column_title = models.CharField(max_length=100)
    second_column_description = RichTextField(help_text="Use <ul> and <li> tags")

    third_column_title = models.CharField(max_length=100)
    third_column_description = RichTextField(help_text="Use <ul> and <li> tags")

    def __str__(self):
        return "Footer Bottom Section"

class FooterCopyright(models.Model):
    copyright_text = models.CharField(verbose_name="Copyright Text", max_length=100)
    privacy_policy = models.CharField(verbose_name="Privacy Policy Page Title", max_length=20)
    terms_page = models.CharField(verbose_name="Terms Page Title", max_length=20)

    def __str__(self):
        return "Footer Copyright Section"

#End Section  Footer Settings


#start Section  SEO Settings

class SEOSettings(models.Model):
    meta_title = models.CharField(max_length=150, verbose_name="Meta Title")
    tag_line = models.CharField(max_length=150, verbose_name="Tag Line")
    meta_description = models.TextField(verbose_name="Meta Description")
    seo_keywords = models.TextField(verbose_name="SEO Keywords", help_text="Comma-separated keywords for SEO")
    meta_image = models.ImageField(upload_to="meta_images/", verbose_name="Meta Image", blank=True, null=True)

    class Meta:
        verbose_name = "SEO Settings"
        verbose_name_plural = "SEO Settings"

    def __str__(self):
        return self.meta_title



class PaymentMethod(models.Model):
    GATEWAY_CHOICES = [
        ('paypal', 'PayPal'),
        ('stripe', 'Stripe'),
        ('sslcommerz', 'SSLCOMMERZ'),
        ('instamojo', 'Instamojo'),
        ('paymob', 'Paymob'),
    ]


    name = models.CharField(
        max_length=50,
        choices=GATEWAY_CHOICES,
        verbose_name="Payment Gateway",
        help_text="Select the payment gateway you want to configure."
    )

    config = models.JSONField(
        default=dict,
        verbose_name="Configuration",
        help_text="Enter key-value pairs for API credentials and settings (e.g., client_id, secret_key, etc.)"
    )


    sandbox = models.BooleanField(
        default=False,
        verbose_name="Sandbox Mode",
        help_text="Enable this to use test/sandbox credentials instead of live ones."
    )

    active = models.BooleanField(
        default=False,
        verbose_name="Active",
        help_text="Enable this payment method for users."
    )

    class Meta:
        verbose_name = "Payment Method"
        verbose_name_plural = "Payment Methods"

    def __str__(self):
        return self.get_name_display()
