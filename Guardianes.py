# =========================================================
#  GUARDIANS OF THE ANCIENT KINGDOM
#  Juego de batalla por turnos en Python
#
#  Características implementadas:
#  ✔ Programación Orientada a Objetos
#  ✔ Clase Abstracta
#  ✔ Herencia
#  ✔ Polimorfismo
#  ✔ Encapsulamiento
#  ✔ Métodos sobrescritos
#  ✔ Comentarios explicativos
# =========================================================

# ---------------- IMPORTACIONES ----------------

import time
import random
from abc import ABC, abstractmethod


# =========================================================
#                 CLASE ABSTRACTA BASE
# =========================================================

class Personaje(ABC):
    """
    Clase abstracta que representa un personaje del juego.
    Todas las clases hijas deben implementar el método atacar().
    """

    def __init__(self, nombre, vida, ataque, defensa):

        # Atributos públicos
        self.nombre = nombre

        # Atributos encapsulados (privados)
        self.__vida = 0
        self.__ataque = ataque
        self.__defensa = defensa
        self.__defendiendo = False

        # Validamos la vida usando el setter
        self.set_vida(vida)

    # =====================================================
    # MÉTODO ABSTRACTO
    # =====================================================

    @abstractmethod
    def atacar(self, objetivo):
        """
        Método abstracto.
        Cada personaje atacará de manera diferente.
        """
        pass

    # =====================================================
    # MÉTODOS GENERALES
    # =====================================================

    def presentarse(self):
        """Presentación básica del personaje"""
        print(f"{self.nombre} entra en batalla.")

    # =====================================================
    # GETTERS (ENCAPSULAMIENTO)
    # =====================================================

    def get_vida(self):
        return self.__vida

    def get_ataque(self):
        return self.__ataque

    def get_defensa(self):
        return self.__defensa

    # =====================================================
    # SETTERS
    # =====================================================

    def set_vida(self, valor):
        """
        Controla que la vida nunca sea menor que 0
        ni mayor que 100.
        """

        if valor < 0:
            self.__vida = 0

        elif valor > 100:
            self.__vida = 100

        else:
            self.__vida = valor

    # =====================================================
    # SISTEMA DE DEFENSA
    # =====================================================

    def defender(self):
        """
        Activa el modo defensa.
        El siguiente daño recibido será reducido.
        """

        self.__defendiendo = True
        print(f"🛡️ {self.nombre} se pone en posición defensiva.")

    def recibir_danio(self, danio):
        """
        Reduce vida según el daño recibido.
        Si está defendiendo, recibe menos daño.
        """

        if self.__defendiendo:
            danio *= 0.5
            print(f"🛡️ {self.nombre} reduce el daño a {danio:.1f}")

        # Restamos la vida
        self.set_vida(self.get_vida() - danio)

        # La defensa solo dura un turno
        self.__defendiendo = False

    # =====================================================
    # MÉTODO ESPECIAL
    # =====================================================

    def __str__(self):
        """
        Representación del objeto al imprimirlo.
        """
        return f"{self.nombre} | Vida: {self.__vida}"


# =========================================================
#                    CLASE GUERRERO
# =========================================================

class Guerrero(Personaje):
    """
    Clase hija que hereda de Personaje.
    Especialista en fuerza física.
    """

    def __init__(self, nombre):
        super().__init__(nombre, 100, 30, 20)

    # Polimorfismo
    def atacar(self, objetivo):

        # Daño aumentado en 20%
        danio = (self.get_ataque() * 1.2) - objetivo.get_defensa()

        # Evita daños negativos
        danio = max(0, danio)

        print(f"⚔️ {self.nombre} golpea con su espada.")
        print(f"Daño realizado: {danio:.1f}")

        objetivo.recibir_danio(danio)

    # Sobrescritura de método
    def presentarse(self):
        print(f"⚔️ {self.nombre}: '¡Mi espada jamás cae!' ")


# =========================================================
#                      CLASE MAGO
# =========================================================

class Mago(Personaje):
    """
    Clase hija especializada en magia.
    """

    def __init__(self, nombre):
        super().__init__(nombre, 80, 40, 10)

    # Polimorfismo
    def atacar(self, objetivo):

        # El mago ignora defensa parcialmente
        danio = self.get_ataque()

        print(f"🔥 {self.nombre} lanza un hechizo.")
        print(f"Daño mágico: {danio}")

        objetivo.recibir_danio(danio)

    def presentarse(self):
        print(f"🔥 {self.nombre}: 'La magia será tu final.'")


# =========================================================
#                    CLASE ARQUERO
# =========================================================

