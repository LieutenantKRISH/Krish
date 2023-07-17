if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_scores = sorted(set(arr),reverse = True )
    
    if len(unique_scores) > 1:
        runner_up_score = unique_scores[1]
        print(runner_up_score)
    else:
        print("No runner-up score available")


Explanation:-
(1)   if __name__ == '__main__'::
This line checks if the code is being run as the main program and not imported as a module.
It ensures that the following code block will only execute if the file is being run directly.


(2)   n = int(input()):
This line prompts the user to enter the number of scores as an integer.

(3)  arr = map(int, input().split()):
This line prompts the user to enter the scores separated by spaces using input().
input().split() splits the input by spaces, creating a list of score strings.
map(int, ...) applies the int function to each element of the list, converting them into integers.
The resulting map object is then assigned to arr.

  
(4)  unique_scores = sorted(set(arr), reverse=True):
This line creates a set of unique scores by converting arr to a set using set(arr).
sorted(..., reverse=True) sorts the set of unique scores in descending order.
The sorted list of unique scores is assigned to unique_scores.

(5)  if len(unique_scores) > 1::
This line checks if the length of unique_scores is greater than 1, indicating that there is a runner-up score available.
If the condition is true, the code proceeds to the next line.

(6)  runner_up_score = unique_scores[1]:
This line assigns the second element (index 1) from the unique_scores list to runner_up_score.
Since the list is sorted in descending order, the second element represents the runner-up score.

(7)  print(runner_up_score):
This line prints the runner-up score.

(8)  else:
If the condition in the if statement from step 5 is false, the code executes the block under the else statement.
print("No runner-up score available"):

This line prints the message "No runner-up score available" when there is no runner-up score.
