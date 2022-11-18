from flask import Flask
from flask_restful import Api
from resources.filmes import BUSCAR_TODOS_FILMES,LOCALIZAR_FILMES_ESPECÍFICOS

app=Flask(__name__)
api=Api(app)




api.add_resource(BUSCAR_TODOS_FILMES,'/filmes')
api.add_resource(LOCALIZAR_FILMES_ESPECÍFICOS,'/filmes/<int:id>')


if __name__=='__main__':
    app.run(debug=True)
