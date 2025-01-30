from graphics import * #much easier to use rather than module.object
import random


def displayImages(images,canvas):#Camel Case
    for i,image in enumerate(images): #i,image show they come as a package
        img = Image(Point(120+200*(i%4),120+200*(i//4)),image)#class names begin with capital letter!!
        img.draw(canvas)

def convertPointToIndex(p):#dont change parameter values
    x = p.getX()
    y = p.getY()
    if x > 20 and x < 220 and y > 20 and y < 220:
        return 0
    if x > 220 and x < 420 and y > 20 and y < 220:
        return 1
    if x > 420 and x < 620 and y > 20 and y < 220:
        return 2
    if x > 620 and x < 820 and y > 20 and y < 220:
        return 3
    
    if x > 20 and x < 220 and y > 220 and y < 420:
        return 4
    if x > 220 and x < 420 and y > 220 and y < 420:
        return 5
    if x > 420 and x < 620 and y > 220 and y < 420:
        return 6
    if x > 620 and x < 820 and y > 220 and y < 420:
        return 7
    
    if x > 20 and x < 220 and y > 420 and y < 620:
        return 8
    if x > 220 and x < 420 and y > 420 and y < 620:
        return 9
    if x > 420 and x < 620 and y > 420 and y < 620:
        return 10
    if x > 620 and x < 820 and y > 420 and y < 620:
        return 11
    
    if x > 20 and x < 220 and y > 620 and y < 820:
        return 12
    if x > 220 and x < 420 and y > 620 and y < 820:
        return 13
    if x > 420 and x < 620 and y > 620 and y < 820:
        return 14
    if x > 620 and x < 820 and y > 620 and y < 820:
        return 15
    
    return -1 #you dont NEED an else if there's a return in the previous statement

def win(images):
    if images[0] != './gifs//1.gif':
        return False
    if images[1] != './gifs//2.gif':
        return False
    if images[2] != './gifs//3.gif':
        return False
    if images[3] != './gifs//4.gif':
        return False
    if images[4] != './gifs//5.gif':
        return False
    if images[5] != './gifs//6.gif':
        return False
    if images[6] != './gifs//7.gif':
        return False
    if images[7] != './gifs//8.gif':
        return False
    if images[8] != './gifs//9.gif':
        return False
    if images[9] != './gifs//10.gif':
        return False
    if images[10] != './gifs//11.gif':
        return False
    if images[11] != './gifs//12.gif':
        return False
    if images[12] != './gifs//13.gif':
        return False
    if images[13] != './gifs//14.gif':
        return False
    if images[14] != './gifs//15.gif':
        return False
    if images[15] != './gifs//blank.gif':
        return False
    return True
    
def neighbors(index):
    if index == 0:
        return [1,4]
    if index == 1:
        return [0,2,5]
    if index == 2:
        return [1,3,6]
    if index == 3:
        return [2,7]
    if index == 4:
        return [0,5,9]
    if index == 5:
        return [1,4,6,9]
    if index == 6:
        return [2,5,7,10]
    if index == 7:
        return [3,6,11]
    if index == 8:
        return [4,9,12]
    if index == 9:
        return [5,8,10,13]
    if index == 10:
        return [6,9,11,14]
    if index == 11:
        return [7,10,15]
    if index == 12:
        return [8,13]
    if index == 13:
        return [9,12,14]
    if index == 14:
        return [10,13,15]
    if index == 15:
        return [11,14]
    return []

def findBlank(images,nbrs):
    print(nbrs)
    for nbr in nbrs:
        print(images[nbr])
        if images[nbr] == './gifs/blank.gif':
            return nbr
    return -1 #since returning index, -1 indicates improper 

def swapTiles(index,blank_index,images,canvas):
    images[blank_index], images[index] = images[index], images[blank_index] #swaps the FILE NAMES
    x = 120+200*(blank_index%4)
    y = 120+200*(blank_index//4)
    img = Image(Point(x,y),images[blank_index])
    img.draw(canvas)
    x = 120+200*(index%4)
    y = 120+200*(index//4)
    img = Image(Point(x,y),images[index])
    img.draw(canvas)


def main():
    canvas = GraphWin("Graphics!!",840,840)#short for window
    canvas.setBackground("pink")
    
    images = []
    for i in range(1,16):
        images.append('./gifs/' + str(i) + '.gif')
    images.append('./gifs/blank.gif')
    random.shuffle(images)
    displayImages(images,canvas)

    while True:
        
        p = canvas.getMouse()
        index = convertPointToIndex(p)
        print(index)
        if index != -1:
            nbrs = neighbors(index)
            print(nbrs)
            blank_index = findBlank(images,nbrs)
            print(blank_index)
            if blank_index != -1:
                swapTiles(index,blank_index,images,canvas)
        if win(images):
            displayImages(images['./gifs/win.gif'],canvas)
            break
    
    

    
    canvas.getMouse()
    canvas.close()

main()
