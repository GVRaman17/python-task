print('check eligible for placement')
apt=input('are you complete aptitude')
if apt=='yes':
    com=input('are you complete communication')
    if com=='yes':
        tec=input('are you complete technical')
        if tec=='yes':
            print('your are eligible for placement')
        else:
            print('not eligible for placement')
    else:
        print('not eligible for placement')
else:
    print('not eligible for placement')
