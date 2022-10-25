/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// Example 1:
// Input: nums = [2, 7, 11, 15], target = 9
// Output: [0, 1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

// Example 2:
// Input: nums = [3, 2, 4], target = 6
// Output: [1, 2]

// Example 3:
// Input: nums = [3, 3], target = 6
// Output: [0, 1]

nums = [3, 2, 3]
target = 6

var twoSum = function (nums, target) {
    // console.log(nums[0] + nums[nums.length-1]);
    if(nums[0] + nums[nums.length-1] === target) {
        let result = [];
        result.push(0, nums.length-1);
        return result;
    }
    for(let i=0; i < nums.length; i++){
        // console.log("i", i);
        let sum = 0;
        let result = [];
        for(let j=i; j < nums.length; j++){
            // console.log("j", j);
            sum += nums[j];
            // console.log("sum", sum);
            result.push(j);
            if(sum === target){
                return result;
            }
        }
    }
};

console.log(twoSum(nums, target))