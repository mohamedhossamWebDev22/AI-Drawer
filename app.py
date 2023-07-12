from colors import colors
import turtle, time, random

def wait(num):
  time.sleep(num)

rColor = random.choice(colors)

print(rColor)

screen = turtle.getscreen()
screen.title("AI Draw !!")
screen.bgcolor("gray")
screen.screensize(500, 500)

pencil = turtle.Turtle()
pencil.color(rColor)

for i in range(150):
  distance = (random.random() * 150)
  print(distance)
  
  rColor = random.choice(colors)
  rColor2 = random.choice(colors)

  pencil.color(rColor)

  screen.bgcolor(rColor2)

  commandes = ['pencil.fd(distance)', 'pencil.rt(distance)', 'pencil.lt(distance)', 'pencil.bk(distance)',]

  cmnd = random.choice(commandes)
  eval(cmnd)


wait(8)