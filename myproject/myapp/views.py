from django.shortcuts import render
from .forms import BookingForm
from django.shortcuts import redirect
from .models import Booking

def index(request):
    return render(request, 'index.html')

def rooms(request):
    return render(request, 'rooms.html')

def booking(request):
    return render(request, 'booking.html')

def book_room(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})

def booking(request):
    return render(request, 'booking_success.html')

def view_bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'view_bookings.html', {'bookings': bookings})

def book(request):
    return render(request, 'book.html')