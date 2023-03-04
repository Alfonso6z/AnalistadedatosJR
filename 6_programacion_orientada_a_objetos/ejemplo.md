# Ejemplo de Programación Orientada a Objetos (POO)

## Clase Vehiculo
## Crear una clase de vehículo sin variables ni métodos.
```python
class Vehiculo:
    pass
```
## Agrega atributos de instancia: vehículo con atributos nombre,velocidad_max y kilometraje (en el constructor).
```python
class Vehiculo:
    def __init__(self,nombre, velocidad_max, kilometraje):
        self.nombre = nombre
        self.velocidad_max = velocidad_max
        self.kilometraje = kilometraje
```
Crea un objeto Vehiculo e imprime sus atributos:
```
nombre: bocho, velocidad maxima: 200 km, kilometraje: 50000 km
```
__Crea el objeto en main() y muestra sus atributos__
## Crea una clase Autobus que heredará todas las variables y métodos de la clase Vehículo.
```python
class Autobus(Vehiculo):
    pass
```
__Crea un objeto Autobus y muestra sus atributos__
```
Nombre del Autobus: Escuela Volvo Velocidad: 180 Kilometraje: 1200 km
```

## Modifica la clase Automovil y agrega el método(función o comportamiento) capacidad_pasajeros
```python
class Vehiculo:
    def __init__(self,nombre, velocidad_max, kilometraje):
        self.nombre = nombre
        self.velocidad_max = velocidad_max
        self.kilometraje = kilometraje
    def capacidad_pasajeros(self,capacidad):
        return f"La capacidad es de {self.nombre} es de {capacidad} pasajeros"
```
### Sobre escribe el método en la clase Autobus
```python
class Autobus(Vehiculo):
    # sobre escribe el método
    def capacidad_pasajeros(self,capacidad=50):
        return f"La capacidad es de {self.nombre} es de {capacidad} pasajeros"
```
__Crea el objeto autobus e imprime la capacidad de pasajeros__

## Defina un atributo de clase “ color ” con un valor por defecto blanco . Es decir, cada vehículo debe ser blanco.
```python
class Vehiculo:
    color = "Blanco"
    def __init__(self,nombre, velocidad_max, kilometraje):
        self.nombre = nombre
        self.velocidad_max = velocidad_max
        self.kilometraje = kilometraje
```
## El cargo de tarifa predeterminado de cualquier vehículo es capacidad de asientos * 100 . Si el vehículo es una instancia de autobús , debemos agregar un 10% adicional en la tarifa completa como cargo de mantenimiento. Entonces, la tarifa total para la instancia de autobús se convertirá en el monto final = tarifa total + 10% de la tarifa total.

```python
class Vehiculo:
    def __init__(self,nombre, velocidad_max, kilometraje,capacidad):
        self.nombre = nombre
        self.velocidad_max = velocidad_max
        self.kilometraje = kilometraje
        self.capacidad = capacidad

    def capacidad_pasajeros(self):
        return f"La capacidad es de {self.nombre} es de {self.capacidad} pasajeros"
    
    def tarifa(self):
        return self.capacidad * 100
```

Sobre escribimos el método tarifa en la clase Autobus
```python
class Autobus(Vehiculo):
    # sobre escribe el método
    def capacidad_pasajeros(self,capacidad=50):
        return f"La capacidad es de {self.nombre} es de {capacidad} pasajeros"
    
    def tarifa(self):
        monto = super().tarifa()
        monto += monto*10/100
        return monto
```
### Verifica el tipo del objeto autobus y si pertenece a la instancia del objeto Autobus
```python
print(type(autobus_1))
print(isinstance(autobus_1,Vehiculo))

```

