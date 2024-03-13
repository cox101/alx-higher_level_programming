#!/usr/bin/node

function factorial(n) {
  if (n < 0) {
    return -1; // Negative numbers don't have factorials, returning -1 as an indicator
  }
  if (n === 0 || isNaN(n)) {
    return 1; // Factorial of 0 or NaN is 1
  }
  return n * factorial(n - 1); // Recursive call to compute factorial
}

const input = Number(process.argv[2]); // Parse the input from command line arguments

console.log(factorial(input)); // Calculate and print the factorial

