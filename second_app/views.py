from django.shortcuts import render
from second_app.models import User
from second_app.forms import FormDetails
# Create your views here.


def index(request):
    return render(request, 'second_app/index.html')


def user(request):
    userlist = User.objects.order_by('first_name')
    mydict = {'user_list': userlist}
    return render(request, 'second_app/show_users.html', context=mydict)


def form_detail_view(request):
    form = FormDetails()
    if request.method == 'POST':
        form = FormDetails(request.POST)
        if form.is_valid():
            print(form.cleaned_data['first_name'])
    return render(request, 'second_app/form_details.html', {'form': form})
