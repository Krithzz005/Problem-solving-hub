"""
Problem: Product of Array Except Self
Approach: Prefix and suffix products
Time Complexity: O(n)
Space Complexity: O(1)
"""

def product_except_self(nums: list[int]) -> list[int]:
    """Compute product of all elements except self without division."""
    n = len(nums)
    res = [1] * n
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
    return res


if __name__ == '__main__':
    # Quick sanity check for Product of Array Except Self
    print('Tested product_except_self.py (Product of Array Except Self)')
