from django_admin_custom_filters.filters import CustomInputChoiceFilter, DropdownFilter


class CalculatedFilter(CustomInputChoiceFilter):
    title = "Choice Input filter"
    parameters_name = ['percent', 'site_id']
    parameters_title = ['Percent', 'Site Id\'s']


class CustomDropdownFilter(DropdownFilter):
    slice_count = 2
