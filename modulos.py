#hay modulos en la libreria de phytho
#en internet google phython modulos o pypi
#y los tuyos
#control + f para buscador de funciones en la web
#uso pip para instalar modulos de terceros en internet
#usar framewors y thimker jusmto con la teoria para seguir aprendiendo
import datetime

print(datetime.date.today())

print(datetime.timedelta(minutes=70))

# se puede hacer de esta otra forma
from datetime import timedelta, date
print(date.today)

#a continuacion estoy importando una funcion de mimodulo y ejecutandola aqui

from mimodulo import sumar, restar
sumar (1,2)
restar(1,2)

