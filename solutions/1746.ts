function maxSumAfterOperation(nums: number[]): number {
    let prev_no_square = 0;
    let prev_square = 0;
    let max = 0
    for (const num of nums) {
        const no_square = Math.max(num, prev_no_square + num);
        const square = Math.max(num * num, prev_no_square + num * num, prev_square + num);
        const local_max = Math.max(prev_no_square, prev_square, no_square, square);
        max = local_max > max ? local_max : max;
        prev_no_square = no_square;
        prev_square = square;
    }
    return max;
};

console.log(maxSumAfterOperation([2, -1, -4, -3]))
console.log(maxSumAfterOperation([0, 0, 0, -4]))
console.log(maxSumAfterOperation([1, -1, 1, 1, -1, -1, 1]))
console.log(maxSumAfterOperation([0, -1, -1]))