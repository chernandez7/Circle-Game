from graphics import *
import random, time

# Checks if point is between two other points
def isBetween(x, end1, end2):
    return end1 <= x <= end2 or end2 <= x <= end1

# Checks if point is inside a rectangle (button)
def isInside(point, rect):
    pt1 = rect.getP1()
    pt2 = rect.getP2()
    return isBetween(point.getX(), pt1.getX(), pt2.getX()) and \
           isBetween(point.getY(), pt1.getY(), pt2.getY())

# Creates rectangle
def makeColoredRect(corner, width, height, color, win):
    corner2 = corner.clone()  
    corner2.move(width, -height)
    rect = Rectangle(corner, corner2)
    rect.setFill(color)
    rect.draw(win)
    return rect

# Create and draw text
def makeText(x, y, text, window):
    text = Text(Point(x, y), text)
    text.draw(window)

# Gets difference of two points
def getShift(point1, point2): 
    dx = point2.getX() - point1.getX()
    dy = point2.getY() - point1.getY()
    return (dx*dx + dy*dy)**.5

# Changes outline of shape to a color
def setOutline(self, color):
        self._reconfig("outline", color)

# Level depending on difficulty
def level(radius, clickLimit):
    # Define new window
    gameWin = GraphWin ("Find the Hole", 500, 500)
    gameWin.yUp()
    makeText(gameWin.getWidth() / 2, 30, "Click to find the Circle", gameWin)
    gameWin.getMouse()

    # Create circle at random position
    x = random.randrange(0 + radius, 500 - radius)
    y = random.randrange(0 + radius, 500 - radius)
    center = Point(x,y)
    circle = Circle(center, radius)
    user = gameWin.getMouse()
    
    clickCount = 0
    # Not in circle and under click count max
    while getShift(user,center) > radius and clickCount < clickLimit:
            clickCount += 1
            user.draw(gameWin)
            user = gameWin.getMouse()

    # If clicked inside circle
    if getShift(user,center) < radius:
        circle.setFill('green')
        makeText(420, 60, 'Level Complete!', gameWin)
        setOutline(circle, "black")
        circle.setFill('green')
        circle.draw(gameWin)
        reButton = makeColoredRect(Point(375, 45), 90, 40, 'yellow', gameWin)
        makeText(420, 25, "Replay?", gameWin)
        pt = gameWin.getMouse()
        gameWin.close()

        # Restart
        if isInside(pt, reButton):
            main()
            
    # If out of turns
    else:
        setOutline(circle, "black")
        circle.setFill('red')
        circle.draw(gameWin)
        makeText(420, 60, "You Lose", gameWin)
        reButton = makeColoredRect(Point(375, 45), 90, 40, 'yellow', gameWin)
        makeText(420, 25, "Replay?", gameWin)
        pt = gameWin.getMouse()
        gameWin.close()
        if isInside(pt, reButton):
            main()
        else:
            gameWin.close()

# Main Start
def main():
    # Creation of window
    win = GraphWin('Find the Circle', 400, 400)
    win.yUp()

    # Buttons
    greenButton = makeColoredRect(Point(75, 320), 80, 30, 'green', win)
    yellowButton = makeColoredRect(Point(75, 280), 80, 30, 'yellow', win)
    redButton = makeColoredRect(Point(75, 240), 80, 30, 'red', win)
    purpleButton  =makeColoredRect(Point(75, 200), 80, 30, 'purple', win)

    # Text on screen
    makeText(118, 305, "Level 1", win)
    makeText(118, 265, "Level 2", win)
    makeText(118, 225, "Level 3", win)
    makeText(118, 185, "Level 4", win)
    makeText(200, 385, "Find the Circle!", win)
    makeText(235, 305, "Number of tries: 20", win)
    makeText(235, 265, "Number of tries: 15", win)
    makeText(235, 225, "Number of tries: 10", win)
    makeText(230, 185, "Number of tries: 5", win)
    makeText(210, 45, "A game by Christopher Hernandez and Morgan Rose", win)
    makeText(win.getWidth() / 2, 360, "Click to choose a level difficulty", win)
    makeText(win.getWidth() / 2, 340, "Click anywhere else to close", win)

    # Get coordinate of mouse click
    pt = win.getMouse()
    win.close()

    # Starts game depending on difficulty
    if isInside(pt, greenButton):
        level(65,20)
        win.close()
    elif isInside(pt, yellowButton):
        level(45,15)
        win.close()
    elif isInside(pt, redButton):
        level(20,10)
        win.close()
    elif isInside(pt, purpleButton):
        level(5,5)
        win.close()
            
# Main Execution
main()
