Custom filters for Django Admin
-
##Information
**1. Custom choice filter**

1.1. Filter by multiple choices 
(Less and Equal, More and Equal, Equal) in each metrics / dimensions lookups

1.2. Add multiple metrics / dimensions for combined queries

1.3. You can add any name for your metrics / dimension to label

**2. Custom dropdown filter**

2.1. Filter uses default view of django list_filter in condition 
when values less than slice count (default slice count is 3)

2.2. When values in filter more than slice count view changed 
to select element.

##Install

You can install this by using `pip`:
```shell
pip install django-admin-custom-filters
```

##Usage

**1. Custom choice filter**

**1.1. Create child class by using parent class CustomInputChoiceFilter.**
```python
from django_admin_custom_filters.filters import CustomInputChoiceFilter


class ChildFilter(CustomInputChoiceFilter):
```
**1.2. Edit variables - title, parameters_title, parameters_name.**
```python
from django_admin_custom_filters.filters import CustomInputChoiceFilter


class ChildFilter(CustomInputChoiceFilter):
    title = "Test Filter"
    parameters_name = ['variable_1', 'variable_2']
    parameters_title = ['Variable First', 'Variable Second']
```
**1.3. Create child class by using parent class CustomModelAdmin.**
```python
from django_admin_custom_filters.admin import CustomModelAdmin

class TestAdmin(CustomModelAdmin):
```
**1.4. Add to list_filter your filter.**
```python
from django_admin_custom_filters.admin import CustomModelAdmin
from .filters import ChildFilter
from .models import Test


class TestAdmin(CustomModelAdmin):
    list_filter = (
        ChildFilter,
    )

    class Meta:
        model = Test
```
**2. Custom dropdown filter**

**2.1. You can create child class for change slice count.**
```python
from django_admin_custom_filters.filters import DropdownFilter


class CustomDropdownFilter(DropdownFilter):
    slice_count = 2
```
**2.2. Add to list_filter your filter.**
```python
from django.contrib import admin
from .filters import CustomDropdownFilter
from .models import Test


class TestAdmin(admin.ModelAdmin):
    list_filter = (
        ('variable_1', CustomDropdownFilter),
    )

    class Meta:
        model = Test
```
**3. Img from examples folder code**

**3.1. Custom choice filter and Custom dropdown filter**

![Image](img/image.png?raw=true)

**3.2. Custom dropdown filter by slice more than values in filter.**

![Image2](img/image 2.png?raw=true)
