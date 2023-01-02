class SparseVector {
    constructor(public nums: number[]) { }

    // Return the dotProduct of two sparse vectors
    dotProduct(vec: SparseVector): number {
        let sum = 0;
        this.nums.forEach((num_1, index) => {
            if (num_1 === 0 || vec.nums[index] === 0) {
                return;
            }
            sum += num_1 * vec.nums[index];
        })
        return sum;
    }
}

console.log(new SparseVector([1, 0, 0, 2, 3]).dotProduct(new SparseVector([0, 3, 0, 4, 0])));
console.log(new SparseVector([1, 0, 0, 0, 0]).dotProduct(new SparseVector([0, 0, 0, 0, 2])))
