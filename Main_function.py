from Robot_package_2 import *
from Environment import create_environment,set_obstacle
import multiprocessing
import matplotlib.pyplot as plt

if __name__ == "__main__":
  manager = multiprocessing.Manager()
  final_pos = manager.list()

  # Create environment
  length , breadth = create_environment()
  r = []

  # Enter detail of obstacle in environment
  obstacles = set_obstacle()
  print("obstacles are.. \n",obstacles)

  count = int(input("Total robot = "))
  calc_inal_loc(count,length,breadth,obstacles)
  for i in range(0,count):
    name = 'r'+str(i)
    r.append(Robot(name,colors[i%11],inal_loc[i]))

  # Representing obstacles
  for i  in range(0,len(obstacles)):
    plt.axhline(y = obstacles[i][1]/breadth, xmin = obstacles[i][0] /length,
                xmax = (obstacles[i][0] + obstacles[i][2])/length ,
                color = 'r',linestyle = '-')
  
  # Representing robot
  for i in range(0,count):
    plt.axhline(y = inal_loc[i][1]/breadth ,
                xmin = inal_loc[i][0]/length,
                xmax = (inal_loc[i][0] +1)/length,
                color = 'b',linestyle = '-')
    
  plt.xlabel('x - axis')
  plt.ylabel('y - axis')
  plt.show()
  
  for x in range(0,count):
    r[x].mydetails(x)
  print()

  
  # Assemble all the robot in left boundary
  '''
  for x in range(0,count):
    r[x].move_to_left(length,breadth,x,obstacles)
  '''
  process_robot = []
  for i in range(count):
    process_robot.append(multiprocessing.Process(target = move_to_left ,
                                                 args = (length,breadth,i,obstacles,inal_loc,final_pos )))

  for p in range(count):
    process_robot[p].start()

  for q in range(count):
    process_robot[q].join()

  print()
  final_pos.sort()
  #print()
  #print("pos = ",final_pos)
  for i in range(0,count):
    inal_loc[i] = [final_pos[i][1],final_pos[i][2]]
    
  for x in range(0,count):
    r[x].mydetails(x)
                  
  print()
  plt.show()
  # Representing obstacles
  for i  in range(0,len(obstacles)):
    plt.axhline(y = obstacles[i][1]/breadth, xmin = obstacles[i][0] /length,
                xmax = (obstacles[i][0] + obstacles[i][2])/length ,
                color = 'r',linestyle = '-')
  
  # Representing robot
  for i in range(0,count):
    plt.axhline(y = inal_loc[i][1]/breadth ,
                xmin = inal_loc[i][0]/length,
                xmax = (inal_loc[i][0] +0.4)/length,
                color = 'b',linestyle = '-')
    
  plt.xlabel('x - axis')
  plt.ylabel('y - axis')
  
  plt.show()
  
  
