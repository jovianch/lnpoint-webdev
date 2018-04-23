from django.forms.widgets import ClearableFileInput, CheckboxInput, DateInput, TimeInput
from django.utils.html import escape, conditional_escape
from django.utils.safestring import mark_safe
  

class BootstrapDateWidget(DateInput):
    """
    A Widget that overrides the default date widget and styles it with Bootstrap
    """
  
    def __init__(self, attrs=None, format=None):
        super(BootstrapDateWidget, self).__init__(attrs, format)
  
    def render(self, name, value, attrs=None):
        """Override the output rendering to return a widget with some Bootstrap niceness"""
  
        # Set a placeholder attribute
        attrs['placeholder'] = 'dd/mm/yyyy'
  
        # Add a class attribute so that we can generically javascript things
        if 'class' in attrs:
            attrs['class'] = attrs['class'] + " datepicker"
        else:
            attrs['class'] = 'datepicker'
  
        widget = DateInput.render(self, name, value, attrs)
  
        return mark_safe(u'<div class="input-append datepicker">' + widget + '<span class="add-on"><i class="icon-calendar"></i></span></div>')

class BootstrapTimeWidget(TimeInput):
    """
    A Widget that overrides the default time widget and styles it with Bootstrap
    """
  
    def __init__(self, attrs=None, format=None):
        super(BootstrapTimeWidget, self).__init__(attrs, format)
  
    def render(self, name, value, attrs=None):
        """Override the output rendering to return a widget with some Bootstrap niceness"""
  
        # Set a placeholder attribute
        attrs['placeholder'] = '00:00'
  
        widget = TimeInput.render(self, name, value, attrs)
  
        return mark_safe(u'<div class="input-append">' + widget + '<span class="add-on"><i class="icon-time"></i></span></div>')