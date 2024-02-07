import clsPolinomio as polinomio

if __name__=='__main__':
    p=polinomio.Polinomio()

    p.cargaPolinomio()

    print("GRADO: " + str(p.getGrado()))
    for i in range(len(p.getListaMonomios())):
        print(p.getListaMonomios()[i].toString())