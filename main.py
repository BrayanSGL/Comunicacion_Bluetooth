import RPi.GPIO as GPIO
import time
from bluedot.btcomm import BluetoothServer
from signal import pause

IN1 = 11
IN2 = 13
PWM = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(PWM, GPIO.OUT)
GPIO.setwarnings(False)

pwm = GPIO.PWM(PWM, 1000)
pwm.start(0)


def run(letter, value):
    print('entré', letter, value)

    pass


def check(sequence):
    result = True
    first_test = True
    second_test = True
    third_test = True

    # 1ra. letras correctas
    for i in range(0, len(sequence)):
        if not sequence[i].isdigit():
            if sequence[i] == 'D':
                first_test = True
            elif sequence[i] == 'I':
                first_test = True
            elif sequence[i] == 'V':
                first_test = True
            elif sequence[i] == 'S':
                first_test = True
            else:
                first_test = False
                print('Error #1: "Letra no reconocida"')
                break

    # 2da. final con letra o inicio con número
    end_char = sequence[len(sequence)-1:]
    start_char = sequence[:1]
    if not end_char.isdigit() or start_char.isdigit():
        second_test = False
        print('Error #2: "Secuencia con letra al final o número al principio"')

    # 3ra. comandos juntos o sin número
    for i in range(0, len(sequence)):
        if not sequence[i-1].isdigit() and not sequence[i].isdigit():
            third_test = False
            print('Error #3: "Comandos juntos o sin número"')
            break

    # Resultado final
    if not (first_test and second_test and third_test):
        result = False

    return result


def analysis(sequence):
    for i in range(0, len(sequence)):
        if not sequence[i].isdigit():
            letter = sequence[i]
            new_sequence = sequence[i+1:]
            for j in range(0, len(new_sequence)):
                if not new_sequence[j].isdigit():
                    value = new_sequence[:j]
                    break
                if new_sequence.isdigit():
                    value = int(new_sequence)
            # Metodo del motor
            run(letter, value)


def unpacking(raw_sequence):
    sequence = ''
    if(raw_sequence.count('@') == 1) and (raw_sequence.count('#') == 1):
        sequence = raw_sequence.strip("@#")
    return sequence


def read(data):
    data = data.strip()
    #length_data = len(data)
    #print(data, str(length_data))
    sequence = unpacking(data)
    if sequence == 'R':
        pwm.ChangeDutyCycle(50)
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        server.send('Estado: Derecha')

    elif sequence == 'L':
        pwm.ChangeDutyCycle(50)
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        server.send('Estado: Izquierda')

    elif sequence == 'S':
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
        server.send('Estado: Detenido')

    elif check(sequence):
        analysis(sequence)

    '''if data == 'A':
        print('llegó una A')
    elif data == 'B':
        print('llegó una B')
    else:
        print('Llegó otra cosa')
        server.send('Hola bebé')'''


print('initializing server')

server = BluetoothServer(read)

pause()
