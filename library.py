def linea(xinicial,yinicial,xfinal,yfinal,turtle):

    s=0
    lista=[]
    turtle.goto(xinicial,yinicial)
    turtle.pendown()
    while s <=1:
        turtle.goto(xinicial+s*(xfinal-xinicial),yinicial+s*(yfinal-yinicial))
        lista.extend((turtle.xcor(),turtle.ycor(),1))
        s +=0.05#si queremos una mejor resolucion usamos un numero menor
    turtle.penup()
    return lista

def noescribir(xinicial,yinicial,xfinal,yfinal,turtle):

    s=0
    lista=[]
    turtle.goto(xinicial,yinicial)
    turtle.penup()
    while s <=1:
        turtle.goto(xinicial+s*(xfinal-xinicial),yinicial+s*(yfinal-yinicial))
        lista.extend((turtle.xcor(),turtle.ycor(),0))
        s +=0.2#si queremos una mejor resolucion usamos un numero menor
    turtle.penup()
    return lista

def circulo(xinicial,yinicial,angi,angsum,r,turtle):
    from math import sin,pi,cos
    s=0
    lista=[]
    turtle.goto(xinicial,yinicial)
    ang= pi*angi/180
    xc=xinicial-r*cos(ang)
    yc=yinicial-r*sin(ang)
    turtle.pendown()

    while s <=1:
        turtle.goto(xc+r*cos(ang+s*pi*angsum/180),yc+r*sin(ang+s*pi*angsum/180))
        lista.extend((turtle.xcor(),turtle.ycor(),1))
        s+=0.02

    turtle.penup()

    return lista

def error(pt,posx,posy,turtle):
    lamb=0.65
    turtle.penup()
    l=pt
    w=lamb*pt
    lista=[]

    lista.extend(linea(posx,posy,posx,posy-l,turtle))
    lista.extend(linea(posx,posy-l,posx+w,posy-l,turtle))#Hace palo de abajo _
    lista.extend(noescribir(posx+w,posy-l,posx,posy,turtle))#regresa arriba
    lista.extend(linea(posx,posy,posx+w,posy,turtle))#hace el palito de arriba -
    lista.extend(noescribir(posx+w,posy,posx,posy-(l/2),turtle))#se va a la mitad
    lista.extend(linea(posx,posy-(l/2),posx+w,posy-(l/2),turtle))#escribe el palito del medio -
    lista.extend(noescribir(posx+w,posy-(l/2),posx+w,posy,turtle))#

    print 'error'
    return lista

def space(pt,posx,posy,turtle):
    lamb=0.5
    turtle.penup()
    l=pt
    w=lamb*pt
    lista=[]

    lista.extend(noescribir(posx,posy,posx+w,posy,turtle))
    #turtle.goto(posx+w,posy)
    print 'space'
    return lista

def backslash(pt,posx,posy,turtle):
    turtle.penup()
    lista=[]

    lista.extend(noescribir(posx,posy,-250-0.2*pt,posy-1.2*pt,turtle))#regresa al inicio de linea
    #turtle.goto(-250-0.2*pt,posy-1.2*pt)
    print 'enter'
    return lista

