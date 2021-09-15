from django_admin_custom_filters.admin import CustomModelAdmin
from filter import CustomDropdownFilter, CalculatedFilter
from core.models import CalculatedData


class CalculatedDataAdmin(CustomModelAdmin):
    list_display = ('profile_id', 'site_id', 'site_id_front', 'service_code', 'percent')
    list_filter = (
        ('service_code', CustomDropdownFilter),
        CalculatedFilter,
    )

    class Meta:
        model = CalculatedData
