from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis = [
    {
    'hotel_id': 1,
    'nome': 'Pousada Belissima',
    'estrelas': 4.5,
    'diaria': 170.50,
    'cidade': 'Serrinha/BA'
    },
    
    {
    'hotel_id': 2,
    'nome': 'Copacabana Palace Hotel',
    'estrelas': 4.2,
    'diaria': 320.70,
    'cidade': 'Rio de Janeiro/RJ'

    },
    
    {
    'hotel_id': 3,
    'nome': 'Ibis',
    'estrelas': 5.0,
    'diaria': 300.00,
    'cidade': 'São Paulo/SP'
    }
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]} # SELECT * FROM hoteis


class Hotel(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome'),
    atributos.add_argument('estrelas'),
    atributos.add_argument('diaria'),
    atributos.add_argument('cidade'),

    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        
        return {'Message': 'Hotel not found!'}, 404 # Not found      

    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return f"message: Hotel ID {hotel_id} already exists!", 400 # Bad request  
            #return 'Hotel já existe!'  
        dados = Hotel.atributos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        hotel.save_hotel()
        return hotel.json()

    def put(self, hotel_id):
        dados = Hotel.atributos.parse_args()
        hotel_encontrado = HotelModel.find_hotel(hotel_id)
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200 # OK
        hotel = HotelModel(hotel_id, **dados)
        hotel.save_hotel()
        return hotel.json(), 201 # created criado

    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            hotel.delete_hotel()
            return {'message': 'Hotel deleted.'}
        return {"message": "Hotel not found."}, 404
