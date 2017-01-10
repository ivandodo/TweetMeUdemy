from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin


# Create your views here.

#If you want to show form even to not authenticated user then you use FormUserNeededMixin
class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = "/tweets"
    #login_url="/admin/"

class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    success_url = "/tweets"
    template_name = 'tweets/update_view.html'

class TweetDetailView(DetailView):
    template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()

    def get_object(self):
        #print(self.kwargs)
        pk = self.kwargs.get("pk")
        obj = get_object_or_404(Tweet, pk=pk)
        return obj

class TweetDeleteView(DeleteView):
    #queryset = Tweet.object.all()
    #model is the same as queryset
    model = Tweet
    template_name = "tweets/delete_confirm.html"
    success_url = reverse_lazy("home")

class TweetListView(ListView):
    template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        #context["another_list"] = Tweet.objects.all()
        return context

# def tweet_create_view(request):
#     form = TweetModelForm(request.POST or None)
#
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.user = request.user
#         instance.save()
#     context = {
#         "form" : form
#     }
#     return render(request, 'tweets/create_view.html', context)

#retrieve
# def tweet_detail_view(request, id=1):
#     obj = Tweet.objects.get(id=id)
#     #print(obj)
#     context = {
#         "object" : obj
#     }
#
#     return render(request, "tweets/detail_view.html", context)
#
# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     #print(queryset)
#
#     context = {
#         "object_list" : queryset
#     }
#
#     return render(request, "tweets/list_view.html", context)