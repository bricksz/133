from tkinter import *
from random import choice
from time import clock

# sx and sy are the horizontal and vertical speed of the ball
# in pixels per animation step

block, ball, sx, sy = None, None, 5, 5

# returns position of the *center* of the ball
def ballPosition():
    x1, y1, x2, y2 = list(field.coords(ball))
    return [(x1+x2)/2, (y1+y2)/2]

def startGame():
    global startTime, ball, block
    # remember to delete block and ball from previous game
    if block:
        field.delete(block)
    block = None
    if ball:
        field.delete(ball)
    # place ball at random
    upperLeftX = choice(list(range(290)))
    upperLeftY = choice(list(range(290)))
    ball = field.create_oval(upperLeftX, upperLeftY,
                             upperLeftX+10, upperLeftY+10,
                             fill='blue')
    startTime = clock()
    animate()

def animate():
    global sx, sy
    pattern = 'Elapsed time: {0:.1f} seconds'
    timeDisplay['text'] = pattern.format(clock()-startTime)
    x, y = ballPosition()
    hitVertical = hitBlock() and blockType == 'vertical'
    if x+sx>300 or x+sx<0 or hitVertical:
        sx *= -1
    hitHorizontal = hitBlock() and blockType == 'horizontal'
    if y+sy>300 or y+sy<0 or hitHorizontal:
        sy *= -1
    field.move(ball, sx, sy)
    if not inGoal():
        root.after(20, animate)

# Only one block at a time; delete one before creating the next

def leftClick(event):
    global block, blockType
    if block:
        field.delete(block)
    block = field.create_rectangle(event.x-20, event.y,
                                       event.x+20, event.y+6,
                                       fill='light green')
    blockType = 'horizontal'

def rightClick(event):
    global block, blockType
    if block:
        field.delete(block)
    block = field.create_rectangle(event.x, event.y-20,
                                       event.x+6, event.y+20,
                                       fill='light green')
    blockType = 'vertical'


# return True if the center of the ball is inside the
# block’s boundary

def hitBlock():
    if not block:
        return False
    ballX, ballY = ballPosition()
    blockX1, blockY1, blockX2, blockY2 = field.coords(block)
    return (blockX1 <= ballX <= blockX2 and blockY1 <= ballY <= blockY2)

# return True if the center of the ball is inside the
# goal area

def inGoal():
    ballX, ballY = ballPosition()
    return 0 <= ballX <= 25 and 275 <= ballY <= 300

root = Tk()

timeDisplay = Label(root)
timeDisplay.pack()

field = Canvas(root, width=300, height=300, bg='light blue')
field.pack()

startButton = Button(root, command=startGame, text='Go')
startButton.pack()

# the goal
field.create_rectangle(0, 275, 25, 300, fill='red')
field.bind('<ButtonPress-1>', leftClick)
field.bind('<ButtonPress-3>', rightClick)

mainloop()
