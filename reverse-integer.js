// Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

// Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

// Example 1:
// Input: x = 123
// Output: 321

// Example 2:
// Input: x = -123
// Output: -321

// Example 3:
// Input: x = 120
// Output: 21


console.log(Math.pow(2, 31))
console.log(Math.pow(-2, 31))

console.log(-1 / 10)

// /**
//  * @param {number} x
//  * @return {number}
//  */

let x = 123

var reverse = function (x) {
    let max = Math.pow(2, 31) - 1;
    let min = Math.pow(-2, 31);
    let res = 0;
    while(x != 0){
        let digit = x % 10;
        console.log("digit % 10 =", digit)
        x = Math.trunc(x/10);
        console.log("x/10 =", x)
        if(res > max / 10 || res == max/10 && digit >= max % 10){
            return 0;
        }
        if(res < min / 10 || res == min/10 && digit <= min % 10){
            return 0;
        }
        res = res * 10 + digit
    }
    return res;
};

console.log(reverse(123))
