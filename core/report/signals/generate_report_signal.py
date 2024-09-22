from django.dispatch import receiver
from django.db.models.signals import post_save
from core.report.models import Report
from core.report.use_case.report import generate_pdf
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework import status
import requests

@receiver(post_save, sender=Report)
def generateReport(sender, instance, **kwargs):
    try:
        pdf = generate_pdf(title=str(instance.title), text=str(instance.text_body), name_freelancer=str(instance.accept_proposal.proposal.perfil.user.name), date_finished="10")
    except BaseException as error:
        return Response({"message": f"Houve um erro dentro de receicer: {str(error)}"})
        
    response = requests.get(pdf)

    with open('pizza.pf') as file:
        file.write(f)


    try:
        subject = 'Relatório'
        message = 
        recipient_list = [instance.accept_proposal.proposal.project.contractor.email]
        from_email = "martinsbarroskaua85@gmail.com"
        send_mail (
            subject=subject,
            message=message,
            recipient_list=recipient_list,
            from_email=from_email,
        )
    except BaseException as error:
        return Response({"message": f"Houve um erro!!!!: {str(error)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

