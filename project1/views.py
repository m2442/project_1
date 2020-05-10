from django.http import HttpResponse
from django.shortcuts import render
import operator

def about(request):
    return render(request, 'about.html')
    
def homepage(request):
    return render(request, 'home.html', {'name': 'mani may'})

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split(' ')
    dict = {}
    for word in wordlist:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    sorted_and_items_dict = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)



    return render(request, 'count.html', {'fulltext': fulltext, 'noofwords': len(wordlist), 'dict': sorted_and_items_dict})
