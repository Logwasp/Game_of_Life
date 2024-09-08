import pygame
import time

WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)
BLACK = (  0,   0,  0)
(width, height) = (800, 800)

running = True
simulationStarted = False

#Class for each cell
class Cell:
    def __init__(self, xpos, ypos, state):
        self.xpos = xpos
        self.ypos = ypos
        self.state = state

    

#Class for the grid
class Grid:
    def __init__(self, gridWidth, gridHeight):
        self.gridWidth = gridWidth
        self.gridHeight = gridHeight

        self.grid = []
        
        for i in range(gridWidth):
            for j in range(gridHeight):
                self.grid.append(Cell(i, j, 0))



#Function to draw the grid
def drawGrid(Grid):
    cellsize = width / Grid.gridWidth
    for i in range(Grid.gridHeight):
        for j in range(Grid.gridWidth):
            if Grid.grid[i*Grid.gridWidth + j].state == 1:
                pygame.draw.rect(screen, WHITE, [j*cellsize, i*cellsize, cellsize, cellsize])
            else:
                pygame.draw.rect(screen, BLACK, [j*cellsize, i*cellsize, cellsize, cellsize])



#Function to check if cell is a edge cell
def isEdgeCell(inputgrid, cell):
    cellIndex = inputgrid.grid.index(cell)
    if (cellIndex % inputgrid.gridWidth == 0) or (cellIndex % inputgrid.gridWidth == inputgrid.gridWidth - 1):
        return True
    elif (cellIndex < inputgrid.gridWidth) or (cellIndex > inputgrid.gridWidth * inputgrid.gridHeight - inputgrid.gridWidth):
        return True
    else:
        return False



#Function to count the number of neighbors
def countNeighbors(grid, cell):
    if isEdgeCell(grid, cell):
        return 0
    
    cellIndex = grid.grid.index(cell)
    neighborCount = 0

    #Check right neighbor
    if grid.grid[cellIndex + 1].state == 1 :
        neighborCount += 1
    
    #Check left neighbor
    if grid.grid[cellIndex - 1].state == 1:
        neighborCount += 1

    #Check top neighbor
    if grid.grid[cellIndex - grid.gridWidth].state == 1:
        neighborCount += 1
    
    #Check bottom neighbor
    if grid.grid[cellIndex + grid.gridWidth].state == 1:
        neighborCount += 1
    
    #Check top right neighbor
    if grid.grid[cellIndex - grid.gridWidth + 1].state == 1:
        neighborCount += 1

    #Check top left neighbor
    if grid.grid[cellIndex - grid.gridWidth - 1].state == 1:
        neighborCount += 1
    
    #Check bottom right neighbor
    if grid.grid[cellIndex + grid.gridWidth + 1].state == 1:
        neighborCount += 1
    
    #Check bottom left neighbor
    if grid.grid[cellIndex + grid.gridWidth - 1].state == 1:
        neighborCount += 1
    
    return neighborCount



#Function to reproduce

def reproduce(grid):
    newGrid = [cell.state for cell in grid.grid]  # Create a copy of the current grid states

    for cell in grid.grid:
        neighbors = countNeighbors(grid, cell)

        # Apply the rules of the Game of Life
        if cell.state == 1:
            if neighbors < 2 or neighbors > 3:
                newGrid[grid.grid.index(cell)] = 0  # Cell dies
            else:
                newGrid[grid.grid.index(cell)] = 1  # Cell stays alive
        else:
            if neighbors == 3:
                newGrid[grid.grid.index(cell)] = 1  # Cell becomes alive

    # Update the grid with the new states
    for i, cell in enumerate(grid.grid):
        cell.state = newGrid[i]
    

        
        




def main():
    global running, screen, simulationStarted
    
    #Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Game of Life")
    screen.fill(BLACK)

    #Create grid
    realgrid = Grid(40, 40)


    realgrid.grid[86].state = 1
    realgrid.grid[88].state = 1
    realgrid.grid[127].state = 1
    realgrid.grid[128].state = 1
    realgrid.grid[167].state = 1

    drawGrid(realgrid)
    pygame.display.update()

    print(countNeighbors(realgrid, realgrid.grid[47]))

    

    

    
    while running:
        ev = pygame.event.get()


        if simulationStarted:
            time.sleep(.4)
            reproduce(realgrid)
            drawGrid(realgrid)
            pygame.display.update()

        for event in ev:

            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                print(f'Mouse clicked at {x}, {y}')

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    simulationStarted = True



            if event.type == pygame.MOUSEBUTTONDOWN and not simulationStarted:
                #Make is such that when I click on a cell, it changes state
                x, y = pygame.mouse.get_pos()
                print(f'Mouse clicked at {x}, {y}')
                cellsize = width / realgrid.gridWidth
                x = int(x // cellsize)
                y = int(y // cellsize)
                print(f'Cell clicked at {x}, {y}')
                realgrid.grid[y*realgrid.gridWidth + x].state = 1
                drawGrid(realgrid)
                pygame.display.update()


            if event.type == pygame.QUIT:
                running = False



def getPos():
    pos = pygame.mouse.get_pos()
    return (pos)



if __name__ == '__main__':
    main()