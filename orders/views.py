from django.core.exceptions import ValidationError
from django.db import transaction
from django.shortcuts import redirect
from django.views.generic import CreateView, FormView

from carts.models import Cart
from orders.forms import CreateOrderForm
from orders.models import Orders, OrderItems
from users.mixins import MessagesMixin


# Create your views here.
class CreateOrderView(MessagesMixin, FormView):
	template_name = "orders/create_order.html"
	form_class = CreateOrderForm
	messages = "Заказ успешно оформлен"
	success_url = "user:profile"

	def form_valid(self, form):
		try:
			with transaction.atomic():
				user = self.request.user
				cart_items = Cart.objects.filter(user=user)
				if cart_items.exists():
					order = Orders.objects.create(
						user=user,
						requires_delivery=form.cleaned_data["requires_delivery"],
						address_delivery=form.cleaned_data.get("address_delivery", "Самовывоз"),
						payment_on_get=form.cleaned_data["payment_on_get"]
					)

					for cart_item in cart_items:
						product = cart_item.product
						title = cart_item.product.title
						quantity = cart_item.quantity
						price = cart_item.product.sell_price()

						if product.quantity < quantity:
							raise ValidationError(
								f"Недостаточно товара {title} на складе|В наличии: {product.quantity}")
						OrderItems.objects.create(
							order=order,
							product=product,
							title=title,
							quantity=quantity,
							price=price
						)
						product.quantity -= quantity
						product.save()

					cart_items.delete()
					return redirect(self.get_success_url())

		except ValidationError as e:
			self.success_url = "cart:user_cart"
			self.messages = str(e)
			return redirect(self.get_success_url())

	def get_context_data(self, **kwargs):
		kwargs["order"] = True
		return super().get_context_data(**kwargs)
