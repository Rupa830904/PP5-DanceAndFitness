from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Package
from profiles.models import UserProfile

import json
import time
import stripe


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        #subject = render_to_string(
         #   "Dance and Fitness: Order confirmation"
        #)
        subject = "Dance and Fitness: Order confirmation"
        #body = render_to_string(
        #    {"order": order, "contact_email": settings.DEFAULT_FROM_EMAIL},
        #)
        body = "test"

        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [cust_email])

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}', status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)
        print(stripe_charge)

        billing_details = stripe_charge.billing_details  # updated
        #shipping_details = intent.shipping

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        print(billing_details)
        if username != "AnonymousUser":
            profile = UserProfile.objects.get(user__username=username)
            #if save_info:
            #    profile.default_phone_number = shipping_details.phone
            #    profile.default_country = shipping_details.address.country
            #    profile.default_postcode = shipping_details.address.postal_code
            #    profile.default_town_or_city = shipping_details.address.city
            #    profile.default_street_address1 = shipping_details.address.line1
            #    profile.default_street_address2 = shipping_details.address.line2
            #    profile.default_county = shipping_details.address.state
            #    profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    #phone_number__iexact=shipping_details.phone,
                    #country__iexact=shipping_details.address.country,
                    #postcode__iexact=shipping_details.address.postal_code,
                    #town_or_city__iexact=shipping_details.address.city,
                    #street_address1__iexact=shipping_details.address.line1,
                    #street_address2__iexact=shipping_details.address.line2,
                    #county__iexact=shipping_details.address.state,
                    #order_total=order_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                print(order)
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            print(order)
            self._send_confirmation_email(order)
            return HttpResponse(
                content=(
                    f'Webhook received: {event["type"]} | SUCCESS: '
                    "Verified order already in database"
                ),
                status=200,
            )
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=billing_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    #phone_number=shipping_details.phone,
                    #country=shipping_details.address.country,
                    #postcode=shipping_details.address.postal_code,
                    #town_or_city=shipping_details.address.city,
                    #street_address1=shipping_details.address.line1,
                    #street_address2=shipping_details.address.line2,
                    #county=shipping_details.address.state,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(cart).items():
                    product = Package.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    ##else:
                    ##    for size, quantity in item_data["items_by_size"].items():
                    ##        order_line_item = OrderLineItem(
                    ##            order=order,
                    ##            product=product,
                    ##            quantity=quantity,
                    ##        )
                    ##        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500,
                )
        self._send_confirmation_email(order)
        return HttpResponse(
            content=(
                f'Webhook received: {event["type"]} | SUCCESS: '
                "Created order in webhook"
            ),
            status=200,
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(content=f'Webhook received: {event["type"]}', status=200)
