def exercise1():
  f = open("ex3.txt", "rt")

  map_item = []
  for line in f:
    map_item.append(line.strip())

  f.close()
  
  coordinate_row, coordinate_col = 0, 0
  step_right, step_down = 3, 1
  map_rows_number = len(map_item) 
  map_cols_number = len(map_item[0])
  our_way = ""  # we're going to record our way

  # go thru
  while True:
    coordinate_row += step_down
    coordinate_col +=  step_right
    # Are we out of the map?
    if coordinate_col > map_cols_number - 1:
      coordinate_col = coordinate_col - map_cols_number # move
    # Record our way
    our_way += map_item[coordinate_row][coordinate_col]
    # Shall we continue?
    if coordinate_row >= map_rows_number - 1: break

  print(f'We encountered {our_way.count("#")} trees')


# for task 2 we need to create a function separately to avoid mess
def get_trees_number_walking_thru_map(map_item, step_right, step_down):
  our_way = ""  # record the way
  coordinate_row, coordinate_col = 0, 0 # start here
  map_rows_number = len(map_item) 
  map_cols_number = len(map_item[0])

  # go thru
  while True:
    coordinate_row += step_down
    coordinate_col +=  step_right
    # Are we out of the map?
    if coordinate_col > map_cols_number - 1:
      coordinate_col = coordinate_col - map_cols_number # move
    # Record our way
    our_way += map_item[coordinate_row][coordinate_col]
    # Shall we continue?
    if coordinate_row >= map_rows_number - 1: break
  
  return our_way.count('#')




def exercise2():
  f = open("ex3.txt", "rt")

  map_item = []
  for line in f:
    map_item.append(line.strip())

  f.close()

  trees_counter_multiplier = 1

  navigation_data = ((1,1), (3,1), (5,1), (7,1), (1,2))
  # Right 1, down 1.
  # Right 3, down 1. (This is the slope you already checked.)
  # Right 5, down 1.
  # Right 7, down 1.
  # Right 1, down 2.
  for pathway in navigation_data:
    trees_there = get_trees_number_walking_thru_map(
      map_item, pathway[0], pathway[1])
    trees_counter_multiplier *= trees_there
  
  print(f'The answer is {trees_counter_multiplier}')

    
exercise1()
exercise2()
