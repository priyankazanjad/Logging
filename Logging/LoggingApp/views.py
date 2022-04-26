from django.shortcuts import render
from django.http.response import HttpResponse
import logging

logger = logging.getLogger('main')
def login_view(request):
    logger.info('Hello')
    return HttpResponse('<H1>Test<H1>')