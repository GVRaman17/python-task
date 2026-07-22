unit=int(input('how much electric bill unit'))
match unit:
    case x if 0<=x<=200:
        print('free')
    case x if 200<x<=500:
        price=unit-200;
        print("your unit is" ,price)
    case x if 500<x:
        price=unit-100;
        print("your unit is" ,price)
    case _:
        print('do not enter negative')
