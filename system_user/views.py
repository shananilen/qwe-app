from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model


# Create your views here.
def user_approvals(request):
    user = get_user_model()
    user_groups = Group.objects.all()
    pending_users = user.objects.filter(is_active=False)
    context = {
        "PENDING_USERS": pending_users,
        "GROUPS": user_groups
    }
    return render(request, 'system_user/user_approvals.html', context)


def approve_user_with_group(request, user_id):
    User = get_user_model()
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        print(group_name)
        pending_user = User.objects.get(id=user_id)
        user_group = Group.objects.get(name=group_name)
        if pending_user and user_group:
            pending_user.groups.add(user_group)
            pending_user.is_active = True
            pending_user.save()
    return redirect('approvals_overview_path')
