# Control de motor con Raspberry Pi
Este código es un script de Python que permite controlar un motor a través de la placa de desarrollo Raspberry Pi utilizando comandos enviados a través de una conexión Bluetooth.

## Requisitos
Para utilizar este código es necesario tener lo siguiente:

- Una placa Raspberry Pi conectada a un motor
- Un dispositivo externo conectado a la Raspberry Pi a través de Bluetooth
## Instalación
Para utilizar este código, es necesario tener instaladas las siguientes librerías:

- RPi.GPIO
- bluedot

Puedes instalar estas librerías utilizando el administrador de paquetes de Python, pip, de la siguiente manera:

```
pip install RPi.GPIO
pip install bluedot
```

## Uso
Para utilizar este código, debes seguir los siguientes pasos:

Establecer una conexión Bluetooth entre la Raspberry Pi y el dispositivo externo.
Ejecutar el script en la Raspberry Pi.
Enviar comandos a través de la conexión Bluetooth para controlar el motor.
Los comandos que puedes utilizar son:

- 'D' para girar el motor hacia la derecha.
- 'I' para girar el motor hacia la izquierda.
- 'S' para detener el motor.
- 'V' para cambiar la velocidad del motor.
Cada comando puede ir seguido de un número que indica el tiempo en segundos que durará la acción. Por ejemplo, para girar el motor hacia la derecha durante 5 segundos, debes enviar el comando 'D5'.

El código incluye una función 'check' que valida si el comando enviado es válido y notifica al usuario en caso de que no lo sea. Los posibles errores que pueden ser detectados son: letras no reconocidas, secuencias que terminan en una letra o comienzan con un número, comandos juntos o sin número, velocidades inválidas y tiempos inválidos.

## Ejemplo
Para girar el motor hacia la derecha durante 5 segundos a una velocidad del 50%, envía el siguiente comando a través de la conexión Bluetooth:

```
V50D5
```
