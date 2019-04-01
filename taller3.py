def resta__base(lista1,lista2,n):
    if type (lista1,list) and type (lista2,list):
        return resta_aux(lista1,0,lista2,n)
    else : return "error"

def resta_aux(lista1,prestado,lista2,base):
    if lista1 == []:
        return []
    elif (lista1[0]- prestado)>lista2[0]:
        return [lista1[0]-prestado]- lista2[0] + resta_aux(lista1[1:],prestado,lista2[1:],base)
    elif (lista1[0]-prestado)== lista2[0]:
        return [0] + resta_aux(lista[1:],prestado,lista2[1:],base)
    elif (lista1[0]-prestado)<lista2[0]:
        return [((lista1[0]-prestado)+base) - lista2[0]] + resta_aux(lista1[1:],prestado + 1, lista2[1:],base)
