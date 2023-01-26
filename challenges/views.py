from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Finish Django Course",
    "february": "Finish React Course",
    "march": "Master DS Algo",
    "april": "Get into 55kg",
    "may": "Daily cardio",
    "june": "Cybersecurity",
    "july": "Footy",
    "august": "AI",
    "september": "Interview prep",
    "october": "4 start in codechef",
    "november": "relax in india",
    "december": "get new job"
}


def index(request):
    # response_data = """
    # <ul>
    #     <li><a href="january">January</a></li>
    # </ul>
    # """
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f'<li><a href=\"{month_path}\">{capitalized_month}</a></li>'
        response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
# def january(request):
#     return HttpResponse("Finish Django Course")


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month</h1>")
    redirect_month = months[month-1]
    reditect_path = reverse(
        "month-challenge", args=[redirect_month])  # challenge/january
    return HttpResponseRedirect(reditect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")

    # if month == 'january':
    #     challenge_text = "Finish Django Course"
    # elif month == 'february':
    #     challenge_text = "Finish React Course"
    # elif month == 'march':
    #     challenge_text = "Master DS Algo"
    # else:
    #     return HttpResponseNotFound("This month is not supported")
    # return HttpResponse(challenge_text)
