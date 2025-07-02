# 🪨 Piedra, 📄 Papel o ✂️ Tijera - Juego en Python  
**Por: Daniel Ilbay Yupa**

¡Bienvenido/a al clásico juego de Piedra, Papel o Tijera implementado en Python para consola!  
Este proyecto fue desarrollado como una práctica divertida para reforzar habilidades de lógica de programación y control de flujo con Python.

---

## 🎯 Objetivo del Proyecto

Desarrollar una aplicación interactiva mediante consola que permita jugar el clásico juego “Piedra, Papel o Tijera” en modo individual o multijugador.  
El sistema debía incorporar una estructura modular, validación de entradas, estadísticas automáticas y una experiencia amigable, utilizando programación estructurada en Python.

---

## 🎮 Descripción General

Este juego ofrece una interfaz clara y amigable para jugar de manera interactiva desde la terminal.  
Al finalizar cada set de partidas, se muestra un resumen con estadísticas y resultados.

---

## 🕹️ Modos de Juego

- **Modo 1: Contra la Computadora**  
  El jugador compite contra un oponente automatizado que selecciona jugadas aleatoriamente.

- **Modo 2: Multijugador (2 jugadores)**  
  Dos jugadores ingresan sus jugadas de forma independiente desde teclado.

- **Opción de Partidas Definidas**  
  Los jugadores pueden establecer cuántas rondas jugar o continuar indefinidamente.

---

## 📊 Estadísticas del Juego

Al finalizar cada juego, el sistema presenta:

- Número total de partidas jugadas.
- Resultado detallado por partida.
- Estadísticas por jugador:
  - Partidas ganadas
  - Partidas perdidas
  - Partidas empatadas

---

## 📜 Reglas del Juego

- 🪨 **Piedra aplasta a** ✂️ **Tijera**
- ✂️ **Tijera corta a** 📄 **Papel**
- 📄 **Papel envuelve a** 🪨 **Piedra**

🔁 Si ambos jugadores eligen la misma opción, la ronda termina en empate.  
⚠️ Solo se permiten entradas válidas: `1` (Piedra), `2` (Papel), `3` (Tijera).  
🏆 Gana quien acumule más victorias al final del set de partidas.

---

## 🎯 Conclusiones del Proyecto
El desarrollo de este proyecto permitió alcanzar satisfactoriamente los objetivos planteados, ya que se implementó un juego completamente funcional e interactivo que refuerza conceptos fundamentales de programación como estructuras condicionales, ciclos, validación de datos y modularidad. La aplicación ofrece una experiencia amigable desde consola, con retroalimentación clara y estadísticas automáticas, lo que demuestra cómo los fundamentos de Python pueden aplicarse para crear sistemas dinámicos. Además, este trabajo sienta las bases para futuras mejoras como la incorporación de una interfaz gráfica, niveles de dificultad o inteligencia artificial básica que mejore la experiencia del jugador.

---

## ▶️ ¿Cómo usar el juego?

1. Asegúrate de tener Python 3 instalado.
2. Descarga o clona este repositorio.
3. Abre la terminal en la carpeta del proyecto.
4. Ejecuta el archivo principal con:

```bash
python main_ppt_v2.py