def A(pt,posx,posy,turtle):
    lamb=0.65
    turtle.penup()
    l=pt
    w=lamb*pt
    lista=[]
    xinicial=posx
    yinicial=posy-l
    xfinal=posx+(w/2)
    yfinal=posy

    lista.extend(linea(xinicial,yinicial,xfinal,yfinal,turtle))
    # xinicial=posx
    # yinicial=posy-l
    # s=0
    # xfinal=posx+(w/2)
    # yfinal=posy
    #
    # turtle.goto(xinicial,yinicial)
    # turtle.pendown()
    # while s <=1:
    #     turtle.goto(xinicial+s*(xfinal-xinicial),yinicial+s*(yfinal-yinicial))
    #     lista.extend((turtle.xcor(),turtle.ycor(),1))
    #     s +=0.1
    #     #se hizo el primer palo diagonal / ahora x=posx+(w/2) y y=posy
    # turtle.penup()

    lista.extend(linea(xfinal,yfinal,posx+w,posy-l,turtle))
    # xinicial=xfinal
    # yinicial=yfinal
    # s=0
    # xfinal=posx+w
    # yfinal=posy-l
    #
    # turtle.goto(xinicial,yinicial)
    # turtle.pendown()
    # while s <=1:
    #     turtle.goto(xinicial+s*(xfinal-xinicial),yinicial+s*(yfinal-yinicial))
    #     lista.extend((turtle.xcor(),turtle.ycor(),1))
    #     s +=0.1
    #     #se hizo el segundo palo diagonal \ ahora x=posx+w y y=posy-l
    # turtle.penup()
    lista.extend(noescribir(posx+w,posy-l,posx+(w/4),posy-(l/2),turtle))#se mueve para hacer la rayita

    lista.extend(linea(posx+(w/4),posy-(l/2),posx+(3*w/4),posy-(l/2),turtle))#hace la rayita
    # xinicial=posx+(w/4)
    # yinicial=posy-(l/2)
    # s=0
    # xfinal=posx+(3*w/4)
    # yfinal=posy-(l/2)
    #
    # turtle.goto(xinicial,yinicial)
    # turtle.pendown()
    # while s <=1:
    #     turtle.goto(xinicial+s*(xfinal-xinicial),yinicial+s*(yfinal-yinicial))
    #     lista.extend((turtle.xcor(),turtle.ycor(),1))
    #     s +=0.1
    #     #se hizo el palito del medio -
    # turtle.penup()

    lista.extend(noescribir(posx+(3*w/4),posy-(l/2),posx+w,posy,turtle))#este ultimo codigo debe estar al final de todas las funciones
    #turtle.goto(posx+w,posy)#este ultimo codigo debe estar al final de todas las funciones
    print 'A'
    return lista

def B(pt,posx,posy,turtle):
    lamb=0.5
    turtle.penup()
    l=pt
    w=lamb*pt
    r=pt/4
    lista=[]

    lista.extend(noescribir(posx,posy,posx,posy-l,turtle))#va a la base
    lista.extend(linea(posx,posy-l,posx,posy,turtle))#sube
    lista.extend(linea(posx,posy,posx+(w/4),posy,turtle))#avanza un poquito
    lista.extend(circulo(posx+(w/4),posy,90,-180,r,turtle))#primer semicriculo
    lista.extend(linea(posx+(w/4),posy-(l/2),posx+(w/2),posy-(l/2),turtle))
    lista.extend(circulo(posx+(w/2),posy-(l/2),90,-180,r,turtle))#segundo semicirculo
    lista.extend(linea(posx+(w/2),posy-l,posx,posy-l,turtle))
    lista.extend(noescribir(posx,posy-l,posx+w,posy,turtle))

    print 'B'
    return lista

def C(pt,posx,posy,turtle):
    lamb=0.80
    turtle.penup()
    l=pt
    w=lamb*pt
    r=pt/2
    lista=[]

    lista.extend(noescribir(posx,posy,posx+r+(1.41)*r,posy-r+(2**(0.5))*r,turtle))#va a la pos inicial
    lista.extend(circulo(posx+(8*r/5),posy-(r/5),53,254,r,turtle))#hace curva
    lista.extend(noescribir(posx+(2.41421)*r,posy-(2.41421)*r,posx+w,posy,turtle))

    print 'C'
    return lista

def D(pt,posx,posy,turtle):
    lamb=0.75
    turtle.penup()
    l=pt
    w=lamb*pt
    r=pt/2
    lista=[]

    lista.extend(noescribir(posx,posy,posx,posy-l,turtle))#va a la base
    lista.extend(linea(posx,posy-l,posx,posy,turtle))#sube
    lista.extend(linea(posx,posy,posx+(r/2),posy,turtle))
    lista.extend(circulo(posx+(r/2),posy,90,-180,r,turtle))#Hace curva
    lista.extend(linea(posx+(r/2),posy-l,posx,posy-l,turtle))
    lista.extend(noescribir(posx,posy-l,posx+w,posy,turtle))

    print 'D'
    return lista

