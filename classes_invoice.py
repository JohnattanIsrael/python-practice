# class Invoice:

#     def greeting(self):
#         return 'Hi there'

# # Instatiation
# inv_one = Invoice()
# print(inv_one.greeting())

# inv_two = Invoice()
# print(inv_two.greeting())

class Invoice():

    def __init__ (self, client, total):
        self.client = client
        self.total = total

    def formatter(self):
        return f'{self.client} owes: ${self.total}'

google = Invoice('Google', 100)
snapchat = Invoice('Snapchat', 200)

print(google.formatter())
print(snapchat.formatter())

print(google.client)
print(snapchat.client)

google.client = 'Yahoo'
print(google.client)

# Now you can help rotect the data by using _ => Protected __ => Private
# getter & setter
print('------------------')

class InvoiceTwo():

    def __init__(self, cliente, totales):
        self._cliente = cliente
        self._totales = totales

    def formateado(self):
        return f' {cliente} ows: ${totales}'

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente

    @property
    def totales(self):
        return self._totales
    
pimarc = InvoiceTwo('Pimarc', 15000)
print(pimarc.cliente)

pimarc.cliente = 'Palmyra'

print(pimarc.cliente)
