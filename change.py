def change():
    expense = 23.75
    money = 100
    print(f'Ingresar gasto:\n{expense}\nDinero recibido\n{money}\n\nVuelto\n\nPesos:\n{int(money) - int(expense) -1 }\nCentavos:\n{(int(money) - int(expense)) - 52 }'  )