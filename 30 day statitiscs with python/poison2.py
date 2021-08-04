if __name__=='__main__':
   average_a,average_y=map(float,input().split())
   cost_a=160+40*(average_a+average_a**2)
   cost_b=128+40*(average_y+average_y**2)
   print(cost_a)
   print(cost_b)