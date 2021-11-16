
import threading

# def tarefa_1():
#     for i in range(10):
#         print('Hello World!')
#     return

# def tarefa_2():
#     for j in range(10):
#         print('Olá Mundo!')
#     return


# threading.Thread(target=tarefa_1).start()
# tarefa_2()


def funcao():
    x = True
    return x


while True:

    if funcao() == False:
        print('Deu certo')
        break
    else:
        print('deu errado')
        break

threading.Thread(target=funcao).start()