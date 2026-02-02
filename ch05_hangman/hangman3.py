# 초기 설정은 여러분들이 하겠습니다 -> random / word_list / display
import random
word_list = [ 'apple', 'banana', 'camel' ]
display = []
chosen_word = random.choice(word_list)

print(f'테스트 단어 : {chosen_word}')

for i in range(len(chosen_word)):
    display.append('_')
print(display)

'''
''.join(반복가능객체) method : '.' 앞에 있는 문자열을 기준으로 반복 가능 객체의 element들을 합쳐서 str로 만들어주는 method
'''

# temp = ['s', 'q', 'l', 'd']
# test = ''.join(temp)
# print(test)
# test = ' '.join(temp)
# print(test)
# test = '  '.join(temp)
#todo - 1 : 사용자가 추측을 반복할 수 있도록 while 반복문을 작성하시오. 사용자가 chosen_word의 모든 문자열들을 맞추었을 때, 즉 display에 '_'가 없을때 반복문을 중단시킬겁니다. 반복문 종료 후 '정답입니다 !!'를 출력하도록

# todo - 2 : 정답을 보여줄 때 apple이라면 a p p l e로 출력될 수 있도록 .join() 메서드를 활용하시오.


# 1
# while '_' in display:
# 2
while ''.join(display) != chosen_word:
    guess = input('단어를 입력해 주세요 >>> ').lower()
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    print(' '.join(display))
print('정답입니다')
        























