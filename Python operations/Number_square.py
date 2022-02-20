def number_square(min,max):
  real_max=max-min+1
  print(real_max)
  for starter in range(min,real_max+1):
    val=starter
    for i in range(starter,real_max+starter):
      print(val,end=" ")
      val=val+1
      if val>max:
        val=min
    print()
    
if __name__=='__main__':
    number_square(2,5)
