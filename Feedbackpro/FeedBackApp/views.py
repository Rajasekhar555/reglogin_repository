from django.shortcuts import render
from .models import FeedbackData
from .forms import FeedbackForm
from django.http.response import HttpResponse
import datetime

date1 = datetime.datetime.now()


def feedback_view(request):
    if request.method == "POST":
        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            name = request.POST.get("name", '')
            rating = request.POST.get("rating", '')
            feedback = request.POST.get("feedback", '')
            data = FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                date=date1
            )
            data.save()
            fform = FeedbackForm()
            fdata = FeedbackData.objects.all()
            return render(request, 'feedback1.html', {'fform': fform, 'fdata': fdata})
        else:
            return HttpResponse("invalid data")
    else:
        fform = FeedbackForm()
        fdata = FeedbackData.objects.all()
        return render(request, 'feedback1.html', {'fform': fform, 'fdata': fdata})
