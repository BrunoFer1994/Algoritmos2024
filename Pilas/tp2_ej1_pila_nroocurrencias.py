# 1. Determinar el número de ocurrencias de un determinado elemento en una pila.
from pila import Pila  # Importación relativa de la clase Pila desde pila.py en el mismo directorio

class UtilidadesPila(object):
    def __init__(self, pila):
        self.pila = pila  # Asigna la pila sobre la cual deseas operar
    
    def contar_ocurrencias(self, elemento):
        contador = 0
        
        # Creamos una pila auxiliar para no alterar la pila original
        pila_auxiliar = Pila()
        
        # Mientras la pila original no esté vacía
        while not self.pila.pila_vacia():
            # Desapilamos el elemento de la pila original
            dato = self.pila.desapilar()
            # Verificamos si es el elemento que estamos buscando
            if dato == elemento:
                contador += 1  # Incrementamos el contador si encontramos una ocurrencia
            # Apilamos el elemento en la pila auxiliar
            pila_auxiliar.apilar(dato)
        
        # Devolvemos los elementos de la pila auxiliar a la pila original
        while not pila_auxiliar.pila_vacia():
            self.pila.apilar(pila_auxiliar.desapilar())
        
        return contador

# Uso de las clases para contar ocurrencias
mi_pila = Pila()
mi_pila.apilar(1)
mi_pila.apilar(2)
mi_pila.apilar(3)
mi_pila.apilar(2)
mi_pila.apilar(2)

utilidades = UtilidadesPila(mi_pila)
elemento_buscado = 2
ocurrencias = utilidades.contar_ocurrencias(elemento_buscado)

print(f"El elemento {elemento_buscado} aparece {ocurrencias} veces en la pila.")
