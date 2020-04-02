import pygame

def main():
    word = getWord()
    pygame.init()

    win = pygame.display.set_mode((500, 500))

    pygame.display.set_caption("hello")

    clock = pygame.time.Clock()

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
        win.fill((255,255,255))
        pygame.draw.line(win,((0,0,0)),(0,450),(500,450),)
        drawHang(win)
        drawMan(win)
        get_spaces = drawWord(win,len(word))
        displayWord(win, get_spaces, word)
        pygame.display.update()
        clock.tick(60)

def drawHang(win):
    # Draw base of hanger
    pygame.draw.line(win,((0,0,0)),(100,350),(300,350),12)
    # Draw Vertical
    pygame.draw.line(win,((0,0,0)),(200,100),(200,350),12)
    # Draw Horizontal
    pygame.draw.line(win,((0,0,0)),(195,100),(350,100),12)
    # Draw Rope
    pygame.draw.line(win,((0,0,0)), (340,100),(340,150), 2)

def drawMan(win):
    # Draw the head
    pygame.draw.circle(win,((0,0,0)),(340,170),20)
    # Draw the body
    pygame.draw.line(win,((0,0,0)), (340,190),(340,265), 2)
    # Draw Left Leg
    pygame.draw.line(win,((0,0,0)), (340,265),(305,300), 2)
    # Draw Right Leg
    pygame.draw.line(win,((0,0,0)), (340,265),(375,300), 2)
    #Draw Left Arm
    pygame.draw.line(win,((0,0,0)), (340,215),(305,250), 2)
    # Draw Right Arm
    pygame.draw.line(win,((0,0,0)), (340,215),(375,250), 2)

def drawWord(screen, lenWord):
    start_x =15
    end_x = 35
    y = 490
    locations = []
    for i in range(lenWord):
        x_avg = (start_x + end_x)/2
        locations.append([x_avg,y-10])
        pygame.draw.line(screen,(0,0,0),(start_x,y),(end_x,y))
        start_x = end_x + 5
        end_x = start_x + 20
    return locations

def displayWord(screen, locations, word):
    font = pygame.font.Font(None, 20)
    for letters in word:
        text = font.render(letters, True, (0,0,0), (255,255,255))
        textRect = text.get_rect()
        for spaces in locations:
            textRect.center = (spaces[0], spaces[1])
        screen.blit(text, textRect)


def getWord():
    word = input("What word are we making?\n\n")
    print(chr(27)+"[2J")
    return word











if __name__ == '__main__':
    main()
    pygame.quit()