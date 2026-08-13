class AddressMixin:

    @property
    def full_address(self):
        return ", ".join(filter(None, [
            self.address_line1,
            self.address_line2,
            self.city,
            self.state,
            self.country
        ]))

    def greeting(self):
        return f"Welcome to {self.city}"