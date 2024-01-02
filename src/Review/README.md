# HW 5
This section will combine what we've learned to build on our logic ability, and to review what we've covered.

- Write a function fuel_cost that takes liters and pricePerLitre (in dollar) as arguments to calculate the cost of purchasing fuel.

Purchases of 2 or more liters get a discount of 5 cents per liter, purchases of 4 or more liters get a discount of 10 cents per liters, and so on every two liters, up to a maximum discount of 25 cents per liter. But total discount per liter cannot be more than 25 cents. Return the total cost rounded to 2 decimal places.

- Complete the function ints_between that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.

For example:
ints_between(1,5) -> [1,2,3,4,5]

- While mpg (miles per gallon) is a common unit of measurement for fuel economy in North America, for Europe the standard unit of measurement is generally liter per 100 km. Conversion between these units is somewhat hard to calculate in your head, so your task here is to implement a simple convertor in both directions.

Write two Functions
mpg2lp100km() converts from miles per gallon to liter per 100 km.
lp100km2mpg() converts in the opposite direction.
Output
The output of both functions should be a number rounded to 2 decimal places.

Examples
mpg2lp100km(42) returns 5.6
lp100km2mpg( 9) returns 26.13

For this kata, use U.S. gallon, not imperial gallon.

1 gallon = 3.785411784 liters
1 mile = 1.609344 kilometers

- Write a function for called sticky_calculator. This calculator works slightly different than normal.

Whenever you add add, subtract, multiply or divide two numbers the two numbers first stick together:

For instance:

50 + 12 becomes 5012
and then the operation is carried out as usual:

(5012) + 12 = 5024
Task
It is your job to create a function which takes 3 parameters:

stickyCalc(operation, val1, val2)
which works just like Frank's sticky calculator

Some Examples
stickyCalc('+', 50, 12)     // Output: (5012 + 12) = 5024
stickyCalc('-', 7, 5)       // Output: (75 - 5) = 70
stickyCalc('*', 13, 20)     // Output: (1320 * 20 ) = 26400
stickyCalc('/', 10, 10)     // Output: (1010 / 10) = 101

- This challenge is about feature requests for a project. Feature requests have been piling up and you need a way to make global estimates of the time it would take to implement them all. If you estimate feature A to take 4 to 6 hours to implement, and feature B to take 2 to 5 hours, then in the best case it will only take you 6 (4 + 2) hours to implement both features, and in the worst case it will take you 11 (6 + 5). In the average case, it will take you 8.5 hours.

To help you streamline the estimation process, write a function named global_estimate that returns a tuple of the global best case, average case and worst case given a tuple of tuples representing best case and worst case guesses.

For example,

estimates = ((1, 2), (3, 4))
global_estimate(estimates) == (4, 5, 6)
For example,

estimates = [[1, 2], [3, 4]]
globalEstimate(estimates) == [4, 5, 6]
Don't worry about rounding or invalid input.

- You will create a function named add. This function will return the sum of all the arguments. Sounds easy, doesn't it??

Well here's the twist. The inputs will gradually increase with their index as parameter to the function.

  add(3,4,5); 
  /*
  returns ( 3 * 1 ) + ( 4 * 2 ) + ( 5 * 3 ) = 26
  */
Remember the function will return 0 if no arguments are passed.

Example
  add(); //=> 0
  add(1,2,3); //=> 14
  add(1,4,-5,5); //=> 14

- Write a function named "generate" that generate the sequence of numbers which starts from the "From" number, then adds to each next term the "Step" number until the "To" number. For example:

generate(10, 20, 10) = [10, 20] # "From" = 10, "Step" = 10, "To" = 20
generate(10, 20, 1) = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] 
generate(10, 20, 5) = [10, 15, 20]
If next term is greater than "To", it can't be included into the output array:

generate(10, 20, 7) = [10, 17]
If "From" bigger than "To", the output array should be written in reverse order:

generate(20, 10, 2) = [20, 18, 16, 14, 12, 10]

Don't forget about input data correctness:
generate(20, 10, 0) = []
generate(10, 20, -5) = []
"From" and "To" numbers are always integer, which can be negative or positive independently. "Step" can always be positive.

- Write a function named find_missing that will take a list of numbers and returns a list of numbers.

Every preceding number is smaller than the one following it.

Some numbers will be missing, for instance:

[-3,-2,1,5] //missing numbers are: -1,0,2,3,4
Your task is to return an array of those missing numbers:

[-1,0,2,3,4]