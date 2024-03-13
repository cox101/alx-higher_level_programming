#!/usr/bin/node

const computeFactorial = (n) => {
  // Base case: if n is NaN or less than 0, return 1
  if (isNaN(n) || n < 0) {
    return 1;
  }
  // Base case: if n is 0, return 1 (factorial of 0 is defined as 1)
  if (n === 0) {
    return 1;
  }
  // Recursive case: compute factorial recursively
  return n * computeFactorial(n - 1);
};

// Parsing the first argument as an integer
const num = parseInt(process.argv[2]);

// Computing the factorial
const factorial = computeFactorial(num);

// Printing the factorial
console.log(factorial);

