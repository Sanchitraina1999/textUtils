from django.http import HttpResponse
from django.shortcuts import render
import string

def home(request):
    return render(request,'index.html')

def analyzer(request):
    text = request.POST.get('text','')

    removePunc = request.POST.get('removePunc','off')
    ALLCAPS = request.POST.get('ALLCAPS','off')
    RNLC = request.POST.get('RNLC','off')
    capfirst = request.POST.get('capfirst','off')
    ESR = request.POST.get('ESR','off')
    CC = request.POST.get('CC','off')

    analyzed = ''

    if(removePunc == 'on'):
        punctuations = string.punctuation
        for characters in text:
            if characters not in punctuations:
                analyzed += characters
        params = {'purpose':'Removed Punctuations','analyzed_text': analyzed }
        text = analyzed

    if(ALLCAPS =='on'):
        analyzed = ''
        for characters in text:
            characters = characters.upper()
            analyzed += characters
        params = {'purpose':'CAPTILIZED all words','analyzed_text': analyzed }
        text = analyzed
        
    if(capfirst =='on'):
        analyzed = text.capitalize()
        params = {'purpose':'CAPTILIZED first character','analyzed_text': analyzed }
        text = analyzed
        
    if(RNLC =='on'):
        analyzed = ''
        for characters in text:
            if characters != '\n' and characters != '\r':
                analyzed += characters
        params = {'purpose':'New line characters removed','analyzed_text': analyzed }
        text = analyzed

    if(capfirst =='on'):
        analyzed = text.capitalize()
        params = {'purpose':'CAPTILIZED first character','analyzed_text': analyzed }

    if(ESR =='on'):
        analyzed = ''
        for index, characters in enumerate(text):
            if not(text[index] == " " and text[index+1]== " "):
                analyzed += characters
        params = {'purpose':'Extra Spaces removed','analyzed_text': analyzed }
        text = analyzed
        
    if(CC =='on'):
        count=0
        for characters in enumerate(text):
            count += 1
        analyzed += '\n\n'
        analyzed += 'Numbers of characters in TEXT: ' + str(count)
        params = {'purpose':'Characters Counted','analyzed_text': analyzed }
    
    if analyzed:
        return render(request,'analyze.html',params)
    else:
        return render(request,'danger.html')