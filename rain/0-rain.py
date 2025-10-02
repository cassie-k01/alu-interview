#!/usr/bin/python3
"""
Rainwater Retention Calculation
"""

def rain(walls):
    if not walls:
        return 0

    left, right = 0, len(walls) - 1
    left_max, right_max = walls[left], walls[right]
    water_trapped = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, walls[left])
            water_trapped += left_max - walls[left]
        else:
            right -= 1
            right_max = max(right_max, walls[right])
            water_trapped += right_max - walls[right]

    return water_trapped

if __name__ == "__main__":
    walls = [0, 1, 0, 2, 0, 3, 0, 4]
    print(rain(walls))  # Output: 6
    walls = [2, 0, 0, 4, 0, 0, 1, 0]
    print(rain(walls))  # Output: 6

