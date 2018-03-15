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
            form.save()

            # first = form.cleaned_data['first_name']
            # last = form.cleaned_data['last_name']
            # email = form.cleaned_data['email_id']
            # user = User(first_name=first, last_name=last, email_id=email)
            # user.save()

    return render(request, 'second_app/form_details.html', {'form': form})


def relative(request):
    return  render(request, 'second_app/relative_url.html')
