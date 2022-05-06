import random
import math

class Robot:
    def __init__(self,name ,colour,position = [0,0], angle_moved = 0):
        self.name = name
        self.colour = colour
        self.position = position
        self.angle_moved = angle_moved
        

    def mydetails(self,j = 0):
        print("Robot:  " , self.name)
        print("color is ",self.colour)
        print("Location is ", inal_loc[j])
        #print("Location is ", self.position)
        #print("Total angle moved ",self.angle_moved)
        print()
    
    # Function to move the robot from one place to
    #another at an angle theta degree
    def move(self,position,distance,angle,prev_angle):
        prev_angle += angle
        print("{} steps at {} degree".format(distance,angle))

        if angle != 90 or angle != 270:
            self.position[0] += distance * round(math.cos(math.radians(prev_angle)),3)
        self.position[1] += distance * round(math.sin(math.radians(prev_angle)), 3)
        
        print("current location is : ",self.position)
        print("Angle moved : ",prev_angle)
        
        return self.position , prev_angle
    
#This function will check whether there is a obstacles /
# robot in left side of robot or not
    
def no_obstacles(x,y,inal_loc,obstacles):
  for obj in obstacles:
    if obj[1] == y and obj[0] < x :
        return False

  for pos in inal_loc:
      if y == pos[1] and x > pos[0]:
        return False
  return True

#This function will return the position of robot
# Whether in the top or bottom boundary or in  mid region

def find_position(breadth,y):
  if y == 0:
    return 'Bottom boundary'
  if y == breadth:
    return 'Top boundary'
  return 'Mid Region'

# This function will find nearest obstacle

def obstacle_Co_ordinate(x,y,breadth,obstacles,inal_loc):
  minm = float('inf')
  x_cord = x
  y_cord = y

  for obj in obstacles:
    if obj[1] != y:
      if minm > abs(obj[1] - y):
        minm = abs(obj[1] - y)
        x_cord = obj[0]
        y_cord = obj[1]

  for pos in inal_loc:
    if pos[1] != y:
      if minm > abs(pos[1] - y):
        minm = abs(pos[1] - y)
        x_cord = pos[0]
        y_cord = pos[1]

  # if no obstacle is in above or below the robot
  # but obstacle is in left of robot
  if x_cord == x and y_cord == y:
    if y != breadth:
      y_cord = breadth - y
    else:
      y_cord = breadth - y//2
  return x_cord , y_cord



# This function will assemble the robot in left
# boundary of environment

def move_to_left(length,breadth,j,obstacles,inal_loc,final_pos):
  print()
  print(" j = ",j)
  print("initial ",inal_loc)
  x,y = inal_loc[j][0],inal_loc[j][1]

  '''
  if robot is on left boundary
  we don't need to do any thing
  '''
  if x == 0:
    print(" j1 = ",j)
    inal_loc[j][0] , inal_loc[j][1] = x,y
  else:
    print(" j2 = ",j)

    # if there is no obstacles/robots in left of robot
    if no_obstacles(x,y,inal_loc,obstacles):
      print(" j3 = ",j)
      x = 0
    else:
     Robot_position = find_position(breadth,y)

     # Co-ordinate of nearest obstacle
     x1 , y1 = obstacle_Co_ordinate(x,y,breadth,obstacles,inal_loc)
      
     
     '''
     If Robot in bottom Boundary
     '''
     if Robot_position == 'Bottom boundary':

       # If obstacle in top boundary
       if y1 == breadth:
         print(" j4 = ",j)
         y = ((breadth - y1//2)*x)//length
       else:
         # Obstacle not in top boundary
         print(" j5 = ",j)
         y = (y1*x)//length


     
     elif Robot_position == 'Mid Region':
       '''
       If Robot in Mid Region
       '''

       # Obstacle Above Robot
       if y1 > y:

         # obstacle in Top boundary
         if y1 == breadth:
           print(" j6 = ",j)
           y = (((y1 - y)*x)// (2*length ))+ y
         else:
           # obstcale not in top boundary
           print(" j7 = ",j)
           y = (((y1 - y)*x)// length )+ y
           
        
       else:
         # Obstacle below Robot

         # Obstacle in bottom boundary
         if y1 == 0:
           print(" j8 = ",j)
           y = -((y*x)//2*length) + y
         else:
           print(" j9 = ",j)
           y = ((y1 - y)*x)//length + y
            

     
     else:
       '''
       If Robot in Top Boundary
       '''

       # if obstacle in bottom boundary
       if y1 == 0:
         #print("y*x = ",(y*x))
         print(" j10 = ",j)
         y = -((y*x)//(2*length)) + y
       else:
         # if obstacle not in bottom boundary
         print(" j11 = ",j)
         y = ((y1 - y)*x)//length + y
     
        
  
  print(" j12 = ",j)
  x = 0
  print(" j = {}, x = {} y = {}".format(j,x,y))
  print()
  final_pos.append([j,x,y])
        
        
        
colors = ["red","blue","green","violet","orange","brown",
         "purple","cyan","indigo","yellow","grey"]

inal_loc = []
def is_valid(x,y,obstacles,inal_loc):
    if [x,y] in inal_loc:
        return False
    
    for obs in obstacles:
        if y == obs[1]:
            if obs[0]-5 <= x <= obs[0] + obs[2]+5:
                return False
    return True

def calc_inal_loc(robot_no , length,breadth,obstacles):
    print()
    print("Enter 1 or 2 for follwoing")
    print("1 Intialise position of robot randomly")
    print("2 Manually give the initial position")
    choice = int(input("pick: "))

    if choice == 1:
        while robot_no > 0:
            x_pos = random.randint(0,length)
            y_pos = random.randint(0, breadth)
            temp = [x_pos,y_pos]
            if is_valid(x_pos,y_pos,obstacles,inal_loc):
                inal_loc.append(temp)
                robot_no -= 1
        #print(inal_loc)
    else:
        print()
        print("Enter x axis and y axis in follwoing way")
        print("75 25")
        print("x_axis <= {} and y_axis <= {}".format(length,breadth))
        print()
        for i in range(0,robot_no):
            print("Enter x and y axis for robot{}".format(i+1))
            x_pos , y_pos = list(map(int,input().split()))
            inal_loc.append([x_pos,y_pos])