def E(pt,posx,posy,turtle):
    lamb=0.65
    turtle.penup()
    l=pt
    w=lamb*pt
    lista=[]

    lista.extend(linea(posx,posy,posx,posy-l,turtle)) #escribe el palo | de arriba abajo
    #turtle.goto(posx,posy)

    #turtle.pendown()

    #turtle.goto(posx,posy-l)
    lista.extend(linea(posx,posy-l,posx+w,posy-l,turtle))#Hace palo de abajo _
    #turtle.goto(posx+w,posy-l) #Hace la forma L

    #turtle.penup()
    lista.extend(noescribir(posx+w,posy-l,posx,posy,turtle))#regresa arriba
    #turtle.goto(posx,posy)

    lista.extend(linea(posx,posy,posx+w,posy,turtle))#hace el palito de arriba -
    #turtle.pendown()

    #turtle.goto(posx+w,posy)#Hace el palito de arriba -

    #turtle.penup()
    lista.extend(noescribir(posx+w,posy,posx,posy-(l/2),turtle))#se va a la mitad
    #turtle.goto(posx,posy-l/2)

    #turtle.pendown()
    lista.extend(linea(posx,posy-(l/2),posx+(w/2),posy-(l/2),turtle))#escribe el palito del medio -
    #turtle.goto(posx+0.75*w,posy-l/2)

    #turtle.penup()
    lista.extend(noescribir(posx+(w/2),posy-(l/2),posx+w,posy,turtle))#
    #turtle.goto(posx+w,posy)#este ultimo codigo debe estar al final de todas las funciones
    print 'E'
    return lista

def F(pt,posx,posy,turtle):
    lamb=0.5
    turtle.penup()
    l=pt
    w=lamb*pt
    lista=[]

    lista.extend(noescribir(posx,posy,posx,posy-l,turtle))#se mueve a la base
    lista.extend(linea(posx,posy-l,posx,posy,turtle)) #escribe el palo | de abajo arriba
    lista.extend(linea(posx,posy,posx+w,posy,turtle))#escribe palo de arriba
    lista.extend(noescribir(posx+w,posy,posx,posy-(l/2),turtle))#se mueve al medio
    lista.extend(linea(posx,posy-(l/2),posx+(w/2),posy-(l/2),turtle))#escribe el palo del medio -
    lista.extend(noescribir(posx+(w/2),posy-(l/2),posx+w,posy,turtle))#va a la posicion final
    print'F'
    return lista

def G(pt,posx,posy,turtle):
    lamb=1
    turtle.penup()
    l=pt
    w=lamb*pt
    lista=[]
    r=pt/2

    lista.extend(noescribir(posx,posy,posx+r+(1.41)*r,posy-r+(2**(0.5))*r,turtle))#va a la pos inicial
    lista.extend(circulo(posx+(8*r/5),posy-(r/5),53,307,r,turtle))#hace curva
    lista.extend(linea(posx+w,posy-(l/2),posx+(w/2),posy-(l/2),turtle))#hace linea
    lista.extend(noescribir(posx+w,posy-(l/2),posx+w,posy,turtle))

    print 'G'
    return lista

def H(pt,posx,posy,turtle):
    lamb=0.65
    turtle.penup()
    l=pt
    w=lamb*pt
    lista=[]

    lista.extend(linea(posx,posy,posx,posy-l,turtle)) #escribe el palo | de arriba abajo
    lista.extend(noescribir(posx,posy-l,posx+w,posy,turtle))#se mueve arriba ala derecha
    lista.extend(linea(posx+w,posy,posx+w,posy-l,turtle)) #escribe el palo | de arriba abajo
    lista.extend(noescribir(posx+w,posy-l,posx,posy-(l/2),turtle))#se mueve al medio
    lista.extend(linea(posx,posy-(l/2),posx+w,posy-(l/2),turtle))#escribe el palo del medio -
    lista.extend(noescribir(posx+w,posy-(l/2),posx+w,posy,turtle))#va a la posicion final
    print'H'
    return lista

