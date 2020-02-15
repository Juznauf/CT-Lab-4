# Name: Muhammad Naufal
# Section: G5

# lab4

# All statements should only be in functions. Do not include statements outside functions in this file.


def select_tweeters(followers):
  # currently, this function always returns the first five users
  # obviously this arbitrary selection will result in a lousy quality score even though it's a "correct" answer :-/


  """
  Objective is to return the top 5 twitter users given the constraints, must be unique followers, runtime is 1 min 
  """

  def max_score(currArray,newArray,current_score):
    """helper function to do comparison"""
    
    counter = 0
    final_arr = []
    for i in range(len(currArray)):
      # replace one array in the combined array with a new array at each iteration
      res_arr = currArray[:]
      res_arr.pop(i)
      res_arr.append(newArray)
      temp2 = []
      for e in res_arr:
        # combine all the list together in a temp2 array
        temp2 += e[1]
      if len(set(temp2)) > counter:
        final_arr = res_arr[:]
        counter = len(set(temp2))
    if counter > current_score:
      # return the new ls and the current score
      return final_arr, counter
    else:
      return currArray, current_score
      
  
  current_score = 0
  result_ls = []

  indexed_ls = list(enumerate(followers))
  indexed_ls.sort(key = lambda x:x[1], reverse = True)

  for e in indexed_ls:
    if len(result_ls) == 5:
      result_ls, current_score = max_score(result_ls,e,current_score)
      # print(result_ls, current_score)
      # break

    elif len(result_ls) == 4:
      result_ls.append(e)
      temp = []
      for i in range(len(result_ls)):
        temp += result_ls[i][1]
      current_score = len(set(temp))
    else:
      result_ls.append(e)


  final_ls = []
  for e in result_ls:
    final_ls.append(e[0])

  return final_ls



if __name__ == "__main__":

  # test case to check if above program works, if yes then we can call the main programme in lab4_main.py

  test_case = [[2],[0,3],[0,1],[1,2,4,5],[1,6,10],[],[7,8],[],[],[8],[9]]
  print(select_tweeters(test_case))
