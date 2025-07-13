#i created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def about(request):
    return HttpResponse("About Hasheem")
def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    capfirst=request.POST.get('caps','off')
    newlrem=request.POST.get('newlinerem','off')
    extrasp=request.POST.get('extrasp','off')
    params={'purpose':'','analyzed_text':''}
    if removepunc=="on":
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params['purpose']+='Removed Punctuations! '
        params['analyzed_text']=analyzed
        djtext=analyzed
    if capfirst=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        
        params['purpose']+='Capitalized! '
        params['analyzed_text']=analyzed
        djtext=analyzed
    if newlrem=="on":
        analyzed=""
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed=analyzed+char
        params['purpose']+='Newline Removed! '
        params['analyzed_text']=analyzed
        djtext=analyzed
    if extrasp=="on":
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params['purpose']+='Extra Space Removed! '
        params['analyzed_text']=analyzed
        djtext=analyzed
    if removepunc!="on" and capfirst!="on" and newlrem!="on" and extrasp!="on":
        return HttpResponse("Error!")
    return render(request,'analyze.html',params)
def capfirst(request):
    return HttpResponse("Capitalize")
def newlinerem(request):
    return HttpResponse("Newline remove")
def spacerem(request):
    return HttpResponse("Space remove <a href='/'>back</a>")
def charcount(request):
    return HttpResponse("Character Count")
