//https://observablehq.com/@rreusser/computing-with-the-bailey-borwein-plouffe-formula
function S(j, n) {
  // Lefthand summation. Add a number of terms equal
  // to the starting digit. Most of the time is spent
  // in this loop.
  let left = 0;
  for (let k = 0; k <= n; k++) {
    let r = 8 * k + j;
    left = mod(left + modPow(16, n - k, r) / r, 1);
  }

  // Righthand summation. Add a small number of terms
  // until the result stops changing.
  let right = 0;
  for (let k = n + 1; ; k++) {
    let rnew = right + 16 ** (n - k) / (8 * k + j);
    if (right === rnew) break;
    right = rnew;
  }

  return left + right;
}
function mod(a,b){
    return a % b;
}

function piBBP(d, n) {
  // Seems to be the convention for including the leading 3
  d -= 1;
  // Shift n digits to the left of the radix point to obtain our final
  // result as a integer
  return Math.floor(
    16 ** n * mod(4 * S(1, d) - 2 * S(4, d) - S(5, d) - S(6, d), 1)
  );
}

console.log(piBBP(0,10))
console.log(piBBP(0,10).toString(16))
console.log(parseInt(piBBP(0,10).toString(16), 16));