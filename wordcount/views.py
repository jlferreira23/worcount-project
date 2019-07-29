from django.http import HttpResponse
from django.shortcuts import render
import operator
from django.core.mail import send_mail

Jayson = "Jayson Ferreira-ballsack"
def home(request):
    return render(request, 'home.html')

def eggs(request):
    return HttpResponse('Eggs are Great!')

def about(request):


    author = Jayson
    copyright = "Copyright 2019"

    return render(request, 'about.html', {'author':author, 'copyright':copyright})

def count(request):
    fulltext = request.GET['fulltext']

    send_mail(
        'Subject',
        fulltext,
        'Test@copyright.com',
        ['jferreira@copyright.com']
            )

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] +=1
        else:
            #Add to dictionary
            worddictionary[word] = 1

        sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})
