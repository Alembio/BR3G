import turtle
from math import *
from library import *
import os.path
import sys

phpfile = sys.argv[1]

#crear unna tortuga llamada turtle
turtle=turtle

#esconder tortuga
turtle.ht()

#Velocidad 1 min 10 max
turtle.speed(10)

direccion="C:/wamp64/www/Python/"
filename= phpfile
#abrir el file a leer y llamarlo f
f=open(direccion + filename,"r")
#guardar en s el string de todo el file
s=f.read()

pt=30
posx= -250
posy= 200
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
    elif x=='1':
        x='one';

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

nombre=os.path.splitext(filename)[0]
print nombre

canvas=turtle.getscreen()
canvas.getcanvas().postscript(file= nombre + "_img.eps")

nomdenuevo= nombre + "_puntos.txt"

nuevo=open(direccion + nomdenuevo,"w")
nuevo.write(" ".join(str(x) for x in out))
nuevo.close()

#sim()

#def esc():
#    while x==1:
#        f.write(recopilar(turtle))
#        time.sleep(.500)
