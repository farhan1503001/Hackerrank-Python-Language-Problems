def one_to_one(A,B,C):
  """
  A function is one to one if every element of C is unique
  A: Input area
  B: Output area
  C: Outputs of the input

  Returns whether the function is one to one or not
  """
  #First check if the outputs are in B
  if len(C)>len(B):
    print("Not a one to one function")
    return False
  for value in C:
    if value not in B:
      print("Not a one to one function")
      return False

  memory_map={}
  for value in C:
    if value not in memory_map:
      memory_map[value]=True
    else:
      #Many to one relation found
      print("Not one to one function")
      return False
  print("One to one function")
  return True


def onto(A,B,C):
  """
  A function is onto if all values of B are in C

  A: Input area
  B: Output area
  C: Outputs of the input

  Returns whether the function is one to one or not  
  """
  for element in B:
    if element not in C:
      print("Not a onto function")
      return False
  print("Onto Function")
  return True

def one_to_one_c(A,B,C):
  #Same as one to one just reverse
  if len(A)!=len(C):
    print("Not one to one correspondence")
    return False
  #check if inputs are present in A
  for value in A:
    if value not in B:
      print("Not one to one correspondence")
      return False
  #Now check only one time present
  memory_map={}
  for value in C:
    if value not in memory_map:
      memory_map[value]=True
    else:
      #Many to one relation found
      print("Not one to one correspondence")
      return False
  print("One to one correspondence")
  return True  


if __name__ == '__main__':
    A=[1,2,3,4]
    B=['a','b','c','d']
    #C=['d','b','c','a']
    output={1:'d',2:'b',3:'c',4:'a'}
    input_list=[]
    out_list=[]
    for num  in output.keys():
       input_list.append(num)
    for value in output.values():
    #print(value)
        out_list.append(value)
    one_to_one(A,B,out_list)
    onto(input_list,B,out_list)
    one_to_one_c(input_list,A,out_list)