from manu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 기본 생성자를 통한 객체 생성
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    choice = input(f'어떤 음료를 드시겠습니까?\n{menu.get_items()}\n재료 확인\n종료\n>>> ')

    if choice == '종료':
        is_on = False
        print('머신을 종료 합니다,')

    elif choice == '재료 확인':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)