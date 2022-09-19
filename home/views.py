from django.shortcuts import render, redirect
from home.models import Contact
from django.contrib import messages
import requests


def index(request):
    return render(request, 'index/index.html')


def services(request):
    return render(request, 'services/services.html')


def portfolio(request):
    return render(request, 'portfolio/portfolio.html')


def about(request):
    return render(request, 'about/about.html')


def get_client_ip(request):
    x = request.META.get('HTTP_X_FORWARDED_FOR')
    if x:
        ip = x.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        data = Contact()
        data.full_name = full_name
        data.phone = phone
        data.message = message
        data.ip = get_client_ip(request)
        data.save()
        messages.success(request, 'Xabaringiz muvoffaqiyatli qabul qilindi! Sizga qisqa vaqt ichida javob beramiz. Raxmat!')

        text = f'🇺🇿 YANGI XABAR KELDI! 🇺🇿 \n' \
               f'\n 👨  FISH: {data.full_name}' \
               f'\n 📲  Telefon raqam: {data.phone}' \
               f'\n 🌐  IP RAQAM: {data.ip}' \
               f'\n 🕒  VAQT: {data.create_time.strftime("%H:%M")}' \
               f'\n 📆  SANA: {data.create_date.strftime("%d-%b, %Y-Yil")}' \
               f'\n 📩  XABAR: {data.message}'
        text1 = "".join(text)

        bot_token = '5726836910:AAEm6JYGKnzk3Pm-YAutEqdUFZ1jSbsHY9M'
        bot_chatID = '1255807110'

        url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={text1}'

        response = requests.get(url)
        return redirect('contact')

    return render(request, 'contact/contact.html')
