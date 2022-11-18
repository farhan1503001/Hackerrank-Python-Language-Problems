import random
def random_walk(threshold:int)->None:
  start=0
  count=0
  print("Position= ",start)
  while(True):
    
    decision=random.choice([-1,1]) #Will choose to increament or decreament
    #print(decision)
    max=start
    start=start+decision
    print("Position= ",start)
    if start>max:
      max=start
    if start==threshold or start==-threshold:
      print("Finished After {0} steps() ".format(count))
      print("Max Position = ",max)
      break
    else:
      
      count=count+1


random_walk(3)
