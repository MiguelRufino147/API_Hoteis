from flask_restful import Resource,reqparse

#LISTA FILMES
filmes=[{
    'id':1,
    'nome':'A espera de um milagre',
    'ano':1999
},
    {
        'id':2,
        'nome':'Forest Gump',
        'ano':1991
    }
]



#CLASSES GERAIS

#primeira classe: Get geral
class BUSCAR_TODOS_FILMES(Resource):
    def get(self):
        return filmes


#segunda classe:get,post,put,delete por id
class LOCALIZAR_FILMES_ESPECÍFICOS(Resource):
    def get (self,id):
        for filme in filmes:
            if filme['id']==id:
                return filme
        return None

    def post (self,id):
        parser=reqparse.RequestParser()
        parser.add_argument('nome')
        parser.add_argument('ano')
        args=parser.parse_args()
        novo_hotel={
            'id':id,
            'nome':args['nome'],
            'ano':args['ano']
        }

        filmes.append(novo_hotel)
        return '<message:filme add>'


