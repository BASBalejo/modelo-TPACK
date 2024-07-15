import turtle

# Configuración de la pantalla
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Dibujo de un corazón")

# Configuración de la tortuga
t = turtle.Turtle()
t.color("red")
t.pensize(5)
t.speed(1)

# Función para dibujar un corazón
def draw_heart():
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.left(120)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()

# Dibujar el corazón
draw_heart()

# Finalizar
turtle.done()
