def is_valid_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False

strona_a = float(input('Wpisz dlugosc boku a: '))
strona_b = float(input('Wpisz dlugosc boku b: '))
strona_c = float(input('Wpisz dlugosc boku c: '))

if is_valid_triangle(strona_a, strona_b, strona_c):
    print('Trojkat jest poprawny')


