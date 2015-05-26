from graphics import *

def isBetween(x, end1, end2):
    return end1 <= x <= end2 or end2 <= x <= end1


def isInside(point, rect):
    pt1 = rect.getP1()
    pt2 = rect.getP2()
    return isBetween(point.getX(), pt1.getX(), pt2.getX()) and \
           isBetween(point.getY(), pt1.getY(), pt2.getY())

def makeColoredRect(corner, width, height, color, win):
    corner2 = corner.clone()  
    corner2.move(width, -height)
    rect = Rectangle(corner, corner2)
    rect.setFill(color)
    rect.draw(win)
    return rect



def main():
    win = GraphWin('Find the Hole', 400, 400)
    win.yUp()

    greenButton = makeColoredRect(Point(75, 320), 80, 30, 'green', win)
    yellowButton = makeColoredRect(Point(75, 280), 80, 30, 'yellow', win)
    redButton = makeColoredRect(Point(75, 240), 80, 30, 'red', win)
    purpbutt  =makeColoredRect(Point(75, 200), 80, 30, 'purple', win)

    text3= Text(Point(118,305), "Level 1")
    text4= Text(Point(118,265), "Level 2")
    text5= Text(Point(118,225), "Level 3")
    text6= Text(Point(118,185), "Level 4")
    text7= Text(Point(200,385), "Find the Hole!")
    text33= Text(Point(235,305), "Number of tries: 20")
    text44= Text(Point(235,265), "Number of tries: 15")
    text55= Text(Point(235,225), "Number of tries: 10")
    text66= Text(Point(230,185), "Number of tries: 5")
    
    
    text8= Text(Point(210,45), "A game by Morgan Rose and Chris Hernandez")
    
    text3.draw(win)
    text4.draw(win)
    text5.draw(win)
    text6.draw(win)
    text7.draw(win)
    text33.draw(win)
    text44.draw(win)
    text55.draw(win)
    text66.draw(win)
    
    text8.draw(win)

    msg = Text(Point(win.getWidth()/2, 360),'Click to choose a level difficulty')
    msg.draw(win)
    pt = win.getMouse()
    win.close()
    
    if isInside(pt, greenButton):
        level(65,20)
    elif isInside(pt, yellowButton):
        level(45,15)
    elif isInside(pt, redButton):
        level(20,10)
    elif isInside(pt, purpbutt):
        level(5,5)

from graphics import*
import random, time

def getShift(point1, point2): 
    dx = point2.getX() - point1.getX()
    dy = point2.getY() - point1.getY()
    return (dx*dx + dy*dy)**.5

def setOutline(self, color):
        self._reconfig("outline", color)

def level(radius, clickLimit):
    
    
    win= GraphWin ("Find the Hole", 500, 500)
    text= Text(Point(win.getWidth()/2,30), "Click to find the Circle; Click to Close")
    text.draw(win)
    win.yUp()
    win.getMouse()
    text.undraw()
    
    
                   
    x = random.randrange(5, 495)
    y = random.randrange(5, 495)
    center=Point(x,y)
    

    circle= Circle(center, radius)
    
    circle.draw(win)
    setOutline(circle, "")
    
    user = win.getMouse()
    
    
    
    clickCount=0
    
     
    
    while getShift(user,center) > radius and clickCount<clickLimit:
        
            clickCount+=1
            user.draw(win)
            user = win.getMouse()

            
    if getShift(user,center) < radius:
        
            
        circle.setFill('green')
        text2= Text(Point(win.getWidth()/2,30), 'Level Complete!')
        text2.draw(win)
        
        reButton = makeColoredRect(Point(375, 45), 90, 40, 'yellow', win)
        retext= Text(Point(420,25), "Replay?")
        retext.draw(win)
        pt = win.getMouse()
        win.close()
        if isInside(pt, reButton):
            main()
        else:
            win.close()
        

    else:
        setOutline(circle, "black")
        circle.setFill('red')
        text747= Text(Point(win.getWidth()/2,30), "You Lose")
        text747.draw(win)
        reButton = makeColoredRect(Point(375, 45), 90, 40, 'yellow', win)
        retext= Text(Point(420,25), "Replay?")
        retext.draw(win)
        pt = win.getMouse()
        win.close()
        if isInside(pt, reButton):
            main()
        else:
            win.close()

main()
