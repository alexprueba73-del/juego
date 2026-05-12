# # ⚔️ GUARDIANS OF THE ANCIENT KINGDOM

Juego de batalla por turnos desarrollado en Python utilizando Programación Orientada a Objetos (POO).

---

# 📖 Descripción

**Guardians of the Ancient Kingdom** es un juego de combate por turnos donde dos jugadores eligen diferentes clases de personajes y luchan hasta que uno sea derrotado.

El proyecto fue diseñado para practicar y demostrar conceptos fundamentales de:

* Programación Orientada a Objetos
* Herencia
* Polimorfismo
* Encapsulamiento
* Clases Abstractas
* Sobrescritura de métodos

---

# 🎮 Características

✔ Sistema de combate por turnos
✔ Tres clases jugables
✔ Ataques especiales según la clase
✔ Sistema de defensa
✔ Mensajes dinámicos de victoria
✔ Arquitectura escalable
✔ Código organizado y comentado

---

# 🧙 Clases Disponibles

## ⚔️ Guerrero

Especialista en fuerza física.

* Vida alta
* Defensa elevada
* Ataques cuerpo a cuerpo con daño aumentado

---

## 🔥 Mago

Especialista en magia arcana.

* Ataques mágicos poderosos
* Ignora parcialmente la defensa enemiga
* Vida menor pero gran daño

---

## 🏹 Arquero

Experto en precisión y golpes críticos.

* Ataques rápidos
* Posibilidad de daño crítico
* Balance entre ataque y defensa

---

# 🛠️ Tecnologías utilizadas

* Python 3
* Programación Orientada a Objetos
* Módulos estándar:

  * `random`
  * `time`
  * `abc`

---

# 📂 Estructura del Proyecto

```bash
GuardiansOfTheAncientKingdom/
│
├── main.py
└── README.md
```

---

# ▶️ Cómo ejecutar el juego

## 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/guardians-of-the-ancient-kingdom.git
```

## 2. Entrar en la carpeta

```bash
cd guardians-of-the-ancient-kingdom
```

## 3. Ejecutar el juego

```bash
python main.py
```

---

# 🧠 Conceptos de POO implementados

## ✅ Clase Abstracta

La clase `Personaje` funciona como base abstracta para todos los personajes.

```python
class Personaje(ABC):
```

---

## ✅ Herencia

Las clases `Guerrero`, `Mago` y `Arquero` heredan de `Personaje`.

---

## ✅ Polimorfismo

Cada clase implementa su propia versión del método:

```python
def atacar(self, objetivo):
```

---

## ✅ Encapsulamiento

Los atributos privados están protegidos mediante getters y setters.

```python
self.__vida
```

---

## ✅ Sobrescritura de métodos

Cada personaje redefine el método:

```python
def presentarse(self):
```

---

# 🚀 Posibles mejoras futuras

* Sistema de niveles
* Inventario
* Objetos y equipamiento
* IA enemiga
* Guardado de partidas
* Efectos de estado
* Habilidades especiales
* Interfaz gráfica con Pygame
* Modo historia

---

# 📸 Ejemplo de partida

```bash
===== GUARDIANS OF THE ANCIENT KINGDOM =====

Jugador 1 elige Guerrero
Jugador 2 elige Mago

===== INICIA LA BATALLA =====

⚔️ Arthur golpea con su espada.
Daño realizado: 26

🔥 Merlin lanza un hechizo.
Daño mágico: 40
```

---

# 👨‍💻 Autor

Proyecto desarrollado como práctica de Programación Orientada a Objetos en Python.

---

# 📜 Licencia

Este proyecto es de uso libre para fines educativos y personales.
