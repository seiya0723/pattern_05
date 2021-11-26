from django.shortcuts import render,redirect
from django.views import View

from .models import Pattern
from .forms import PatternForm


class IndexView(View):

    def get(self, request, *args, **kwargs):

        patterns    = Pattern.objects.all()
        context     = { "patterns":patterns }

        return render(request,"shop/index.html",context)


    def post(self, request, *args, **kwargs):

        form    = PatternForm(request.POST, request.FILES)

        if form.is_valid():
            print("バリデーションOK")
            #保存する
            form.save()
        else:
            print("バリデーションNG")

        return redirect("shop:index")

index   = IndexView.as_view()

