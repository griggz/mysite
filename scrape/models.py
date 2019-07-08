from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils import timezone


class ScrapeManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(ScrapeManager, self).filter(draft=False).filter(
            scrape_date__lte=timezone.now())


class Yelp(models.Model):
    business_name = models.CharField(max_length=120, blank=True, null=True)
    link = models.CharField(max_length=120)
    scrape_date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    objects = ScrapeManager()

    def get_absolute_url(self):
        return reverse('scrape:results', kwargs={'slug': self.slug})


class Results(models.Model):
    yelp_id = models.ForeignKey(Yelp, on_delete=models.CASCADE, null=True)
    author = models.CharField(max_length=120, blank=True, null=True)
    date = models.CharField(max_length=120, blank=True)
    rating = models.CharField(max_length=120, blank=True, null=True)
    review = models.TextField(max_length=500, blank=True)

    def get_absolute_url(self):
        return reverse('scrape:results', kwargs={'pk': self.pk})


def create_slug(instance, new_slug=None):
    link = instance.link.rsplit('biz/', 1)
    if '?' in link[1]:
        slug = slugify(link[1].split('?')[0])
    else:
        slug = slugify(link[1])

    if new_slug is not None:
        slug = new_slug
    qs = Yelp.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_scrape_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_scrape_receiver, sender=Yelp)
