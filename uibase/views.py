from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .utils import read_json_data

def returnindex(request):
    raw = read_json_data()
    kb = raw.get("data", {})          # <- only the category tree
    meta = raw.get("metadata", {})    # optional
    return render(request, "uibase/UI.html", {"kb": kb, "meta": meta})
