def maxArea(heights):
    maxarea = 0
    for i in range(len(heights)):
        for j in range(i + 1, len(heights)):
            maxarea = max(min(heights[i], heights[j]) * (j - i)
    return(maxArea)
