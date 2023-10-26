import os
from zipfile import ZipFile

from django.conf import settings
from django.http import HttpResponse


def download_files(favorite):
    """Функция архивирования и скачивания резюме избранных кандидатов."""
    path = os.path.join(settings.MEDIA_ROOT, settings.RESUMES_UPLOAD[:-1])
    zip_file = os.path.join(path, settings.RESUMES_ARCHIVE_FILENAME)
    with ZipFile(zip_file, mode="w") as archive:
        for query in favorite:
            filename = query.candidate.resume.name
            add_file = os.path.join(path, filename.split("/")[-1])
            if os.path.isfile(add_file):
                archive.write(add_file, filename)
    response = HttpResponse(open(zip_file, "rb").read())
    response["Content-Type"] = "application/octet-stream"
    response[
        "Content-Disposition"
    ] = f'attachment; filename="{settings.RESUMES_ARCHIVE_FILENAME}"'
    return response
