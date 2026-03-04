from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from cars.forms import CommentForm
from cars.models import Brand, Car

# Create your views here.
class HomeView(ListView):
    model = Car
    template_name = 'cars/home.html'
    context_object_name = 'cars'

    def get_queryset(self):
        queryset = Car.objects.all()
        brand_id = self.request.GET.get('brand')
        if brand_id:
            queryset = queryset.filter(brand__id=brand_id)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        context['selected_brand'] = self.request.GET.get('brand', '')
        return context
    
class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comments.all().order_by('-created_at')
        return context
    
    def post(self, request, *args, **kwargs):
        car = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.user = request.user
            comment.save()
            return redirect('car_detail', slug=car.slug)
        context = self.get_context_data()
        context['comment_form'] = form
        return render(request, self.template_name, context)