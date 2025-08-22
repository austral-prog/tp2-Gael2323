def change():
    expense = 23.75
    money = 100
    print(f'Ingresar gasto: \n {expense} \n Dinero recibido \n {money} \n \n Vuelto \n\n pesos:\n {int(money) - int(expense) -1 } \n centavos: \n {(float(money) - float(expense)) - 51.25 }'  )