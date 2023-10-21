from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .utils import get_email_list

# Create your views here.


class SendEmailView(APIView):
    def post(self, request):
        first_name = request.data.get('first_name', '')
        last_name = request.data.get('last_name', '')
        company = request.data.get('company', '')

        emails = get_email_list(first_name,last_name, company)
        print(emails)


        subject = 'Hello, Django Email 22!'
        message = 'Please give job.'
        from_email = 'shubhjhawar78@example.com'  # Replace with the sender's email address

        send_mail(subject, message, from_email, emails, fail_silently=False)

        return Response({"success":emails}, status=status.HTTP_200_OK)