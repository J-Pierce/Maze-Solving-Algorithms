def move_drone(target_x,target_y):
	move_x = target_x - get_pos_x()
	move_y = target_y - get_pos_y()
	while (move_x != 0 or move_y != 0):
		
		n = get_world_size()

		isSuccess = True
		if (0 < move_x and move_x <= n/2) or (-n <= move_x and move_x < -n/2):
			if move(East) == False:
				isSuccess = False
		elif (-n/2 <= move_x and move_x < 0) or (n/2 < move_x and move_x <= n):
			if move(West) == False:
				isSuccess = False
		elif (0 < move_y and move_y <= n/2) or (-n <= move_y and move_y < -n/2):
			if move(North) == False:
				isSuccess = False
		elif (-n/2 <= move_y and move_y < 0) or (n/2 < move_y and move_y <= n):
			if move(South) == False:
				isSuccess = False

		if isSuccess == False:
			return isSuccess
		
		move_x = target_x - get_pos_x()
		move_y = target_y - get_pos_y()
	return True

def water():
	if get_water() <0.5:
		if num_items(Items.Water) > 0:
			use_item(Items.Water)

def fertalise():
	if num_items(Items.Fertilizer) > 0:
		use_item(Items.Fertilizer)
