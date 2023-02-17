'''
dibujar vidas
'''
AHORCADO = ['''
                  +---+
                  |   |
                      |
                      |
                      |
                      |
                =========''', '''
                  +---+
                  |   |
                  O   |
                      |
                      |
                      |
                =========''', '''
                  +---+
                  |   |
                  O   |
                  |   |
                      |
                      |
                =========''', '''
                  +---+
                  |   |
                  O   |
                 /|   |
                      |
                      |
                =========''', '''
                  +---+
                  |   |
                  O   |
                 /|\  |
                      |
                      |
                =========''', '''
                  +---+
                  |   |
                  O   |
                 /|\  |
                 /    |
                      |
                =========''', '''
                  +---+
                  |   |
                  O   |
                 /|\  |
                 / \  |
                      |
                =========''']

def vidas(vidas):
      return AHORCADO[len(AHORCADO)-vidas-1]

def main():
    for i in range(len(AHORCADO)):
        print(AHORCADO[i])
        input()
if __name__ == "__main__":
    main()