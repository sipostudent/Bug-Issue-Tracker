from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime

from .forms import CreateTicketForm, EditTicketForm
from .models import Ticket
from account.models import User


# Create your views here.
def index(request):  

    email = request.session.get('user_email')
    print(email)

    ticket_list = [
        {
            'id': ticket.id,
            'title': ticket.title,
            'category': ticket.category.title(),
            'date': ticket.time
        }
        for ticket in Ticket.objects.order_by('id')
    ]

    page = request.GET.get('page', 1)
    paginator = Paginator(ticket_list, 10)
    tickets = paginator.get_page(page)
    form = CreateTicketForm()

    print(paginator.page_range)

    return render(
        request,
        'index.html',
        {
            'tickets': tickets,
            'page': paginator.page_range,
            'form': form
        }
    )


def details(request, id):
       
    email = request.session.get('user_email')
    print(email)
    email = request.session.get('user_email')

    if email:
        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            user = None
    else:
        user = None

    try:
        ticket = Ticket.objects.get(id=int(id))
        return render(request, 'details.html', {'ticket': ticket, 'user': user})
    except ObjectDoesNotExist:
        return redirect('index')

def edit_details(request, id):

    email = request.session.get('user_email')
    print(email)
    email = request.session.get('user_email')

    if email:
        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            return redirect('login')

        try:
            ticket = Ticket.objects.get(id=int(id))
        except ObjectDoesNotExist:
            return redirect('index')

        try:
            assert(ticket.user == user)
        except AssertionError:
            return redirect(f'details/{id}')
    else:
        return redirect('login')
    
    form = EditTicketForm(initial={
        'title': ticket.title,
        'category': ticket.category,
        'details': ticket.details
    })

    if request.method == "POST":
        form = EditTicketForm(request.POST)

        if form.is_valid():
            ticket.title = form.cleaned_data['title']
            ticket.category = form.cleaned_data['category']
            ticket.details = form.cleaned_data['details']

            ticket.save()

    return render(request, 'edit_details.html', {'ticket': ticket, 'form': form})


def create_ticket(request):

    email = request.session.get('user_email')
    print(email)
    email = request.session.get('user_email')
    
    if email:
        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            return redirect('login')

    form = CreateTicketForm()

    if request.method == 'POST':
        print("posted")
        form = CreateTicketForm(request.POST)

        if form.is_valid():
            print("valid form")
            ticket = Ticket(
                title=form.cleaned_data['title'],
                time=datetime.now(),
                category=form.cleaned_data['category'],
                details=form.cleaned_data['details'],
                user=user
            )

            ticket.save()
            return redirect(f'/details/{ticket.id}')
        else:
            return redirect('/')

    return redirect('/')


def delete_ticket(request, id):
    email = request.session.get('user_email')
    print(email)
    email = request.session.get('user_email')
    
    if email:
        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            return redirect('login')

        ticket = Ticket.objects.get(id = int(id))

        if ticket.user == user:
            ticket.delete()

    return redirect('/')
