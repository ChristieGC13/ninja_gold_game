from django.shortcuts import render, redirect
import random

# Create your views here.
def root(request):
    if 'counter' not in request.session:
        request.session['counter'] += 1
    if 'activities' not in request.session:
        request.session['activities'] = []
    if 'gold_total' not in request.session:
        request.session['gold_total'] = 0
    return render(request, 'index.html')

def process(request):
    print(request.POST['place'])
    place = request.POST['place']
    gold_total = request.session['gold_total']
    if (place == "farm"):
        gold_found = random.randint(10, 20)
        gold_total += gold_found
        request.session['activities'].append(f'Earned {gold_found} gold pieces from the farm!')
    elif (place == "cave"):
        gold_found = random.randint(5,10)
        gold_total += gold_found
        request.session['activities'].append(f'Earned {gold_found} gold pieces from the cave!')
    elif (place == "house"):
        gold_found = random.randint(2, 5)
        gold_total += gold_found
        request.session['activities'].append(f'Earned {gold_found} gold pieces from the house!')
    else:
        gold_found = random.randint(-50, 50)
        gold_total += gold_found
        request.session['activities'].append(f'Earned {gold_found} gold pieces from the casino!')
    return redirect('/')

def reset(request):
    del request.session
    return redirect('/')