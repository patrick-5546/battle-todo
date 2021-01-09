from django.shortcuts import render

# Create your views here.


def teamHub(request) {
    return render(request, 'team-hub/team-hub.html')
}
