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

def maze():
    setup()
    for i in range(299):
        tremauxs()
        use_item(Items.Weird_Substance, get_world_size()*num_unlocked(Unlocks.Mazes))
    harvest()
    
maze()