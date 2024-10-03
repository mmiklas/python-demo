# Napisz funkcję test(), pobierającą liczbę punktów.
# Jeżeli punktów więcej niż 50 to wyświetl napis zaliczony.
# W przeciwnym wypadku wyświetl niezaliczony.


def test(points):
    if points > 50:
        print("zaliczony")
    else:
        print("niezaliczony")

# Sprawdź jak działa ta funkcja
test(60)
test(40)