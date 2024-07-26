from django.core import checks
from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class OrderField(models.PositiveIntegerField):

    def __init__(self, unique_for_field=None, *args, **kwargs):
        self.unique_for_field = unique_for_field
        super().__init__(*args, **kwargs)

    def check(self, **kwargs):
        return [*super().check(**kwargs), *self._check_for_field_attribute(**kwargs)]

    def _check_for_field_attribute(self, **kwargs):
        if self.unique_for_field is None:
            return [
                checks.Error(" OrderField must define a 'unique for field' attribute ")
            ]
        elif self.unique_for_field not in [
            field.name for field in self.model._meta.get_fields()
        ]:
            return [
                checks.Error(
                    f"The entered OrderField({self.unique_for_field}) doesn't match an existing model field "
                )
            ]
        return []

    def pre_save(self, model_instance, add):

        if getattr(model_instance, self.attname) is None:

            query_set = self.model.objects.all()
            try:
                filter = {
                    self.unique_for_field: getattr(
                        model_instance, self.unique_for_field
                    )
                }
                query_set = query_set.filter(**filter)
                value = query_set.latest(self.attname).order + 1
            except ObjectDoesNotExist:
                value = 1
            return value
        return super().pre_save(model_instance, add)
