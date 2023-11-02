from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .utils import get_email_list, email_body
import pandas as pd
from email.mime.text import MIMEText
from django.core.mail import EmailMultiAlternatives

class SendEmailView(APIView):
    def post(self, request):
        first_name = request.data.get('first_name', '')
        last_name = request.data.get('last_name', '')
        company = request.data.get('company', '')

        emails = get_email_list(first_name, last_name, company)
        print(emails)

        subject = "Career - Coffee Chat"
        html_message = email_body(first_name, company)  # HTML email body
        from_email = 'shubhjhawar45@gmail.com'  # Replace with the sender's email address

        for email in emails:
            print("email sent!")
            # Use EmailMultiAlternatives to send an HTML email
            msg = EmailMultiAlternatives(subject, 'Plain text message', from_email, [email])
            msg.attach_alternative(html_message, "text/html")
            msg.send()

        results = [[first_name, last_name, company]]  # Wrap the data in a list

        # Update the Excel file with the email information
        self.update_excel_file(results)

        return Response({"success": emails}, status=status.HTTP_200_OK)

    def update_excel_file(self, results):
        # Load the existing Excel file
        try:
            df = pd.read_excel('email_data.xlsx')
        except FileNotFoundError:
            # Handle the case where the file doesn't exist
            df = pd.DataFrame(columns=['First Name', 'Last Name', 'Company'])

        # Create a DataFrame from the results
        new_data = pd.DataFrame(results, columns=['First Name', 'Last Name', 'Company'])

        # Concatenate the new data with the existing data (if any)
        df = pd.concat([df, new_data])

        # Save the updated data to the Excel file
        df.to_excel('email_data.xlsx', index=False)
