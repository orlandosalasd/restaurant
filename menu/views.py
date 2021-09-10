from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.http import HttpResponseRedirect


from person.choices import ProfileRoles

from menu.models import Menu
from menu.models import Order
from menu.models import FoodOption

from menu.forms import OrderForm
from menu.forms import MenuForm

# Create your views here.


@login_required
def index(request):
    """View function for home page of site."""

    day_menu_options = Menu.objects.filter(menu_date__year=datetime.today().year,
                                           menu_date__month=datetime.today().month,
                                           menu_date__day=datetime.today().day)

    context = {
        'today_menu_options': day_menu_options,
        'number_today_options': day_menu_options.count()
    }
    return render(request, 'index.html', context=context)


# Order Views


class UserOrderView(LoginRequiredMixin, ListView):
    """Generic class-based view listing Orders for user."""
    model = Order
    template_name = 'user_order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        query = Order.objects.filter(order_date__year=datetime.today().year,
                                     order_date__month=datetime.today().month,
                                     order_date__day=datetime.today().day)

        # The Administrators users can see all today order for all users.
        if self.request.user.profile.rol == ProfileRoles.ADMINISTRATOR or self.request.user.is_staff:
            return query
        else:
            return query.filter(user=self.request.user)


class DeleteOrderView(LoginRequiredMixin, DeleteView):
    """Generic class-based view Delete Orders."""
    model = Order
    success_url = "/menu/order"
    template_name = 'order_confirm_delete.html'

    # Validate in case de user is customer, only can delete his orders
    def get_queryset(self):
        query = super(DeleteOrderView, self).get_queryset()
        if self.request.user.profile == ProfileRoles.CUSTOMER:
            return query.filter(user=self.request.user)
        return query


@login_required
def create_order(request):
    """View Method to create a new order"""
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order()
            order.user = request.user
            order.menu = form.cleaned_data['menu']
            order.order_suggestion = form.cleaned_data['order_suggestion']
            order.order_date = datetime.now()
            order.save()

            return HttpResponseRedirect(reverse('order'))
    else:
        form = OrderForm()

    context = {
        'form': form
    }
    return render(request, 'create_order.html', context)


@permission_required('profile.administrator_access')
def create_menu(request):
    """View Method to create a new Menu"""
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = Menu()
            menu.name = form.cleaned_data['name']
            menu.menu_date = datetime.now()
            menu.save()
            for food in form.cleaned_data['food_plates']:
                menu.food_plate.add(food.id)
            menu.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = MenuForm()

    context = {
        'form': form
    }
    return render(request, 'create_order.html', context)


class DeleteMenuView(PermissionRequiredMixin, DeleteView):
    """Generic class-based view Delete Menu."""
    permission_required = 'profile.administrator_access'
    model = Menu
    success_url = "/menu/"
    template_name = 'menu_confirm_delete.html'


class CreateFoodOptionView(PermissionRequiredMixin, CreateView):
    """Class View to create new food plate"""
    permission_required = 'profile.administrator_access'
    model = FoodOption
    fields = ['name', 'description']
    template_name = 'foodoption_form.html'
    success_url = "/menu/order"


class FoodOptionListView(PermissionRequiredMixin, ListView):
    """Generic class-based view listing Orders for user."""
    permission_required = 'profile.administrator_access'
    model = FoodOption
    success_url = "/menu/food/list/"
    template_name = 'food_list.html'
    context_object_name = 'food_options'


class DeleteFoodOptionView(PermissionRequiredMixin, DeleteView):
    """Class View to delete new menu"""
    permission_required = 'profile.administrator_access'
    model = FoodOption
    success_url = "/menu/food/list/"
    template_name = 'food_confirm_delete.html'





