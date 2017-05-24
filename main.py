import turtle
from math import *
from library import *
#from writer import *

#crear unna tortuga llamada turtle
turtle=turtle

#esconder tortuga
turtle.ht()

#Velocidad 1 min 10 max
turtle.speed(9)

#abrir el file a leer y llamarlo f
f=open("/Users/rafaella/Documents/Interfaz VLI/probando.txt","r")
#guardar en s el string de todo el file
s=f.read()

pt=30
posx= -50
posy= 100
margenIzq= 300
margenInf=- 250
out=[]

turtle.penup()
turtle.goto(-margenIzq,-margenInf)
turtle.pendown()
turtle.goto(margenIzq,-margenInf)
turtle.goto(margenIzq,margenInf)
turtle.goto(-margenIzq,margenInf)
turtle.goto(-margenIzq,-margenInf)
turtle.penup()


#def sim():
for count in range(len(s)):
    x=s[count]
    if x==' ':
        x='space'
    elif x=='\n':
        x='backslash'

    if posx<margenIzq:

        try:
            out.extend(eval(x)(pt,posx,posy,turtle)) #esta es la funcion que llama a la libreria
        except:
            print 'Algo ha salido mal'
            out.extend(error(pt,posx,posy,turtle))#cuando la el caracter no pertenece a la libreria


        out.extend(noescribir(turtle.xcor(),turtle.ycor(),turtle.xcor()+0.2*pt,turtle.ycor(),turtle))#especio entre letra y letra
        posx=turtle.xcor()
        posy=turtle.ycor()

    elif posx>=margenIzq:
        out.extend(backslash(pt,posx,posy,turtle))#siguiente linea si se llego al maximo de la pagina
        out.extend(noescribir(turtle.xcor(),turtle.ycor(),turtle.xcor()+0.2*pt,turtle.ycor(),turtle))#espacio entre l y l
        posx=turtle.xcor()
        posy=turtle.ycor()
        out.extend(eval(x)(pt,posx,posy,turtle))
        out.extend(noescribir(turtle.xcor(),turtle.ycor(),turtle.xcor()+0.2*pt,turtle.ycor(),turtle))#especio entre letra y letra
        posx=turtle.xcor()
        posy=turtle.ycor()

    elif posy<margenInf:
        print 'Se llego al maximo de la pagina'
        break

print out
print len(out)

canvas=turtle.getscreen()
canvas.getcanvas().postscript(file="duck.eps")

#sim()

#def esc():
#    while x==1:
#        f.write(recopilar(turtle))
#        time.sleep(.500)