def I(pt,posx,posy,turtle):
    lamb=0
    turtle.penup()
    l=pt
    w=lamb*pt
    lista=[]

    lista.extend(linea(posx,posy,posx,posy-l,turtle)) #escribe el palo | de arriba abajo
    lista.extend(noescribir(posx,posy-l,posx+w,posy,turtle))#va a la posicion final
    print 'I'
    return lista

def J(pt,posx,posy,turtle):
    lamb=0.5
    turtle.penup()
    l=pt
    w=lamb*pt
    lista=[]
    r=w/2

    lista.extend(noescribir(posx,posy-l,posx+w,posy,turtle))#va a la posicion inicial
    lista.extend(linea(posx+w,posy,posx+w,posy-(3*l/4),turtle)) #escribe el palo | de arriba abajo
    lista.extend(circulo(posx+w,posy-(3*l/4),0,-180,r,turtle))#hace curva
    lista.extend(noescribir(posx,posy-(3*l/4),posx+w,posy,turtle))#va a la posicion final

    print 'J'
    return lista

def K(pt,posx,posy,turtle):
    lamb=0.65
    turtle.penup()
    l=pt
    w=lamb*pt
    lista=[]

    lista.extend(linea(posx,posy,posx,posy-l,turtle)) #escribe el palo | de arriba abajo
    lista.extend(noescribir(posx,posy-l,posx+w,posy,turtle))#va arriba a la derecha
    lista.extend(linea(posx+w,posy,posx,posy-(l/2),turtle))#escribe linea hacia el medio /
    lista.extend(linea(posx,posy-(l/2),posx+w,posy-l,turtle))#escribe linea desde el medio \
    lista.extend(noescribir(posx-w,posy-l,posx+w,posy,turtle))#va a la posicion final
    print 'K'
    return lista

def L(pt,posx,posy,turtle):
    lamb=0.65
    turtle.penup()
    l=pt
    w=lamb*pt
    lista=[]

    lista.extend(linea(posx,posy,posx,posy-l,turtle)) #escribe el palo | de arriba abajo
    lista.extend(linea(posx,posy-l,posx+w,posy-l,turtle))#Hace palo de abajo _
    lista.extend(noescribir(posx-w,posy-l,posx+w,posy,turtle))#va a la posicion final
    print 'L'
    return lista

def M(pt,posx,posy,turtle):
    lamb=0.65
    turtle.penup()
    l=pt
    w=lamb*pt
    lista=[]

    lista.extend(noescribir(posx,posy,posx,posy-l,turtle))#se mueve a la base
    lista.extend(linea(posx,posy-l,posx,posy,turtle)) #escribe el palo | de abajo arriba
    lista.extend(linea(posx,posy,posx+(w/2),posy-(3*l/4),turtle))#escribe el primer palito \
    lista.extend(linea(posx+(w/2),posy-(3*l/4),posx+w,posy,turtle))
    lista.extend(linea(posx+w,posy,posx+w,posy-l,turtle)) #escribe el palo | de arriba abajo
    lista.extend(noescribir(posx+w,posy-l,posx+w,posy,turtle))#va a la posicion final

    print 'M'
    return lista

def N(pt,posx,posy,turtle):
    lamb=0.65
    turtle.penup()
    l=pt
    w=lamb*pt
    lista=[]

    lista.extend(noescribir(posx,posy,posx,posy-l,turtle))#se mueve a la base
    lista.extend(linea(posx,posy-l,posx,posy,turtle)) #escribe el palo | de abajo arriba
    lista.extend(linea(posx,posy,posx+w,posy-l,turtle)) #Escribe diagonal \
    lista.extend(linea(posx+w,posy-l,posx+w,posy,turtle))#Escribe palo de abajo arriba
    print 'M'
    return lista

