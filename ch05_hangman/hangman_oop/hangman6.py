import random
import hangman_arts
import hangman_word_list

# import 다음에 파일명을 썼다는 것에 주목해야합니다. 이 파일 하나를 파이썬에서는 module(모듈)이라고 합니다.

# 외부의 hangman_word_list 변수를 참조해서 chosen_word를 만들 필요가 있습니다

print(hangman_arts.logo)
# 위에가 힌트. 그러면 chosen_word를 불러올 수 있도록 코드를 작성하시오.

display = []
chosen_word = random.choice(hangman_word_list.word_list)

print(f'테스트 단어 : {chosen_word}')

for i in range(len(chosen_word)):
    display.append('_')

end_of_game = False
live = 6
while not end_of_game:
    print(hangman_arts.stages[live])
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
            print(hangman_arts.stages[live])
            print(f'정답은 {chosen_word}입니다.')
            
    if '_' not in display:
        print(f'정답입니다')
        end_of_game = True

    print(' '.join(display))

print('게임 종료')