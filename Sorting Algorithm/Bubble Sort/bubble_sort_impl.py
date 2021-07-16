class BubbleSort:
    def __init__(self, nums):
        self.nums = nums

    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def sort(self):
        for i in range(len(self.nums)-1):
            for j in range(len(self.nums)-i-1):
                if self.nums[j] > self.nums[j+1]:
                    self.swap(j, j+1)

if __name__ == '__main__':
    n = [-1,7,4,12,-87,-56,-199,199,76]
    bubble_sort = BubbleSort(n)
    bubble_sort.sort()
    print(bubble_sort.nums)