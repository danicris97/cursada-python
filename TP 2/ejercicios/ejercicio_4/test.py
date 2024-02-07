import clsImagen as imagen

if __name__=='__main__':
    img1=imagen.clsImagen(5,10)
    f={}

    print(img1.getMatrizIntensidad())

    img1.determinaFrecuencia()
    f=img1.getFrecuencia()
    print(f)