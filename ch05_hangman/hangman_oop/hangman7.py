import random
from hangman_arts import *
#hangmang_arts 파일의 전체 데이터를 가지고 오겠다는 의미

from hangman_word_list import word_list
# hangman_word_list 파일 내에서 word_list 변수만 가지고 오겠다는 의미

print(logo)

# 이상과 같이 작성한 것을 기준으로 hangman을 완성하시오.

display = []
chosen_word = random.choice(word_list)

print(f'테스트 단어 : {chosen_word}')

for i in range(len(chosen_word)):
    display.append('_')

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
        # print(stages[live])
        print(f'기회가 {live}번 남았습니다.')
        if live == 0:
            print(f'모든 기회를 잃었습니다.')
            end_of_game = True
            print(stages[live])
            print(f'정답은 {chosen_word}입니다.')

    if '_' not in display:
        print(f'정답입니다')
        end_of_game = True

    print(' '.join(display))

print('게임 종료')

