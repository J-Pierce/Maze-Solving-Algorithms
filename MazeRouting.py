import Utils

def tremauxs():
    places ={}
    testOrder={North:[West,North,East,South],East:[North,East,South,West],South:[East,South,West,North],West:[South,West,North,East],}
    facing = North

    while get_entity_type() != Entities.Treasure:
        location = (get_pos_x(), get_pos_y())

        if location in places:
            pass
        else:
            places[location] = testOrder[facing][:]
        
        if move(places[location][0]):
            facing = places[location][0]

        newTest = places[location]
        newTest.pop(0)
        places[location] = newTest
    
def setup():
    if get_entity_type() != Entities.Bush:
        harvest()
    if get_ground_type() == Grounds.Soil:
        till()
    plant(Entities.bush)
    while can_harvest() == False: 
        Utils.water()
    use_item(Items.Weird_Substance, get_world_size()*num_unlocked(Unlocks.Mazes))

def optimalLine(vert,horz):
    if vert == 0:
        if horz > 0:
            return "Right"
        elif horz < 0:
            return "Left"
    elif horz == 0:
        if vert > 0:
            return "Up"
        elif vert < 0:
            return "Down"          
    elif horz > 0 and vert > 0:
        return "UpRight"
    elif horz > 0 and vert < 0:
        return "RightDown"
    elif horz < 0 and vert < 0:
        return "DownLeft"
    else:
        return "LeftUp"
            
   

def mazeRouting():
    goal_x,goal_y = measure()
    curr_x,curr_y= (get_pos_x(),get_pos_y())
    places ={}
    firstMove = True
    facing = North 
    optimalPath={"Up":[North, West, East, South],"Right":[East, North, South, West],"Down":[South, East, West, North],"Left":[West, South, North, East],
    "UpRight":[North, East, South, West],"RightDown":[East, South, West, North],"DownLeft":[South, West, North, East],"LeftUp":[West, North, East, South]}
    oppositeDirection={North:South,East:West,South:North,West:East}
    use_item(Items.Weird_Substance, get_world_size()*num_unlocked(Unlocks.Mazes))

    while (curr_x != goal_x or curr_y != goal_y):
        horz = goal_x-curr_x
        vert = goal_y-curr_y
        
        optimal = optimalLine(vert,horz)
        quickRoute = optimalPath[optimal]

        location = (curr_x,curr_y)

        if location in places:
            pass
        else:
            if firstMove == True:
                places[location] = quickRoute[:]
                firstMove = False
            else:
                addRoute = quickRoute[:]
                addRoute.remove(oppositeDirection[facing])
                addRoute.append(oppositeDirection[facing])
                places[location] = addRoute
        
        if move(places[location][0]):
            facing = places[location][0]

        newTest = places[location]
        newTest.pop(0)
        places[location] = newTest
        curr_x,curr_y= (get_pos_x(),get_pos_y())

def maze():
    setup()
    tremauxs()
    for i in range(298):
        mazeRouting()
    harvest()
    
maze()