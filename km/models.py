from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from django.db.models.signals import pre_save


class Province(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    zip_prefix = models.CharField(max_length=2)

    def __str__(self):
        return '%s - %s' % (self.zip_prefix, self.name)

    def get_locations(self):
        return Location.objects.filter(province=self)

    def get_locations_list(self):
        return ', '.join([l.name for l in
                          Location.objects.filter(province=self)])


class Location(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    zip_code = models.CharField(max_length=5, blank=False, null=False)
    province = models.ForeignKey(Province)


@receiver(pre_save, sender=Location)
def find_province_from_zip(sender, instance, *args, **kwargs):
    province_prefix = instance.zip_code[:2]

    try:
        province = Province.objects.get(zip_prefix=province_prefix)
    except ObjectDoesNotExist:
        name = 'Province with prefix {}xxx'.format(province_prefix)
        province = Province(name=name, zip_prefix=province_prefix)
        province.save()

    instance.province = province
