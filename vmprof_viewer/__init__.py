from __future__ import print_function
import sys
import os
import json
import hashlib
import webbrowser

from django.core import management
from django.conf import settings
from django.conf.urls import url
from django import http
from django.contrib.staticfiles import views as static

import vmprof


def get_profile_data(fobj, program_argv=""):
    stats = vmprof.read_profile(fobj)
    data = {
        'VM': stats.interp,
        'profiles': stats.get_tree()._serialize(),
        'argv': program_argv,
        'version': 1,
    }
    return {
        'data': data,
        'checksum': hashlib.md5(json.dumps(data).encode('ascii')).hexdigest(),
        'vm': data['VM'],
        'name': data['argv']
    }


def configure(base_dir, urlpatterns):
    settings.configure(
        DEBUG=True,
        ROOT_URLCONF=urlpatterns,
        INSTALLED_APPS=['django.contrib.staticfiles'],
        STATIC_URL="/static/",
        STATICFILES_DIRS=[
            os.path.join(base_dir, "vmprof_viewer/vmprof-server/server/static"),
            os.path.join(base_dir, "vmprof_viewer/static/"),
        ],
        MIDDLEWARE_CLASSES=[],
    )


def main():
    if len(sys.argv) != 2:
        print("Usage: %s FILE" % sys.argv[0], file=sys.stderr)
        exit(1)

    profile_file = sys.argv[1]
    profile_data = get_profile_data(profile_file, profile_file)

    urlpatterns = (
        url(r"^$",
            static.serve, {'path': "standalone.html", 'insecure': True}),
        url(r"^api/log/[a-z0-9]+/",
            lambda request: http.JsonResponse(profile_data))
    )
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    sys.path.append(base_dir)
    configure(base_dir, urlpatterns)

    host, port = "localhost", 8000
    webbrowser.open("http://%s:%d/#/%s" % (host, port, profile_data['checksum']))
    django_cmd = ["runserver", "--noreload", "%s:%d" % (host, port)]
    management.ManagementUtility([sys.argv[0]] + django_cmd).execute()
