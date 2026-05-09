
import pygame as p
import settings as s
show_hq_text = False
hq_x=0
hq_y=0
robots=[[0,0]]
planets=[[300,300,s.eternium,s.etmap]]
def button (text,x,y,color,sx,sy):
        text=p.font.SysFont("arial",30).render(text,True,color)
        screen.blit(text,(x,y))
        button_rect = p.Rect(x, y, sx, sy)
        p.draw.rect(screen, color, button_rect, 2)  # Draw the button border
        return button_rect


   
p.mixer.init()
############################  boolean variables  ################
showm=False
run=True
hqplaced=False
can_place_hq=False
shq=False
ettxt=False
return_to_hq=False
reaserch_open = False
#####################################
p.mixer.music.play(-1)  
#####################################
p.init()
screen=p.display.set_mode((s.WIDTH, s.HEIGHT),p.RESIZABLE)

while run:
    x=0
    y=0

    
##################  events  ##################
    for event in p.event.get():
        mouse_x,mouse_y=p.mouse.get_pos()
        
        if hqplaced==True and showm==True and mouse_x>=hq_x and mouse_x<=hq_x+s.hq.get_width() and mouse_y>=hq_y and mouse_y<=hq_y+s.hq.get_height()  and p.mouse.get_pressed()[0] :
            show_hq_text = True

################  clicking events  ###########
        for planet in planets:
            screen.blit(planet[2], (planet[0], planet[1]))
            p_rect = p.Rect(planet[0] + s.x1, planet[1] + s.y1, planet[2].get_width(), planet[2].get_height())



            
        if event.type == p.MOUSEBUTTONDOWN:


            if mouse_x>=s.x1+50 and mouse_x<=s.x1+50+s.eternium.get_width() and mouse_y>=s.y1+100 and mouse_y<=s.y1+100+s.eternium.get_height():
                showm=True
                can_place_hq=False
                map_open_time=p.time.get_ticks()
                shq=True
            if showm==True:
                # if pressing on hq
               
            
                if mouse_x>=s.WIDTH-150 and mouse_x<=s.WIDTH-150+s.etmap.get_width() and mouse_y>=s.HEIGHT-70 and mouse_y<=s.HEIGHT-70+s.etmap.get_height():
                    showm=False
                    emap=False
                    ettxt=False
                    shq=False
                   
                
#                  PLACE HQ (only after next click)
            if showm and can_place_hq and not hqplaced:
                hq_x = mouse_x
                hq_y = mouse_y
                hqplaced = True
                s.money-=1000000
                shq=True
               
            
               
            if mouse_x>=hq_x and mouse_x<=hq_x+s.hq.get_width() and mouse_y>=hq_y and mouse_y<=hq_y+s.hq.get_height() and p.mouse.get_pressed()[0] and hqplaced==True :
                text4=p.font.SysFont("arial",30).render("HQ",True,s.white)
                screen.blit(text4,(hq_x,hq_y-30))
#### quit event     
        if event.type==p.QUIT:
            run=False