def O(pt,posx,posy,turtle):
    lamb=1
    turtle.penup()
    l=pt
    w=lamb*pt
    r=l/2
    lista=[]

    lista.extend(noescribir(posx,posy,posx+(w/2),posy,turtle))#Se mueve al medio
    lista.extend(circulo(posx+(w/2),posy,90,360,r,turtle))#hace circulo
    lista.extend(noescribir(posx+(w/2),posy,posx+w,posy,turtle))#se va a la posicion final

    print 'O'
    return lista

def P(pt,posx,posy,turtle):
    lamb=0.5
    turtle.penup()
    l=pt
    w=lamb*pt
    r=pt/4
    lista=[]

    lista.extend(noescribir(posx,posy,posx,posy-l,turtle))#va a la base
    lista.extend(linea(posx,posy-l,posx,posy,turtle))#sube
    lista.extend(linea(posx,posy,posx+r,posy,turtle))#avanza un poquito
    lista.extend(circulo(posx+r,posy,90,-180,r,turtle))#primer semicriculo
    lista.extend(linea(posx+r,posy-2*r,posx,posy-2*r,turtle))#retrocede un poquito
    lista.extend(noescribir(posx,posy-2*r,posx+w,posy,turtle))#va a posicion final

    print 'P'
    return lista

def Q(pt,posx,posy,turtle):
    lamb=1
    turtle.penup()
    l=pt
    w=lamb*pt
    r=l/2
    lista=[]

    lista.extend(noescribir(posx,posy,posx+(w/2),posy,turtle))#Se mueve al medio
    lista.extend(circulo(posx+(w/2),posy,90,360,r,turtle))#hace circulo
    lista.extend(noescribir(posx+(w/2),posy,posx+(w/2),posy-(l/2),turtle))#se va a la posicion del medio
    lista.extend(linea(posx+(w/2),posy-(l/2),posx+w,posy-l,turtle))
    lista.extend(noescribir(posx+w,posy-l,posx+w,posy,turtle))#va a posicion final

    print 'Q'
    return lista

def R(pt,posx,posy,turtle):
    lamb=0.5
    turtle.penup()
    l=pt
    w=lamb*pt
    r=pt/4
    lista=[]

    lista.extend(noescribir(posx,posy,posx,posy-l,turtle))#va a la base
    lista.extend(linea(posx,posy-l,posx,posy,turtle))#sube
    lista.extend(linea(posx,posy,posx+r,posy,turtle))#avanza un poquito
    lista.extend(circulo(posx+r,posy,90,-180,r,turtle))#primer semicriculo
    lista.extend(linea(posx+r,posy-2*r,posx,posy-2*r,turtle))#retrocede un poquito
    lista.extend(linea(posx,posy-2*r,posx+w,posy-l,turtle))#hace raya \
    lista.extend(noescribir(posx+w,posy-l,posx+w,posy,turtle))#va a posicion final

    print 'R'
    return lista

def S(pt,posx,posy,turtle):
    lamb=0.5
    turtle.penup()
    l=pt
    w=lamb*pt
    r=pt/4
    lista=[]

    lista.extend(noescribir(posx,posy,posx+w,posy,turtle))#va a la pos inicial
    lista.extend(linea(posx+w,posy,posx+(w/2),posy,turtle))#retocede un poquito
    lista.extend(circulo(posx+(w/2),posy,90,180,r,turtle))#primer semicriculo
    lista.extend(circulo(posx+(w/2),posy-(l/2),90,-180,r,turtle))#segundo semicirculo
    lista.extend(linea(posx+(w/2),posy-l,posx,posy-l,turtle))
    lista.extend(noescribir(posx,posy-l,posx+w,posy,turtle))

    print 'S'
    return lista

def T(pt,posx,posy,turtle):
    lamb=0.65
    turtle.penup()
    l=pt
    w=lamb*pt
    lista=[]

    lista.extend(noescribir(posx,posy,posx+(w/2),posy,turtle))#se mueve al medio
    lista.extend(linea(posx+(w/2),posy,posx+(w/2),posy-l,turtle)) #escribe el palo | de arriba abajo
    lista.extend(noescribir(posx+(w/2),posy-l,posx,posy,turtle))#se mueve arriba
    lista.extend(linea(posx,posy,posx+w,posy,turtle)) #escribe el palo - de arriba
    print 'T'
    return lista

