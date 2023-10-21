from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .utils import get_email_list
import pandas as pd

# Create your views here.

class SendEmailView(APIView):
    def post(self, request):
        first_name = request.data.get('first_name', '')
        last_name = request.data.get('last_name', '')
        company = request.data.get('company', '')

        emails = get_email_list(first_name, last_name, company)
        print(emails)

        subject = 'Hello, Django Email Excel!'
        message = f'Hello {first_name}, please give job.'
        from_email = 'shubhjhawar78@example.com'  # Replace with the sender's email address

        send_mail(subject, message, from_email, emails, fail_silently=False)

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
