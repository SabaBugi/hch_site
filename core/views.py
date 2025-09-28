from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Goal, Service, SiteSettings
from .forms import ContactForm


def home(request):
    services = Service.objects.all()
    site_settings = SiteSettings.objects.first()
    goals = Goal.objects.all()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            # Compose email
            subject = f"ახალი შეტყობინება საიტიდან - {name}"
            body = f"""
            სახელი: {name}
            ელ.ფოსტა: {email}

            შეტყობინება:
            {message}
            """

            try:
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,  # Sender (Zoho email)
                    [settings.EMAIL_HOST_USER],   # Recipient (your company Zoho email)
                    fail_silently=False,
                )
                messages.success(request, "თქვენი შეტყობინება წარმატებით გაიგზავნა!")
            except Exception as e:
                messages.error(request, f"შეტყობინების გაგზავნა ვერ მოხერხდა: {e}")

            return redirect("home")
    else:
        form = ContactForm()

    return render(request, "home.html", {
        "services": services,
        "settings": site_settings,
        "goals": goals,
        "form": form,
    })

