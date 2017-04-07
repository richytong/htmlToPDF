from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import Template, Context
from django.db.models import Q
from django.db.models import Count
from django.db import connections
from django.template.loader import get_template
from django.template import RequestContext
from django.conf import settings
from collections import defaultdict
from weasyprint import HTML
import json

def index(request):
    render_data = {}
    html_template = get_template('rich/cv.html')
    # html_template = get_template('rich/onfleet-coverletter.html')
    output_html = html_template.render(RequestContext(request,render_data)).encode(encoding="UTF-8")
    pdf_file = HTML(string=output_html, base_url=request.build_absolute_uri()).write_pdf()
    http_response = HttpResponse(pdf_file, content_type='application/pdf')
    http_response['Content-Disposition'] = 'filename="stage_source_export.pdf"'
    return http_response