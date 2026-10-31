function add(a, b) {
  return a + b;
}

function isPositive(n) {
  return n > 0;
}

// Deliberately not exercised by any test: produces NoCoverage mutants.
function multiply(a, b) {
  return a * b;
}

export { add, isPositive, multiply };
