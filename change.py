def change():
    expense = 23.75
    money = 100
    vuelto = 0
    centavos = 0
    # Intento fallido print(f'Ingresar gasto:\n{expense}\nDinero recibido\n{money}\n\nVuelto\n\nPesos:\n{int(money) - int(expense) -1 }\nCentavos:\n{(int(money) - int(expense)) - 52 }'  )
    print(f"Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)

    print("\nVuelto\n")

    print("Pesos:")
    vuelto = int(money - expense)
    print(int(vuelto))

    print("Centavos: ")
    centavos = ((money - expense)-vuelto) * 100
    print(int(centavos))
