from django.shortcuts import render

def index(request):
    # context = {
    #     'base_info': BaseInfo.objects.first(),
    #     'menus' : Menu.objects.all(),
    #     'areas' : Areas.objects.all(),
    #     'news' : News.objects.filter(published=True).order_by('-date'),
    #     'speakers' : Speakers.objects.all(),
    #     'topics' : TopicAreas.objects.all(),
    #     'dates' : ImportantDates.objects.all(),
    #     'footer' : Footer.objects.first(),
    #     'prog_com' : Organizers.objects.filter(Q(committee__contains='prog')),
    #     'org_com': Organizers.objects.filter(Q(committee__contains='org')),
    #     'publications' : Publications.objects.all(),
    #     'fees' : Fees.objects.all(),
    # }
    return render(request, 'index.html')