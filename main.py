import pygame
import math

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
    y=0.0
    def __init__(self, color, size, mass, x, y, vx, vy, id):
        self.color = color
        self.size = size
        self.mass = mass
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
    def move(self, mod=1):
        self.x+=self.vx*mod
        self.y+=self.vy*mod
    def accelerate(self, x, y):
        self.vx+=x
        self.vy+=y


WIDTH = 640
HEIGHT = 480
# PIXEL_SCALE_FACTOR = 500000
# PLANET_SIZE_SCALE_FACTOR = 1500000

running = True
planets=[]

#create planets using user input
x = True
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
    planets.append(Planet(Color(r,g,b),size, mass, x, y, vx, vy, numOfPlanets))
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
        for p in planets:
                acceleration = (nForce/planet.mass)
                    if planet.y<p.y:
        planet.accelerate(tx, ty)
                    deltaX = planet.x-p.x
                    planet.y += deltaY
                    p.x -= deltaX
                    p.y -= deltaY
    pygame.display.update()