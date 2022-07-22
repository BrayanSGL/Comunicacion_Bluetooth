from msilib import sequence


sequence_example = '@D185S4I10V50D2#'
motor_state = 'stop'


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
            print(letter, value)


def unpacking(raw_sequence):
    sequence = ''
    if(raw_sequence.count('@') == 1) and (raw_sequence.count('#') == 1):
        sequence = raw_sequence.strip("@#")
    return sequence


sequence = unpacking(sequence_example)
if check(sequence):
    analysis(sequence)
