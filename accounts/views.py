from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.contrib import messages
from .forms import UserProfileForm


class UserProfileView(View):
    def get(self, request, *args, **kwargs):
        form = UserProfileForm(instance=request.user)
        return render(request, "account/profile.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = UserProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Your profile is update!")

            except Exception as e:
                messages.error(request, f"An error occured: {str(e)}")

        else:
            messages.error(request, "Please try again!")

        return HttpResponseRedirect(request.META["HTTP_REFERER"])
