from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post
from django.core import serializers
from django.http import HttpResponse
from lxml import etree as ET
import os
def post_detalle(request,isbn):
    post= get_object_or_404(Post,ISBN=isbn)

    return render(request,'blog/post/detalle.html',
                  {'post':post})

class PostListView(ListView):
    queryset= Post.libros.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/lista.html'


def listXML(request):
    queryset = Post.libros.all()
    queryset = serializers.serialize('xml',queryset)
    xsl_filename=os.getcwd()+'/blog/libros.xsl'
    rawxml=queryset.encode('utf-8')
    print (rawxml)
    parser = ET.XMLParser(ns_clean=True, recover=True, encoding='utf-8')
    rawxml = ET.fromstring(rawxml, parser=parser)
    xslt = ET.parse(xsl_filename)
    transform = ET.XSLT(xslt)
    xml = transform(rawxml)
    print(xml)
    return HttpResponse(xml, content_type="application/xml")


def rawXML(request):
    queryset = Post.libros.all()
    queryset = serializers.serialize('xml',queryset)
    return HttpResponse(queryset, content_type="application/xml")
