from django.shortcuts import render
from django.views import View
# Create your views here.

class Index(View):
    template = 'G_electronics.html'
    context = {}
    def get(self, request):
        context = self.context
        return render(request, self.template, context)
    
    def post(self, request):
        context = self.context
        return render(request, self.template, context)
      


class products(View):
    template = 'products.html'
    context = {}
    def get(self, request):
        context = self.context
        return render(request, self.template, context)
    
    def post(self, request):
        context = self.context
        return render(request, self.template, context)
      