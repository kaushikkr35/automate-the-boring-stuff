list_of_lambdas = []

l = lambda x : list_of_lambdas.append(x)
for i in range(1,6):
    l(i)

print(list_of_lambdas)

