def fibonacci(n):
    reeks = [0,1]
#beginwaarden


    for i in range(2,n+1):
        next_num = reeks[-1] + reeks[-2]
#Voeg de laatste twee getallen achter elkaar toe

        reeks.append(next_num)
    return reeks
#breng eerst n Fibonacci-getallen terug


reeks = fibonacci(10)
print(reeks)