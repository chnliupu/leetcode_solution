function threeSum(nums: number[]): number[][] {
    nums.sort();
    let i = 0;
    let solution: number[][] = [];
    while (i < nums.length && !(nums[i] > 0)) {
        if (nums[i] != nums[i - 1]) {
            solution.push(...twoSum(nums, i));
        }
        i++;
    }
    return solution;
};

function twoSum(nums: number[], targetIndex: number): number[][] {
    const target = nums[targetIndex];
    const solution: number[][] = [];
    const visited = new Set<number>();
    let i = targetIndex + 1;
    while (i < nums.length) {
        const re: number = -target - nums[i];
        if (visited.has(re)) {
            solution.push([target, nums[i], re]);
            while (i + 1 < nums.length && nums[i] == nums[i + 1]) {
                i++;
            }
        }
        visited.add(nums[i]);
        i++;
    }
    return solution;
}

console.log(threeSum([0, 0, 0, 0]))
console.log(threeSum([-1, 0, 1, 2, -1, -4]));
console.log(threeSum([0, 1, 1]));
console.log(threeSum([0, 0, 0]));