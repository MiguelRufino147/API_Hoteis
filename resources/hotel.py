
from flask_restful import Resource,reqparse
from models.hotelmod import HotelModel
hoteis=[
    {
        'hotel_id':'alpha',
        'nome':'Alpha hotel',
        'estrelas':4.3

    },
    {
        'hotel_id':'musi',
        'nome':'musi hotel',
        'estrelas':4.6
    },
    {
        'hotel_id':'paulo',
        'nome':'paulo hotel',
        'estrelas':3.2
    }
]



class Hoteis(Resource):
    def get(self):
        return {'hoteis':hoteis}


class localizar_Hotel(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')






    def verificar_existencia(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    #MÉTODOS

    def get(self, hotel_id):
        hotel = localizar_Hotel.verificar_existencia(hotel_id)
        if hotel:
            return hotel
        return {'message': 'Not Found'}, 404

    def post(self, hotel_id):

        dados=localizar_Hotel.argumentos.parse_args()
        hotelobj=HotelModel(hotel_id,**dados)
        novo_hotel=hotelobj.json()
        hoteis.append(novo_hotel)
        return {'message':'Adicionado'}

    def put(self,hotel_id):
        dados=localizar_Hotel.argumentos.parse_args()
        hotelobj=HotelModel(hotel_id,**dados)
        novo_hotel=hotelobj.json()
        hotel=localizar_Hotel.verificar_existencia(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
        hoteis.append(novo_hotel)
        return novo_hotel





    def delete(self, hotel_id):
        global hoteis
        hoteis=[hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]




