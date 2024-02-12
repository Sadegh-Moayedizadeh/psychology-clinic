import os

from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from clinic.apps.homepage.forms import ContentForm


def homepage(request):
    content_directory = "src/clinic/apps/homepage/content"
    content_data = {}

    for filename in os.listdir(content_directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(content_directory, filename)
            with open(file_path, "r") as file:
                content = file.read()
                key = os.path.splitext(filename)[0]
                content_data[key] = content

    return render(request, "index.html", content_data)


def edit_content(request, title):
    content_directory = "src/clinic/apps/homepage/content"
    if (title + ".txt") not in os.listdir(content_directory):
        return Http404("The content with this title does not exist.")
    content_file_path = content_directory + f"/{title}.txt"

    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            with open(content_file_path, "w") as file:
                file.write(content)
            return redirect("homepage")
    else:
        with open(content_file_path, "r") as file:
            default_content = file.read()
        initial_data = {"name": title, "content": default_content}
        form = ContentForm(initial=initial_data)

    return render(request, "edit.html", {"form": form})


def get_edit_list(request):
    current_url = reverse("edit_list")
    urls = []
    content_directory = "src/clinic/apps/homepage/content"
    for filename in os.listdir(content_directory):
        filename_whithout_extension = os.path.splitext(filename)[0]
        urls.append(
            (
                request.build_absolute_uri("/")
                + current_url
                + filename_whithout_extension,
                filename_whithout_extension,
            )
        )
    return render(request, "edit_list.html", {"urls": urls})
