# I have created this file #Ankit
from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     return HttpResponse('<h1>Hello Ankit<h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Code with Harry </a>')
#
# def about(request):
#     return HttpResponse("About Ankit bhai")

# def index(request):
#     return render(request, "index.html") #render takes first argument as request and 2nd as template name
#     #return HttpResponse('<h1>Home</h1>')
#
# def removepunc(request):
#     #get the text
#     djtext=request.GET.get('text', 'default')#It use to give value of text or default if nothing is there in text area of html
#     print(djtext)
#     # Analyze the text
#     return HttpResponse("Removepunc <a href='/'>Back</a>")
#
# def capfirst(request):
#     return HttpResponse("capfirst  <a href='/'>Back</a>")
#
# def newlineremove(request):
#     return HttpResponse("newlineremove <a href='/'>Back</a>")
#
# def spaceremove(request):
#     return HttpResponse("spaceremove <a href='/'>Back</a>")
#
# def charcount(request):
#     return HttpResponse("charcount <a href='/'>Back</a>")

def index(request):
    return render(request, "index.html")  # render takes first argument as request and 2nd as template name
    # return HttpResponse('<h1>Home</h1>')


def analyze(request):
    # get the text
    djtext = request.POST.get('text',
                             'default')  # It use to give value of text or default if nothing is there in text area
    # of html

    # Check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraSpaceRemove = request.POST.get('spaceRemove', 'off')

    # Check which checkbox is on
    if removepunc == 'on':
        punctuation = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        param = {'purpose': 'Remove punctuation', 'Analyze_text': analyzed}
        djtext=analyzed
        #return render(request, "analyze.html", param)
    if(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed = analyzed+char.upper()
        param = {'purpose': 'Change to upper case', 'Analyze_text': analyzed}
        djtext = analyzed
        #return render(request, "analyze.html", param)

    if(newlineremove=='on'):
        analyzed = ""
        for char in djtext:
            if char !='\n' and char !='\r':
                analyzed = analyzed + char
        param = {'purpose': 'New Line Remover', 'Analyze_text': analyzed}
        djtext = analyzed
        #return render(request, "analyze.html", param)
    if(extraSpaceRemove=='on'):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==' ' and djtext[index+1]==' '):
                analyzed=analyzed+char
        param= {'purpose': 'New Line Remover', 'Analyze_text': analyzed}
        #return render(request, "analyze.html", param)
    if (removepunc != 'on' and fullcaps!='on' and newlineremove!='on' and extraSpaceRemove!='on'):
        return HttpResponse("Error")

    return render(request, "analyze.html", param)


