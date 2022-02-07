from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import default


def index(request) :
     return HttpResponse('''<h1>hello</h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7&ab_channel=CodeWithHarry">Django CodeWithHarry</a>''')


def about(request):
    return HttpResponse("About Suktij")

def index(request):
    return render(request,'index.html')#it's a way to send variables to templates

def analyze(request):
    djtext= request.POST.get('text','default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    if removepunc=="on":
      punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
      analyzed=""
      for char in djtext:
        if char not in punctuations:
           analyzed=analyzed+char
      params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
      djtext=analyzed

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()

        params = {'purpose': 'Changed to Upper Case', 'analyzed_text': analyzed}
        djtext=analyzed

    if(extraspaceremover=="on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
              analyzed = analyzed + char

        params = {'purpose': 'Removed Newlines', 'analyzed_text': analyzed}
        djtext=analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed Newlines', 'analyzed_text': analyzed}

    if(removepunc!="on" and extraspaceremover!="on" and fullcaps!="on" and newlineremover!="on"):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)
