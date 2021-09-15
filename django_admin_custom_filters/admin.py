from django.contrib import admin
from inspect import isclass
from .filters import CustomInputChoiceFilter


__all__ = ('CustomModelAdmin', )


class CustomModelAdmin(admin.ModelAdmin):

    def lookup_allowed(self, key, value):
        for item in self.list_filter:
            if isclass(item):
                if issubclass(item, CustomInputChoiceFilter):
                    if key in item.lookup_parameters + item.parameters_name:
                        return True

        return super(CustomModelAdmin, self).lookup_allowed(key, value)
