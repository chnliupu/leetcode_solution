/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let prev = -Infinity;
    let max = prev;
    for(const num of nums) {
        local_max = Math.max(prev+num, num);
        max = Math.max(max, local_max);
        prev = local_max;
    }
    return max;
};

console.log(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
console.log(maxSubArray([1]))
console.log(maxSubArray([5,4,-1,7,8]))
