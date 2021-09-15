from urllib.parse import urlparse
from django.contrib.admin.filters import AllValuesFieldListFilter
from django.contrib.admin import ModelAdmin, SimpleListFilter, ListFilter
from django.utils.translation import gettext_lazy as _
from decimal import Decimal


__all__ = ('CustomInputChoiceFilter', 'DropdownFilter')


class CustomInputChoiceFilter(ListFilter):
    parameters_name = []
    parameters_title = []
    lookup_parameters = []
    validation_error = []
    template = 'filters/input_filter.html'

    def __init__(self, request, params, model, model_admin):
        super().__init__(request, params, model, model_admin)

        self.lookup_parameters = [f"filter_{parameter_name}" for parameter_name in self.parameters_name]

        for parameter_name in (self.parameters_name + self.lookup_parameters):
            if parameter_name in params:
                value = params.pop(parameter_name)
                self.used_parameters[parameter_name] = value

        lookup_choices = self.lookups(request, model_admin)

        if lookup_choices is None:
            lookup_choices = ()

        self.lookup_choices = list(lookup_choices)

    def has_output(self):
        return len(self.lookup_choices) > 0

    def value(self, parameter_name):
        if parameter_name in self.parameters_name + self.lookup_parameters:
            return self.used_parameters.get(parameter_name)
        else:
            return None

    def lookups(self, request, model_admin):
        return [
            ("lte", "Less and Equal"),
            ("gte", "More and Equal"),
            ("eq", "Equal"),
        ]

    def expected_parameters(self):
        return [self.parameters_name]

    def choices(self, changelist):
        for lookup, title in self.lookup_choices:
            for index, parameter_name in enumerate(self.lookup_parameters):
                yield {
                    'selected': self.value(parameter_name) == str(lookup),
                    'query_string': changelist.get_query_string({parameter_name: lookup}),
                    'display': title,
                    'name': parameter_name,
                    'value': lookup,
                    'filter_for': self.parameters_title[index]
                }

    def queryset(self, request, queryset):
        self.validation_error.clear()
        params = {}
        for param in self.used_parameters:
            if 'filter' not in param and self.used_parameters[param]:
                try:
                    value = Decimal(self.value(param))
                    if f'filter_{param}' in self.used_parameters and self.value(f'filter_{param}') in ["lte", "gte"]:
                        params[f"{param}__{self.value(f'filter_{param}')}"] = value
                    else:
                        params[param] = value
                except:
                    self.validation_error.append(param)
        if params:
            return queryset.filter(**params)
        return queryset


class DropdownFilter(AllValuesFieldListFilter):
    slice_count = 3
    template = 'filters/dropdown_filter.html'

    def slice_str(self):
        return f"{self.slice_count}:"
