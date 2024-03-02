from enum import Enum

class Game:
    def __init__(self, player1, player2):
        self.allSpaces = list('123456789')
        self.board = {}
        self.player1 = player1
        self.player2 = player2
        for space in self.allSpaces:
            self.board[space] = Mark.BLANK.value
    def isValidSpace(self, space):
        if space is None:
            return False
        return space in self.allSpaces or self.getBoardSpace(space) == Mark.BLANK.value

    def play(self):
        currentPlayer, nextPlayer = Mark.X.value, Mark.O.value
        while True:
            print(self.getBoardStr())  # Wyświetl planszę na ekranie.

            # Zadawaj graczowi pytanie, aż wprowadzi prawidłową liczbę od 1 do 9:
            move = None
            while not self.isValidSpace(move):
                print(f'Jaki jest ruch gracza {currentPlayer}? (1-9)')
                move = input()
            self.updateBoard(move, currentPlayer)  # Wykonanie ruchu.
            # Sprawdzenie, czy gra jest zakończona:
            if self.isWinner(currentPlayer):  # Sprawdzenie, kto wygrał.
                print(self.getBoardStr())
                print(currentPlayer + ' wygrał grę!')
                break
            elif self.isBoardFull(self.allSpaces):  # Sprawdzenie remisu.
                print(self.getBoardStr())
                print('Gra zakończyła się remisem!')
                break
            currentPlayer, nextPlayer = nextPlayer, currentPlayer  # Zmiana gracza.
        print('Dziękuję za grę!')

    def isWinner(self, player):
         """Zwraca True, jeśli gracz jest zwycięzcą tej planszy KIK."""
         b, p = self.board, player  # Krótsze nazwy jako "składniowy cukier".
         # Sprawdzenie, czy trzy takie same znaki występują w wierszach, kolumnach i po przekątnych.
         return ((b['1'] == b['2'] == b['3'] == p) or  # poziomo na górze
                (b['4'] == b['5'] == b['6'] == p) or  # poziomo w środku
                 (b['7'] == b['8'] == b['9'] == p) or  # poziomo u dołu
                 (b['1'] == b['4'] == b['7'] == p) or  # pionowo z lewej
                 (b['2'] == b['5'] == b['8'] == p) or  # pionowo w środku
                 (b['3'] == b['6'] == b['9'] == p) or  # pionowo z prawej
                 (b['3'] == b['5'] == b['7'] == p) or  # przekątna 1
                 (b['1'] == b['5'] == b['9'] == p))  # przekątna 2

    def getBoardStr(self):
        return f'''
                {self.board['1']}|{self.board['2']}|{self.board['3']} 1 2 3 
                -+-+- 
                {self.board['4']}|{self.board['5']}|{self.board['6']} 4 5 6 
                -+-+- 
                {self.board['7']}|{self.board['8']}|{self.board['9']} 7 8 9'''

    def getBoardSpace(self, space):
        return self.board[space]

    def updateBoard(self, space, mark):
        self.board[space] = mark

    def isBoardFull(self, allSpaces):
        """Zwraca True, jeśli wszystkie pola na planszy są zajęte."""
        for space in allSpaces:
            if self.board[space] == Mark.BLANK.value:
                return False  # Jeśli nawet jedno pole jest puste, zwracaj False.
        return True  # Nie ma wolnych pól, zatem zwróć True.

class Player:
    def __init__(self, name):
        self.name = name


class Mark(Enum):
    X = 'X'
    O = 'O'
    BLANK = ' '


player1 = Player("Jan")
player2 = Player("Adam")
game = Game(player1, player2)

game.play()
