nimi = input('Mis on teie nimi: ')
lubatud = int(input('Sisestage lubatud kiirus (km/h): '))
tegelik = int(input('Sisestage tegelik kiirus (km/h): '))

def arvutaTrahv():
    if (tegelik > lubatud):
        trahv = (tegelik - lubatud) * 3
        if (trahv <= 190):
            return print(f'{nimi}, kiiruse ületamise eest on teie trahv {trahv} eurot.')
        return print(f'{nimi}, kiiruse ületamise eest on teie trahv 190 eurot.')

arvutaTrahv()
