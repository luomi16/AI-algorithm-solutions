def pancake_sort(arr):
    # 我们定义了一个名为 pancake_sort 的函数，它接受一个名为 arr 的参数。
    # arr 是我们要排序的煎饼堆栈（实际上是一个整数列表）。
    # 例如： [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    n = len(arr)
    # 初始化变量 n
    # 我们需要一个变量 n 来表示我们当前还需要排序的部分的长度。初始化为 arr 的长度。

    while n > 1:
        # 我们将使用一个 while 循环来进行排序，只要 n 大于1，我们就继续循环。
        # 这意味着我们至少有两个煎饼还没有排序。

        # Find the index of the largest element in arr[0...n-1]
        # 找到当前最大煎饼的位置
        # 我们使用 max() 函数找到当前未排序部分的最大值，并使用 index() 函数找到这个最大值在列表中的位置。
        idx_max = arr.index(max(arr[0:n]))

        # Bring the largest element to the top if it's not already there
        # 将最大煎饼移到正确的位置
        # 如果最大煎饼不在最底部，我们首先检查它是否在最顶部。如果不在顶部，我们将其翻到顶部。
        if idx_max != n - 1:
            if idx_max != 0:
                # Flip to bring idx_max to the front
                arr = arr[idx_max::-1] + arr[idx_max+1:]

            # Flip again to bring the largest element to the bottom
            # 然后，我们将最大的煎饼从顶部翻到它应该在的位置。
            arr = arr[n-1::-1] + arr[n:]

        # 我们已经将一个煎饼放在了它正确的位置，所以我们减小 n，
        # 然后继续循环直到所有的煎饼都排序好。
        n -= 1
    # 一旦所有煎饼都已经排序，我们返回排序后的 arr。
    return arr


# Test
pancakes = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(pancake_sort(pancakes))
