import pygame as p
from pygame import mixer
import pygame as p
p.mixer.init()

bg=p.image.load(("graphics/bg.jpg"))
eternium=p.image.load(("graphics/eternium.png"))
etmap=p.image.load(("graphics/map of eternium.png"))
hq=p.image.load(("graphics/HQ.png"))
ninjua=p.image.load(("graphics/ninjua.png"))
nunjua_map=p.image.load(("graphics/ninjuamap.png"))
p.mixer.music.load(("graphics/Krisu - Oxygen for a Dying World.mp3"))

texto="where do u want to place ur hq! Click on ______ to exit map."
money=1000000
copper=0
iron=0
y1,x1=0,0
cx,cy=0,0
telescope_level=1
x=0
y=0
speed=1
#####################################
WIDTH=600
HEIGHT=600
##############COLORS#################
red=(255,0,0)
black=(0,0,0)
white=(255,255,255)
blue=(0,0,255)
green=(0,255,0)
yellow=(255,255,0)
orange=(255,128,0)
purple=(128,0,128)
pink=(255,192,203)
violet=(238,130,238)
grey=(128,128,128)
#####################################
