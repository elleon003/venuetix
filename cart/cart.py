from decimal import Decimal
from django.conf import settings
from events.models import Event 

class Cart:
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, event, quantity=1, override_quantity=False):
        """
        Add an event ticket to the cart or update its quantity
        """
        event_id = str(event.id)
        if event_id not in self.cart:
            self.cart[event_id] = {
                'quantity': 0,
                'price': str(event.price)
            }
        if override_quantity:
            self.cart[event_id]['quantity'] = quantity
        else:
            self.cart[event_id]['quantity'] += quantity
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, event):
        """
        Remove an event from the cart
        """
        event_id = str(event.id)
        if event_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the event tickets from the database
        """
        event_ids = self.cart.keys()
        # get the event objects and add them to the cart
        events = Event.objects.filter(id__in=event_ids)
        cart = self.cart.copy()
        for event in events:
            cart[str(event.id)]['event'] = event
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(
            Decimal(item['price']) * item['quantity']
            for item in self.cart.values()
        )

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()