##############################################
    
    screen.fill(s.black)

    for i in range(s.WIDTH//s.bg.get_width()-100,s.WIDTH//s.bg.get_width()+100):
        for bz in range(s.HEIGHT//s.bg.get_height()-100,s.HEIGHT//s.bg.get_height()+100):
            screen.blit(s.bg,(i*s.bg.get_width()+s.x1,bz*s.bg.get_height()+s.y1))
    text=p.font.SysFont("arial",30).render(f"${s.money}",True,s.white)
    copper_text=p.font.SysFont("arial",30).render(f"copper: {s.copper}",True,s.white)   
    screen.blit(text,(50,50))
    screen.blit(copper_text,(50,100))
    speed=30
   
    screen.blit(s.eternium,(s.x1+50,s.y1+100))                                             #|
##################################    linked to boolean variables   #####################
    #  if map is open
    a=1200
    ya=300
    
    if showm==True:
        screen.blit(s.etmap,(0,0))
        text2=p.font.SysFont("arial",30).render(s.texto,True,s.white)
        screen.blit(text2,(50,50))
        text3=p.font.SysFont("arial",30).render("___________",True,s.white)
        screen.blit(text3,(s.WIDTH-150+10,s.HEIGHT-70+10))

        #detecting clicks on hq
    
    copper=p.draw.rect(screen, s.orange, (a,ya,10,10))

        
        

    hqr=p.Rect(  (hq_x, hq_y, s.hq.get_width(), s.hq.get_height()))
    # if hq is visible
    if hqplaced==True and shq==True:
    
        
        screen.blit(s.hq, (hq_x, hq_y))
        s.texto="HQ placed successfully the robot coming out of it will gather copper for you! "
        
        
    # to enable placing hq after 2 seconds
    if showm and not can_place_hq:
        if p.time.get_ticks() - map_open_time >= 2000:
            can_place_hq = True
    


    # detecting the relation between robot and orange rectangle
    
# inside the menu when clicking on hq
    if show_hq_text==True:
        p.draw.rect(screen, s.grey, (0,300,1300,500))
        text5=p.font.SysFont("arial",30).render("do u want to sell ur copper?",True,s.white)   
        screen.blit(text5,(50,300))
        text6=p.font.SysFont("arial",30).render("click here to sell",True,s.white)   
        screen.blit(text6,(50,350))
        p.draw.rect(screen, s.red, (50,350,text6.get_width(),text6.get_height()), 2)
        amount_of_copper=p.font.SysFont("arial",30).render(f"copper: {s.copper}",True,s.white)
        screen.blit(amount_of_copper,(50,400))
        close_button = button("close",s.WIDTH-150,s.HEIGHT-70,s.red,100,50)
        if close_button.collidepoint(mouse_x, mouse_y) and p.mouse.get_pressed()[0]:
            show_hq_text = False
        button_rect = button("to make upgrade robot speed", 350, 350, s.red, 300, 50)
        research_button = button("research", 700, 350, s.red, 150, 50)
        if research_button.collidepoint(mouse_x, mouse_y) and p.mouse.get_pressed()[0] :
            reaserch_open = True
        if reaserch_open == True:
            p.draw.rect(screen, s.grey, (0,0,1300,700))
            close_butt=button("close",s.WIDTH-150,s.HEIGHT-70,s.red,100,50)
            upgrade_telescope=button("upgrade telescope",350,350,s.red,300,50)
            if upgrade_telescope.collidepoint(mouse_x, mouse_y) and p.mouse.get_pressed()[0] and s.copper>=100:
                s.telescope_level+=1
                s.copper-=100
            if close_butt.collidepoint(mouse_x, mouse_y) and p.mouse.get_pressed()[0]:
                reaserch_open = False
            

        if button_rect.collidepoint(mouse_x, mouse_y) and p.mouse.get_pressed()[0] and s.copper>=10:
            s.speed+=0.05
            s.copper-=10



        if mouse_x>=50 and mouse_x<=50+text6.get_width() and mouse_y>=350 and mouse_y<=350+text6.get_height() and p.mouse.get_pressed()[0]:
            s.money+=s.copper*2
            s.copper=0

########################################################
########################################################
################################################################################################################

################################################################################################################
########################################################
########################################################
########################################################
########################################################
########################################################
########################################################
########################################################
########################################################

#####################################################
    place=""
    def move_robot_towards_target(placee,move):
        if place==placee:
            move

            
    

    


    for robot in robots:
        robot_rect=p.draw.rect(screen, s.black, (robot[0]+hq_x, robot[1]+hq_y, 10, 10))
        if hqplaced==True and return_to_hq==False:
            if robot[0]+hq_x>=a :
                place="right"
            if robot[0]+hq_x<=a :
                place="left"
            if robot[1]+hq_y>=ya :
                place="down"
            if robot[1]+hq_y<=ya :
                place="up"
            if robot[1]+hq_y<ya and robot[0]+hq_x<a:
                place="upleft"
            if robot[1]+hq_y>ya and robot[0]+hq_x<a:
                place="downleft"
            if robot[1]+hq_y<ya and robot[0]+hq_x>a:
                place="upright"
            if robot[1]+hq_y>ya and robot[0]+hq_x>a:
                place="downright"
        
        # moving the robot towards the orange rectangle
            if place=="right":
                robot[0]-=s.speed
            if place=="left":
                robot[0]+=s.speed
            if place=="down":
                robot[1]-=s.speed
            if place=="up":
                robot[1]+=s.speed
            if place=="upleft":
                robot[0]+=s.speed
                robot[1]+=s.speed
            if place=="downright":
                robot[0]-=s.speed
                robot[1]-=s.speed
            if place=="downleft":
                robot[0]+=s.speed
                robot[1]-=s.speed
            if place=="upright":
                robot[0]-=s.speed
                robot[1]+=s.speed
            if hqplaced==True and return_to_hq==True:
                #detecting relation between robot and hq
                if robot[0]+hq_x>=a :
                    place="right"
                if robot[0]+hq_x<=a :
                    place="left"
                if robot[1]+hq_y>=ya :
                    place="down"
                if robot[1]+hq_y<=ya :
                    place="up"
                if robot[1]+hq_y<ya and robot[0]+hq_x<a:
                    place="upleft"
                if robot[1]+hq_y>ya and robot[0]+hq_x<a:
                    place="downleft"
                if robot[1]+hq_y<ya and robot[0]+hq_x>a:
                    place="upright"
                if robot[1]+hq_y>ya and robot[0]+hq_x>a:
                    place="downright"



        



        if copper.colliderect(robot_rect):
            return_to_hq=True
            print("collided")
        if return_to_hq:
            if robot[0] > 0: robot[0] -= 1
            if robot[0] < 0: robot[0] += 1
            if robot[1] > 0: robot[1] -= 1
            if robot[1] < 0: robot[1] += 1
        if hqr.colliderect(robot_rect):
            
            if return_to_hq==True:
                s.copper+=1
                return_to_hq=False
                

       
###########
    if p.key.get_pressed()[p.K_UP]:
        y+=speed
    if p.key.get_pressed()[p.K_DOWN]:
        y-=speed
    if p.key.get_pressed()[p.K_LEFT]:
        x+=speed
    if p.key.get_pressed()[p.K_RIGHT]:
        x-=speed
    s.x1+=x
    s.y1+=y
   
###############
    p.display.update()
p.quit()