#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const numbers = process.argv.slice(2).map(Number); // Extracting numbers from command line arguments
  const sortedNumbers = numbers.sort((a, b) => b - a); // Sorting numbers in descending order
  const secondLargest = sortedNumbers[1]; // Getting the second largest number
  console.log(secondLargest);
}

