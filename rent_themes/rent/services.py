from .models import Theme, Rent
from datetime import datetime

class Util:
    def calcular_desconto(self, idCliente: int, idTema: int, rent: Rent):
        desconto = 0

        #conta quantos alugueis o cliente tem
        rentCount = Rent.objects.filter(client = idCliente).count()
        if rentCount>0:
            desconto +=10

        #transforme o date em uma instancia date
        if isinstance(rent.date, str):
            rent_date = datetime.strptime(rent.date, '%Y-%m-%d').date()
        else:
            rent_date = rent.date
        
        #descobre o dia da semana
        dia = rent_date.weekday()
        if (dia == 0 or dia == 1 or dia == 2 or dia == 3):
            desconto +=40   

        #recupera o preço do tema
        tema = Theme.objects.get(id=idTema)
        precoTema = tema.price

        #calcula valor final com os descontos aplicados
        finalValue = ((100-desconto)* precoTema)/100
        return finalValue


