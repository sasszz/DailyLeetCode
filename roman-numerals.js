/**
 * @param {string} s
 * @return {number}
 */

// Input: s = "III"
// Output: 3
// Explanation: III = 3

// Input: s = "LVIII"
// Output: 58
// Explanation: L = 50, V = 5, III = 3.

// Input: s = "MCMXCIV"
// Output: 1994
// Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

s = "MCMXCIV"

var romanToInt = function (s) {
    roman = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 };
    let res = 0;
    for (let i = s.length - 1; i >= 0; i--) {
        if(roman[s[i]] < roman[s[i+1]]){
            console.log(roman[s[i]]);
            res -= roman[s[i]];
        }
        else{
            res += roman[s[i]];
        }
    }
    return res;
}

console.log(romanToInt(s))

// s="III"
// roman = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 };
// console.log(roman[s[0]])
