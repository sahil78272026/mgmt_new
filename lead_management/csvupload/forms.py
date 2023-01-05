from django import forms

class ColumnMappingForm(forms.Form):
    # MultipleChoiceField to display a list of columns in the CSV file
    csv_columns = forms.MultipleChoiceField(choices=[])

    # SelectMultipleField to allow the user to select the corresponding field in your application for each column
    mapping = forms.SelectMultiple(choices=[
        ('name', 'Name'),
        ('email', 'Email'),
        ('status', 'Status'),
    ])