def U(pt,posx,posy,turtle):
    lamb=0.5
    turtle.penup()
    l=pt
    w=lamb*pt
    lista=[]
    r=w/2

    lista.extend(noescribir(posx,posy-l,posx+w,posy,turtle))#va a la posicion inicial
    lista.extend(linea(posx+w,posy,posx+w,posy-(3*l/4),turtle)) #escribe el palo | de arriba abajo
    lista.extend(circulo(posx+w,posy-(3*l/4),0,-180,r,turtle))#hace curva
    lista.extend(linea(posx,posy-(3*l/4),posx,posy,turtle))#hace otra linea
    lista.extend(noescribir(posx,posy,posx+w,posy,turtle))#va a la posicion final

    print 'U'
    return lista

def V(pt,posx,posy,turtle):
    lamb=0.65
    turtle.penup()
    l=pt
    w=lamb*pt
    lista=[]

    lista.extend(linea(posx,posy,posx+(w/2),posy-l,turtle)) #Escribe diagonal \
    lista.extend(linea(posx+(w/2),posy-l,posx+w,posy,turtle))#escribe otra diagonal /
    print 'V'
    return lista

def W(pt,posx,posy,turtle):
    lamb=0.8
    turtle.penup()
    l=pt
    w=lamb*pt
    lista=[]

    lista.extend(linea(posx,posy,posx+(w/4),posy-l,turtle)) #Escribe diagonal \
    lista.extend(linea(posx+(w/4),posy-l,posx+(w/2),posy-(l/2),turtle)) #Escribe diagonal /
    lista.extend(linea(posx+(w/2),posy-(l/2),posx+(3*w/4),posy-l,turtle)) #Escribe diagonal \
    lista.extend(linea(posx+(3*w/4),posy-l,posx+w,posy,turtle)) #Escribe diagonal /

    print 'W'
    return lista

def X(pt,posx,posy,turtle):
    lamb=0.65
    turtle.penup()
    l=pt
    w=lamb*pt
    lista=[]

    lista.extend(linea(posx,posy,posx+w,posy-l,turtle)) #Escribe diagonal \
    lista.extend(noescribir(posx+w,posy-l,posx,posy-l,turtle))#se mueve abajo a la izquierda
    lista.extend(linea(posx,posy-l,posx+w,posy,turtle))#segunda diagonal/

    print 'X'
    return lista

def Y(pt,posx,posy,turtle):
    lamb=0.65
    turtle.penup()
    l=pt
    w=lamb*pt
    lista=[]

    lista.extend(noescribir(posx,posy,posx+w,posy,turtle))#se mueve arriba a la derecha
    lista.extend(linea(posx+w,posy,posx,posy-l,turtle))#segunda diagonal/
    lista.extend(noescribir(posx,posy-l,posx,posy,turtle))#se mueve arriba a la izquierda
    lista.extend(linea(posx,posy,posx+(w/2),posy-(l/2),turtle))#hace palito diagonal \
    lista.extend(noescribir(posx+(w/2),posy-(l/2),posx+w,posy,turtle))#va a la posicion final

    print 'Y'
    return lista

def Z(pt,posx,posy,turtle):
    lamb=0.65
    turtle.penup()
    l=pt
    w=lamb*pt
    lista=[]

    lista.extend(linea(posx,posy,posx+w,posy,turtle)) #escribe el palo - de arriba
    lista.extend(linea(posx+w,posy,posx,posy-l,turtle))#segunda diagonal /
    lista.extend(linea(posx,posy-l,posx+w,posy-l,turtle)) #escribe el palo - de abajo
    lista.extend(noescribir(posx+w,posy-l,posx+w,posy,turtle))#va a la posicion final

    print 'Z'
    return lista
