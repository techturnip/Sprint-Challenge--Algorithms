#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) We have a single loop that appears would only run 2 times, so the runtime complexity would be O(n).


b) The outer loop will run n times for a complexity O(n) and the inner loop will run less than n times `j *= 2` for a complexity of O(log n). O(n*log(n))


c) The if statement for the base case is O(n) and the recursive call O(n-1) and the fn will simply have O(n) complexity.

## Exercise II

Given this problem I think that since we already have a sorted array of floors with the n story building
and the egg breaks at floor >= f, we can minimize the number of broken eggs by implementing a similar
algorithm to our merge sort algorithm, but instead of merging we would be eliminating lists of floors.

Finding f with the least amount of eggs dropped, we would need to find the middle floor (split the array)
and drop an egg from that point and test if it the egg breaks.

If the egg breaks we can eliminate the array of floors > f. Then we will split the left array and repeat
until we reach floor f.

The time complexity, would likely be O(log(n)) since we have an n-story building and we are eliminating half
as we recurse will always run less than n times.
