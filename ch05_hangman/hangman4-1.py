import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = [ 'apple', 'banana', 'camel' ]
display = []
chosen_word = random.choice(word_list)

print(f'테스트 단어 : {chosen_word}')

for i in range(len(chosen_word)):
    display.append('_')
# todo - 1 : 남은 기회 숫자를 추적하기 위한 lives 변수를 선언하고 6으로 초기화하세요.

# todo - 2 : while문의 조건을 수정하여 6 번의 기회가 소진되면 반복문이 종료 될 수 있도록 조건을 작성하시오.

end_of_game = False
live = 6
while not end_of_game:
    print(stages[live])
    guess = input('단어를 입력해 주세요 >>> ').lower()
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
            print(f'기회가 {live}번 남았습니다.')

    if guess not in chosen_word:
        live -= 1
        # print(stages[live])      # 틀렸을 때만 그림이 나온다는 점이 문제
        print(f'기회가 {live}번 남았습니다.')
        if live == 0:
            print(f'모든 기회를 잃었습니다.')
            end_of_game = True
            print(stages[live])
            print(f'정답은 {chosen_word}입니다.')
        # 다 맞췄을 때도 end_of_game = True가 되어야 하기 때문에 별개의 조건문
    if '_' not in display:  # 다 맞췄다는 것을 의미
        print(f'정답입니다')
        end_of_game = True

    print(' '.join(display))

print('게임 종료')




