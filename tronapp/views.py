from django.shortcuts import render
import requests
import json

def index(request):
    context = {}
    if request.method == 'POST':
        tx_hash = request.POST.get('tx_hash')
        if tx_hash:
            url = f"https://apilist.tronscan.org/api/transaction-info?hash={tx_hash}"
            try:
                response = requests.get(url)
                data = response.json()
                context['result'] = json.dumps(data, ensure_ascii=False, indent=4)
            except Exception as e:
                context['error'] = str(e)
    return render(request, 'tronapp/index.html', context)