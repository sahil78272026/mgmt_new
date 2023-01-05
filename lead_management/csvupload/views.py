from django.shortcuts import render, redirect
from .forms import ColumnMappingForm

def map_columns(request):
    # If this is a POST request, the user has submitted the form
    print("Before Post")
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        print("After Post")
        form = ColumnMappingForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            print("Form is valid")
            # Process the data in form.cleaned_data as needed
            csv_columns = form.cleaned_data['csv_columns']
            mapping = form.cleaned_data['mapping']
            # Save the mapped columns to the database or perform some other action with the data
            # ...

            # Redirect to a success URL
            return redirect('success_url')
    # If this is a GET request, or if the form is invalid, create a blank form
    elif request.method == 'GET':
        
        print("if request is GET")
        form = ColumnMappingForm()

    # Render the template
    print("before HTML file")
    return render(request, 'map_columns.html',{'form': form})