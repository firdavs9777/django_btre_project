from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
# Create your views here.
def contact(request):
  if request.method == 'POST':
    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    realtor_email = request.POST['realtor_email']

    # First check if the user is authenticated or not
    if request.user.is_authenticated: 
      user_id = request.user.id 
      # If already connected before
      has_connected = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
      if has_connected:
        messages.error(request, 'You have already made an inquiry for this listing')
        return redirect('/listings/' + listing_id)
      

    contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
    contact.save()
    send_mail(
    'New Property Listing Inquiry', 
    f"""
    Hello,

    You have received a new inquiry for the property listing: {listing}.

    Here are the details of the inquiry:

    - Name: {name}
    - Email: {email}
    - Phone: {phone}
    - Message: {message}

    Please log in to the admin panel to view more information about this inquiry.

    Regards,
    The Property Team
    """, 
    'fmutalipov7@gmail.com', 
    [realtor_email, 'techinfo@gmail.com'], 
    fail_silently=False
    )

    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect('/listings/' + listing_id)