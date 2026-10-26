#try - linijki powodujące błąd (najlepiej tylko one - mozliwie jak najmniej kodu)
#except <nazwa(klasa) bledu> - co ma sie wydarzyc gdy wystapi dany błąd
#else - kontynuacja bloku try - wykona sie tylko jezeli w try nie dojdzie do bledu
#finally

try:
    a = int(input('Podaj liczbe: '))
    b = int(input('Podaj liczbe: '))
except ValueError:
    print('Podałeś złą wartość')
else:
    try:
        result = a / b
    except ZeroDivisionError:
        print('Dzielnik nie moze byc rowny 0')
    else:
        print(result)
    # finally:
    #     print('To zawsze sie wykona')
    print('To zawsze sie wykona')
