from bluedot.btcomm import BluetoothServer
from signal import pause


def read(data):
    data = data.strip()
    length_data = len(data)
    print(data, str(length_data))

    if data == 'A':
        print('llegó una A')
    elif data == 'B':
        print('llegó una B')
    else:
        print('Llegó otra cosa')
        server.send('Hola bebé')


print('initializing server')

server = BluetoothServer(read)

pause()
