import random
file = open('WordsStockRus.txt', 'r', encoding='utf-8')
words = []
for word1 in file:
    words.append(word1[:-1])
def start_playing():
    class Game:
        def __init__(self,mis_left):
            self.mist_left = mis_left
            self.shown_word = ''
            self.let_used = []
            self.word = ''
            self.wword = ''
            self.continue_game = '+'
        def generate_word(self):
            random_int = random.randint(0,len(words)-1)
            length = len(words[random_int])
            self.shown_word = '_' * length
            self.word = words[random_int]
            self.wword = words[random_int]
            return self.word
        def mistake_amount(self):
            self.mist_left = mis_left

        def make_guess(self,letter):
            if letter in self.let_used:
                print(f'Данная буква уже была использована')
            else:
                if self.word.find(letter) != -1:
                    am = self.word.count(letter)
                    for i in range (am):
                        if self.word.find(letter) == 0:
                            self.shown_word = letter + self.shown_word[1:len(self.word)]
                            self.word = '_' + self.word[1:len(self.word)]
                        else:
                            self.shown_word = self.shown_word[:self.word.find(letter)] + letter + self.shown_word[self.word.find(letter)+1:len(self.word)]
                            self.word = self.word[:self.word.find(letter)] + '_' + self.word[self.word.find(letter)+1:len(self.word)]
                    self.let_used.append(letter)
                    print(f'Вы угадали букву:{self.shown_word}')
                elif self.word.find(letter) == -1:
                    if self.mist_left == 1:
                        self.mist_left -= 1
                        self.continue_game = input(f'Вы умерли. Искомое слово: {self.wword}. Хотите продолжить игру? (+,-): ')
                        return self.mist_left
                    else:
                        self.mist_left -= 1
                    print(f'Такой буквы в слове нет, осталось {self.mist_left} допустимых ошибок')
                    self.let_used.append(letter)
    game1 = Game(1)
    while game1.continue_game == '+':
        game1 = Game(int(input('Сколько попыток ошибиться?: ')))
        game1.generate_word()
        print(game1.shown_word)
        while (game1.shown_word.count('_') > 0) and (game1.mist_left != 0):
            game1.make_guess(input('Введите букву: '))
start_playing()














