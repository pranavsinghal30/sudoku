path = "sudoku.csv"

import pandas as pd
import numpy as np
import time
from copy import deepcopy

df = pd.read_csv(path)

def sudoko_display(arr):
  arr = arr.astype(np.str)
  for i in range(arr.shape[0]):
    if i%3 ==0 :
      print("-------------------------")
    for j in range(0,arr.shape[1],3):
      if j == 0:
        print("|",end = " ")
      print(" ".join(arr[i][j:j+3]),end=" ")
      print("|",end = " ")
    print()
    if i==8 :
      print("-------------------------")



def solve(arr1):
  arr = deepcopy(arr1)
  empty_pos = find_empty(arr)
  #print("sudoko grid:")
  #sudoko_display(arr)
  #print("looking for position"+str(empty_pos))
  if empty_pos == None:
    return arr
  valid = find_valid(arr,empty_pos)
  #print("valid numbers for position "+str(empty_pos)+" are "+str(valid))
  if len(valid) != 0:
    for n in valid:
      #print("setting "+str(empty_pos)+" as "+str(n))
      arr[empty_pos] = n
      result = solve(arr)
      if not result is None:
        if find_empty(result) == None:
          return result
  #else:
    #print("No valid numbers so going back")
  
def find_empty(arr):
  positions = np.where(arr==0)
  if len(positions[0])>0:
    position_row = positions[0][0]
    position_col = positions[1][0]
    return (position_row,position_col)
  return None
def find_valid(arr,pos):
  row = pos[0]
  col = pos[1]
  valid = []
  sub_row = (3*(pos[0]//3),3*(pos[0]//3)+3)
  sub_col = (3*int(pos[1]//3),3*(pos[1]//3)+3)
  sub_arr = arr[sub_row[0]:sub_row[1],sub_col[0]:sub_col[1]]
  for i in range(1,10):
    if np.array(arr[row,:] == i).sum() ==0:
      if np.array(arr[:,col] == i).sum() ==0:
        if np.array(sub_arr == i).sum() ==0:
          valid.append(i)
  return valid

def solver(row):
  string = row['quizzes']
  arr = np.array(list(string)).reshape(9,9).astype(np.int8)
  start_time = time.time()
  sudoko_display(arr)
  result = solve(arr)
  print("\n\nSolution:")
  sudoko_display(result)
  return (time.time()-start_time)


solver(df.sample(n=1).iloc[0,:])

