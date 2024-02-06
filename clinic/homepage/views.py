import os

from django.shortcuts import render

def homepage(request):
    content_directory = 'clinic/homepage/content'
    content_data = {}

    for filename in os.listdir(content_directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(content_directory, filename)
            with open(file_path, 'r') as file:
                content = file.read()
                key = os.path.splitext(filename)[0]
                content_data[key] = content

    return render(request, 'index.html', content_data)