class Arquero(Personaje):
    """
    Clase hija especializada en ataques críticos.
    """

    def __init__(self, nombre):
        super().__init__(nombre, 90, 35, 15)

    # Polimorfismo
    def atacar(self, objetivo):

        # Posibilidad de golpe crítico
        if self.get_ataque() > objetivo.get_defensa():
            danio = self.get_ataque() * 2
            print("🎯 ¡Golpe crítico!")

        else:
            danio = self.get_ataque() - objetivo.get_defensa()

        danio = max(0, danio)

        print(f"🏹 {self.nombre} dispara una flecha.")
        print(f"Daño realizado: {danio}")

        objetivo.recibir_danio(danio)

    def presentarse(self):
        print(f"🏹 {self.nombre}: 'Nunca verás venir mi flecha.'")


# =========================================================
#                         LORE
# =========================================================

def mostrar_lore():

    print("\n📜 ===== GUARDIANS OF THE ANCIENT KINGDOM ===== 📜\n")

    print("En un reino olvidado existen tres órdenes legendarias:\n")

    print("⚔️ Guerreros -> Dominan la fuerza física.")
    print("🔥 Magos -> Controlan el poder arcano.")
    print("🏹 Arqueros -> Expertos en precisión letal.")

    print("\nDos campeones lucharán...")
    print("Solo uno sobrevivirá.\n")

    input("Presiona ENTER para continuar...")


# =========================================================
#                    CREACIÓN DE PERSONAJES
# =========================================================

def menu_creacion(num_jugador):

    print(f"\n=========== JUGADOR {num_jugador} ===========")

    nombre = input("Nombre del personaje: ")

    print("\nSelecciona una clase:")
    print("1. Guerrero")
    print("2. Mago")
    print("3. Arquero")

    opcion = input("Opción: ")

    # Selección de personaje
    if opcion == "1":
        personaje = Guerrero(nombre)

    elif opcion == "2":
        personaje = Mago(nombre)

    else:
        personaje = Arquero(nombre)

    personaje.presentarse()

    return personaje


# =========================================================
#                        TURNOS
# =========================================================

def turno(jugador, enemigo):

    print(f"\n===== Turno de {jugador.nombre} =====")

    print("1. Atacar")
    print("2. Defender")

    opcion = input("¿Qué deseas hacer?: ")

    if opcion == "1":
        jugador.atacar(enemigo)

    elif opcion == "2":
        jugador.defender()

    else:
        print("❌ Opción inválida. Pierdes el turno.")


# =========================================================
#                     MENSAJE FINAL
# =========================================================

def mensaje_victoria(ganador):

    if isinstance(ganador, Guerrero):

        frases = [
            "⚔️ La fuerza siempre triunfa.",
            "⚔️ Victoria digna de un verdadero guerrero.",
            "⚔️ Su espada decidió el destino."
        ]

    elif isinstance(ganador, Mago):

        frases = [
            "🔥 La magia dominó el combate.",
            "🔥 El poder arcano fue imparable.",
            "🔥 Un hechizo selló la victoria."
        ]

    else:

        frases = [
            "🏹 Precisión perfecta.",
            "🏹 Una flecha bastó para ganar.",
            "🏹 Nadie escapa del arquero."
        ]

    print(random.choice(frases))


# =========================================================
#                        BATALLA
# =========================================================

def iniciar_batalla(p1, p2):

    print("\n🔥 ===== INICIA LA BATALLA ===== 🔥")

    # Bucle principal del juego
    while p1.get_vida() > 0 and p2.get_vida() > 0:

        # Turno jugador 1
        turno(p1, p2)

        # Verificamos si perdió jugador 2
        if p2.get_vida() <= 0:
            break

        # Turno jugador 2
        turno(p2, p1)

        # Verificamos si perdió jugador 1
        if p1.get_vida() <= 0:
            break

        # Mostrar estado actual
        print("\n📊 ESTADO ACTUAL")
        print(p1)
        print(p2)

        # Pausa visual
        time.sleep(1)

    # Determinar ganador
    ganador = p1 if p1.get_vida() > 0 else p2
    perdedor = p2 if ganador == p1 else p1

    print(f"\n🏆 {ganador.nombre} ha derrotado a {perdedor.nombre}")

    mensaje_victoria(ganador)


# =========================================================
#                   PROGRAMA PRINCIPAL
# =========================================================

if __name__ == "__main__":

    # Mostrar historia
    mostrar_lore()

    # Crear jugadores
    jugador1 = menu_creacion(1)
    jugador2 = menu_creacion(2)

    # Iniciar combate
    iniciar_batalla(jugador1, jugador2)