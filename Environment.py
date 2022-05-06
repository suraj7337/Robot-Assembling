def create_environment():
  global length,breadth,x_axis,y_axis
  print("Enter data for environment: ")
  length = int(input("Enter length: "))
  breadth = int(input("Enter breadth: ")) 
  print("Co-ordinate of rectangular area (4 - corners) is:")
  print("[0,0]  {}  {}  {}   in clockwise direction".format
        ([0,breadth],[length,breadth],[length , 0]))
  print()

  return length,breadth

def set_obstacle():
  obstacles = []
  obstacle_no = int(input("Enter number of obstacle "))
  print("for obstacle enter three parameter ")
  print("x_axis y_axix length ")
  print()
  while obstacle_no > 0:
    obs = list(map(int,input().split()))
    assert obs[2] < length - 10, "Length of obstacle will be less than length of environment"
    obstacles.append(obs)
    obstacle_no -= 1
    
  return obstacles

  
  


  



        


