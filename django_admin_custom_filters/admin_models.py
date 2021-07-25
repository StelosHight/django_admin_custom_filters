from django.contrib import admin
from filters import CustomInputChoiceFilter

class CustomModelAdmin(admin.ModelAdmin):

    def lookup_allowed(self, key, value):
        for item in self.list_filter:
            if isinstance(item, (list, tuple, dict)):
                continue
            if issubclass(item, CustomInputChoiceFilter):
                if key in item.lookup_parameters + item.parameters_name:
                    return True
        return super(CustomModelAdmin, self).lookup_allowed(key, value)