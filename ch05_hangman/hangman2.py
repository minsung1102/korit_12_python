import random

word_list = [ 'apple', 'banana', 'camel']
choice_word = random.choice(word_list)
print(f'테스트 단어 : {choice_word}')

#todo - 1 : 비어있는 list인 display를 만드시오,
display = []
# list에 element를 추가하는 메서드 : .append()
# display.append('김')
# display.append('영')
# print(display)
# display[1] = 1
# print(display)
# display[4] = 4
# print(display)
#todo - 2 : 이상의 코드 라인을 참조하여 chosen_word의 각 문자 개수마다 '_' 를 추가하시오. 예를 들어 chosen_word == 'apple'이라면 display = [ '_', '_', '_', '_', '_']로 만들어져야합니다.
# for i in range(len(choice_word)):
#     display.append('_')
# print(display)

#todo - 3 : chosen_word의 각 문자들을 반복시켰을 때 그 위치가 guess와 일치한다면 해당 위치의 display에 문자를 공개합니다. 예를 들어 chosen_word가 apple이고 guess == 'p'라면 display = [ '_','p','p', '_','_']로 바뀌어야 합니다.

# 특정 index에 있는 '_'를 guess로 대입해줘야 합니다.
# chosen_word[i]가 guess와 일치한다면 display[i]('_'겠죠)를 guess로 재대입해줘야 합니다.
guess = input("단어를 입력해주세요 >>> ")

for i in range(len(choice_word)):
    display.append('_')
    if guess == choice_word[i]: # // 일치한다면 해당하는 ==
        display[i] = guess      # 재대입하라는 =
print(display)

