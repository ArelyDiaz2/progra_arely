# -*- coding: utf-8 -*-
"""ejercicios_PIA.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RRiZl6VYTKWcknK1EdRxb42faGsC8qI-
"""

class Tienda:
    def __init__(self, monto_compra):
        self.monto_compra = monto_compra

    def aplicar_descuento(self):
        descuento = 0
        if self.monto_compra < 500:
            descuento = 0
        elif 500 <= self.monto_compra <= 1000:
            descuento = 0.05
        elif 1000 < self.monto_compra <= 7000:
            descuento = 0.11
        elif 7000 < self.monto_compra <= 15000:
            descuento = 0.18
        else:
            descuento = 0.25

        descuento_aplicado = self.monto_compra * descuento
        monto_con_descuento = self.monto_compra - descuento_aplicado

        return monto_con_descuento

monto = float(input("Ingrese el monto de la compra: "))
tienda = Tienda(monto)
monto_con_descuento = tienda.aplicar_descuento()

print("El monto con descuento aplicado es: ", monto_con_descuento)

class Dinosaurio:
    def _init_(self, NOM, PES, LON):
        self.NOM = NOM
        self.PES = PES
        self.LON = LON
        self.PESKIL = 0
        self.LONMET = 0

    def dinosaurio(self):
        self.PESKIL = self.PES / 2.20462
        self.LONMET = self.LON * 0.3047

        print(f"Nombre del dinosaurio: {self.NOM}")
        print(f"Peso en kilogramos: {self.PESKIL:.2f} kg")
        print(f"Longitud en metros: {self.LONMET:.2f} m")


dino = Dinosaurio(NOM="Tyrannosaurus Rex", PES=900, LON=40)

dino.dinosaurio()

class Gasolinera:
    def __init__(self, galones_surtidos):
        self.galones_surtidos = galones_surtidos
        self.precio_litro = 8.20
        self.litros_por_galon = 3.785

    def gasolina(self):
        litros_surtidos = self.galones_surtidos * self.litros_por_galon
        monto_a_cobrar = litros_surtidos * self.precio_litro
        return monto_a_cobrar

galones = float(input("Ingrese la cantidad de galones surtidos: "))
gasolinera = Gasolinera(galones)
monto_a_cobrar = gasolinera.gasolina()
print(f"El monto a cobrar al cliente es: {monto_a_cobrar:.2f}")