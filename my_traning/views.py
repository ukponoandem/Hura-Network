

# def send_message():
#    message = client.messages.create(
#       body = "Hi ,This is a automation repetitive",
#       from_ = "+15077078557" ,   
#       to =  "+2349161248397"
#    )
   
#    print(f"message from me {message.sid}")



# send_message()



# import smtplib
# import schedule
# import time

# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart


# def email_sender():
#     sender = "ukponoadem@gmail.com"
#     recipient_email = "ukponoadem@gmail.com"
#     password = 'mogj dheq kzyj igpy'
    
#     subject = "AUTOMATION REPETITIVE TASK...."
#     body = f"Hello {recipient_email},This is an automation repetitive task."

#     # Create message
#     message = MIMEMultipart()
#     message["From"] = sender
#     message["To"] = recipient_email
#     message["Subject"] = subject
#     message.attach(MIMEText(body, "plain"))
    


#     try:
#         # Connect to the SMTP server
#         # server = smtplib.SMTP('smtp.gmail.com', 587)
#         server = smtplib.SMTP_SSL("smtp.gmail.com", 465) 
#           # Secure the connection
#         server.login(sender, password)  # Login
#         server.sendmail(sender, recipient_email, message.as_string())  # Send the email
        
#         print(f"Email sent to {recipient_email}")
        
#     except Exception as e:
#         print(f"Error: {e}")
#     finally:
        # server.quit()  # Close the server connection

 #Schedule the email to be sent every day at 07:00 AM
# schedule.every().day.at("07:00").do(email_sender)

# while True:
#         schedule.run_pending()  # Run scheduled tasks
#         time.sleep(1)  # Wait for 60 seconds before checking again


# email_sender()
# Create your views here.


from django.shortcuts import render
def about(request):
    return render(request,"about.html")
def index(request):
    return render(request,"index.html")

# def price(request):
#     return render(request,"price.html")

# def service(request):
#     return render(request,"service.html")

def speed(request):
    return render(request,"speed.html")

def radio(request):
    return render(request,"radio.html")

def radiob(request):
    return render(request,"radio b.html")
def speedb(request):
    return render(request,"speed b.html")
def cloudb(request):
    return render(request,"cloud b.html")
def datab(request):
    return render(request,"data b.html")
def voipb(request):
    return render(request,"voip.html")
def coverage(request):
    return render(request,"coverage.html")
def contact(request):
    return render(request,"contact.html")

from .sender_mail import send_email
from django.http import HttpResponse

def email_sender(request):
    if request.method == "POST":
        
      # Get form data
        First = request.POST.get('First')
        message = request.POST.get('message')
        number = request.POST.get('number')
        email = request.POST.get('email')
        page = request.POST.get('page') 
        # First_name = request.POST.get('Firstname')
        # Last_name = request.POST.get('Last_name')
        # message = request.POST.get('message')
        # Email = request.POST.get('email')
        
        
        print(f"Form submitted from: {First} {number}")
        

        try:
            # Prepare subject and body for the email
            subject = f"Message from {First}  number {number} message"
            body = message
            to_email = 'hurawireless@gmail.com'  # This is your email address
            from_email = 'ukponoadem@gmail.com'  # Same as sender's email (your email)
            password = 'eggf vykb lkxd yajo'  # Your email password or app password
            

            send_email(subject, body, to_email, from_email, password)
            return HttpResponse(f"Email sent successfully from {email} to {to_email}, check your inbox!")
        # return HttpResponse(f"Email sent successfully to {to_email}, check your inbox!")
        except Exception as e:
            return HttpResponse(f"Failed to send email: {e}")
        
        
        
        
    if request.path == 'email_sender/':
    #     # Render the default contact form template
        return render(request, 'contact.html') 
    # # You can also render different templates based on the 'page' value
    # # Example: Render different templates for design, disasters, or edge
    # if 'design' in request.path:
    #     return render(request, 'design.html')
    # elif 'disasters' in request.path:
    #     return render(request, 'disaster.html')
    # elif 'edge' in request.path:
    #     return render(request, 'edge.html')
        
    



