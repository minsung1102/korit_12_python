MENU = {
    '에스프레소': {
        '재료': {
            '물' : 50,
                '커피' :18,
        },
        '가격' : 1.5,
    },
    '라떼' : {
       '재료' : {
           '물' : 200,
           '우유' : 150,
           '커피' : 24
       } ,
        '가격' : 2.5,
    },
    '카푸치노' : {
        '재료' : {
            '물' : 250,
            '우유' : 100,
            '커피' : 24
        },
        '가격' : 3.0,
    },
}

resources = {
    '물' : 300,
    '우유' : 200,
    '커피' : 100,
}
profit = 0

def report():
    print(f'물 : {resources['물']}ml\n'
          f'우유 : {resources["우유"]}ml\n'
          f'커피 : {resources['커피']}g\n'
          f'돈 : {profit}원')

def is_resource_enough(order_ingerdients):  # order_ingredients = drink['재료']

    for item in order_ingerdients:
        if order_ingerdients[item] > resources[item]:
            print(f'{resources[item]}이(가) 부족합니다')
            return False
    return True

def process_coins():

    total = 0.0
    total += int(input('쿼터즈 동전을 넣어주세요 >>> '))*0.25
    total += int(input('데임스 동전을 넣어주세요 >>> '))*0.10
    total += int(input('니켈즈 동전을 넣어주세요 >>> '))*0.05
    total += int(input('페니즈 동전을 넣어주세요 >>> '))*0.01
    return total

def is_transaction_successful(money_received, drink_cost):

    global profit
    change = round(money_received - drink_cost, 2)
    if change > 0:
        profit += drink_cost
        print(f'잔돈 : {change} 원을 반환합니다.')
        return True
    else:
        print(f'금액이 충분하지 않습니다. ${money_received}를 반환합니다')

def make_coffee(drink_name, order_ingredients): # call2() 유형으로 정의

    # 재료 감하는 부분
    for item in order_ingredients:  # order_ingredients = drink['재료']
        resources[item] -= order_ingredients[item]
    # 커피 안내문구
    print(f'{drink_name}가 나왔습니다. 맛있게 드세요')

is_on = True
while is_on:
    choice = input('어떤 음료를 드시겠습니까? 에스프레소 / 라떼 / 카푸치노 >>> ')

    if choice == 'off':
        is_on = False
        print('자판기가 종료 되었습니다.')

    elif choice == 'report':
        report()

    elif choice in ['에스프레소','라떼', '카푸치노']:
        drink = MENU[choice]
        if is_resource_enough(drink['재료']):
            money_received = process_coins()
            if is_transaction_successful(money_received, drink['가격']):

                #재료 차감
                make_coffee(choice, drink['재료'])

    else:
        print("잘못된 입력입니다.")