import pygame
import math
import time
class Color:
    r=None
    g=None
    b=None
    def __init__(self, r, g, b):
        self.r = r
        self.b = b
        self.g = g

class Planet:
    color=None
    size=None
    mass=None
    vx=0.0
    vy=0.0
    x=0.0
    y=0.0    id=None
    def __init__(self, color, size, mass, x, y, vx, vy, id):
        self.color = color
        self.size = size
        self.mass = mass
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy        self.id = id
    def move(self, mod=1):
        self.x+=self.vx*mod
        self.y+=self.vy*mod
    def accelerate(self, x, y):
        self.vx+=x
        self.vy+=y
def calculate(p1x, p1y, p2x, p2y, p1m, p2m):    distance=((p1x-p2x)**2)+((p1y-p2y)**2);    return float(667)*(float(p1m*p2m)/float(distance));

WIDTH = 640
HEIGHT = 480
# PIXEL_SCALE_FACTOR = 500000
# PLANET_SIZE_SCALE_FACTOR = 1500000

running = True
planets=[]

#create planets using user input
x = TruenumOfPlanets=0
while x:
    r = int(input("Enter RGB color values: "))
    g = int(input())
    b = int(input())
    size = int(input("Enter the object's diameter in meters: "))
    mass = int(input("Enter the object's mass in kilograms: "))
    x = int(input("Enter the object's initial x position: "))
    y = int(input("Enter the object's initial y position: "))
    vx = int(input("Enter the object's initial x velocity: "))
    vy = int(input("Enter the object's initial y velocity: "))
    numOfPlanets+=1
    planets.append(Planet(Color(r,g,b),size, mass, x, y, vx, vy, numOfPlanets))    if input("if you want to enter another object, type y. Otherwise, type n\t").lower()=='n':
        x=False

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GravityEngine")
quit=False
while not quit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit=True
    win.fill([0, 0, 0])
    for planet in planets:
        if planet.x>=0 and planet.x<=640 and planet.y>=0 and planet.y<=480:
            pygame.draw.circle(win, (planet.color.r, planet.color.g, planet.color.b), (int(planet.x), int(planet.y)), int(planet.size))
        planet.move(0.125)
        tx=0
        ty=0
        for p in planets:            if planet.id!=p.id:                nForce = calculate(planet.x, planet.y, p.x, p.y, planet.mass, p.mass)
                acceleration = (nForce/planet.mass)                if (planet.x-p.x)==0:                    slope=0                else:                    slope = ((planet.y-p.y)/(planet.x-p.x))                if slope!=0:                    if planet.x<p.x:                        tx+=acceleration/slope                    else:                        tx-=acceleration/slope
                    if planet.y<p.y:                        ty+=acceleration*slope                    else:                        ty-=acceleration*slope
        planet.accelerate(tx, ty)    #improve this at some point    for planet in planets:        for p in planets:            if planet.id!=p.id:                distance = ((planet.x-p.x)**2)+((planet.y-p.y)**2)                radDist = planet.size+p.size                if distance<radDist**2:                    distance = math.sqrt(distance)                    deltaY = planet.y-p.y
                    deltaX = planet.x-p.x                    radDist = (radDist-distance)/2                    deltaX = radDist*(deltaX/distance)                    deltaY = radDist*(deltaY/distance)                    planet.x += deltaX
                    planet.y += deltaY
                    p.x -= deltaX
                    p.y -= deltaY    pygame.time.delay(100)
    pygame.display.update()