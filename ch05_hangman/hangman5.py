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

logo = '''
                                                                                      
                                                                                      
  ,---,                                                 ____                          
,--.' |                                               ,'  , `.                        
|  |  :                      ,---,                 ,-+-,.' _ |                 ,---,  
:  :  :                  ,-+-. /  |  ,----._,.  ,-+-. ;   , ||             ,-+-. /  | 
:  |  |,--.  ,--.--.    ,--.'|'   | /   /  ' / ,--.'|'   |  || ,--.--.    ,--.'|'   | 
|  :  '   | /       \  |   |  ,"' ||   :     ||   |  ,', |  |,/       \  |   |  ,"' | 
|  |   /' :.--.  .-. | |   | /  | ||   | .\  .|   | /  | |--'.--.  .-. | |   | /  | | 
'  :  | | | \__\/: . . |   | |  | |.   ; ';  ||   : |  | ,    \__\/: . . |   | |  | | 
|  |  ' | : ," .--.; | |   | |  |/ '   .   . ||   : |  |/     ," .--.; | |   | |  |/  
|  :  :_:,'/  /  ,.  | |   | |--'   `---`-'| ||   | |`-'     /  /  ,.  | |   | |--'   
|  | ,'   ;  :   .'   \|   |/       .'__/\_: ||   ;/        ;  :   .'   \|   |/       
`--''     |  ,     .-./'---'        |   :    :'---'         |  ,     .-./'---'        
           `--`---'                  \   \  /                `--`---'                 
                                      `--`-'                                          '''
print(logo)

word_list = [ 'apple', 'banana', 'orange', 'grape', 'lemon', 'lime', 'cherry', 'peach', 'pear', 'plum', 'dog', 'cat', 'bird', 'fish', 'horse', 'cow', 'pig', 'sheep', 'goat', 'chicken', 'table', 'chair', 'desk', 'bed', 'sofa', 'lamp', 'clock', 'door', 'window', 'floor', 'book', 'pen', 'pencil', 'paper', 'notebook', 'ruler', 'eraser', 'bag', 'box', 'shelf', 'car', 'bus', 'train', 'plane', 'ship', 'bike', 'truck', 'taxi', 'subway', 'scooter', 'sun', 'moon', 'star', 'sky', 'cloud', 'rain', 'snow', 'wind', 'storm', 'rainbow', 'red', 'blue', 'green', 'yellow', 'black', 'white', 'pink', 'purple', 'brown', 'gray', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'big', 'small', 'tall', 'short', 'long', 'wide', 'narrow', 'fast', 'slow', 'heavy', 'happy', 'sad', 'angry', 'tired', 'hungry', 'thirsty', 'hot', 'cold', 'warm', 'cool', 'teacher', 'student', 'class', 'school', 'lesson', 'homework', 'exam', 'test', 'grade', 'subject', 'math', 'science', 'history', 'art', 'music', 'sport', 'English', 'Korean', 'computer', 'library', 'family', 'father', 'mother', 'brother', 'sister', 'uncle', 'aunt', 'cousin', 'baby', 'child', 'home', 'house', 'room', 'kitchen', 'bathroom', 'garden', 'yard', 'garage', 'balcony', 'roof', 'food', 'rice', 'bread', 'meat', 'fish', 'egg', 'milk', 'cheese', 'butter', 'soup', 'drink', 'water', 'juice', 'tea', 'coffee', 'soda', 'beer', 'wine', 'sugar', 'salt', 'shirt', 'pants', 'dress', 'skirt', 'shoes', 'socks', 'hat', 'coat', 'jacket', 'sweater', 'body', 'head', 'face', 'eye', 'ear', 'nose', 'mouth', 'hand', 'leg', 'foot', 'color', 'shape', 'circle', 'square', 'triangle', 'line', 'point', 'edge', 'corner', 'side', 'day', 'night', 'morning', 'evening', 'noon', 'today', 'tomorrow', 'yesterday', 'week', 'month', 'go', 'come', 'walk', 'run', 'jump', 'sit', 'stand', 'lie', 'sleep', 'wake', 'eat', 'drink', 'cook', 'bake', 'cut', 'open', 'close', 'read', 'write', 'draw', 'play', 'sing', 'dance', 'swim', 'climb', 'ride', 'drive', 'fly', 'watch', 'listen', 'talk', 'speak', 'say', 'tell', 'ask', 'answer', 'shout', 'call', 'laugh', 'cry', 'make', 'do', 'build', 'break', 'fix', 'clean', 'wash', 'paint', 'move', 'carry', 'buy', 'sell', 'pay', 'cost', 'spend', 'save', 'borrow', 'lend', 'give', 'take', 'love', 'like', 'hate', 'want', 'need', 'hope', 'wish', 'try', 'help', 'use', 'start', 'stop', 'begin', 'end', 'finish', 'continue', 'change', 'stay', 'wait', 'leave', 'work', 'study', 'learn', 'teach', 'train', 'practice', 'play', 'win', 'lose', 'draw', 'think', 'know', 'remember', 'forget', 'understand', 'believe', 'guess', 'choose', 'decide', 'plan', 'city', 'town', 'village', 'country', 'nation', 'world', 'earth', 'land', 'sea', 'ocean', 'mountain', 'hill', 'river', 'lake', 'forest', 'desert', 'island', 'beach', 'valley', 'cave', 'animal', 'plant', 'tree', 'flower', 'grass', 'leaf', 'root', 'seed', 'fruit', 'vegetable', 'machine', 'tool', 'phone', 'computer', 'camera', 'radio', 'TV', 'internet', 'robot', 'engine', 'money', 'coin', 'card', 'bank', 'shop', 'market', 'store', 'price', 'sale', 'cash', 'friend', 'enemy', 'neighbor', 'stranger', 'guest', 'host', 'partner', 'team', 'group', 'crowd', 'idea', 'fact', 'truth', 'lie', 'dream', 'story', 'word', 'sentence', 'question', 'answer', 'music', 'song', 'sound', 'voice', 'noise', 'art', 'picture', 'photo', 'film', 'drama', 'game', 'health', 'doctor', 'nurse', 'hospital', 'medicine', 'disease', 'pain', 'blood', 'heart', 'brain', 'future', 'past', 'present', 'time', 'space', 'life', 'death', 'love', 'peace', 'war' ]

display = []
chosen_word = random.choice(word_list)

print(f'테스트 단어 : {chosen_word}')

for i in range(len(chosen_word)):
    display.append('_')

# ascii art generator를 통해 hangman logo를 만들고 logo변수에 대입하시오.
# 첫 시작 시에만 print(logo)가 실행될 수 있게끔 작성하시오
# 생성형 ai에 word_list를 400 개 짜리 만들어 달라고 해서 붙여넣으시오.
# 그러면 전체 hangman이 완성

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